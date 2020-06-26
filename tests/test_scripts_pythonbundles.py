# Run tests using pytest, e.g. from the root directory
#   $ python3 -m pytest --ignore tests/testing/ -vvv
#
# Requirements for this script:
# - Python >= 3.6
# - pytest
import pathlib
import pytest
import random
import sys
import subprocess

PYTHONBUNDLES = pathlib.Path(__file__).parent / '..' / 'pythonbundles.py'
TEST_DATA = pathlib.Path(__file__).parent / 'data' / 'scripts_pythonbundles'


def run_pythonbundles(*args, success=True):
    """
    Runs pythonbundles.py with given command line arguments

    Arguments:
      *args: Shell arguments passed to the script
      success:
       - true-ish: assert return code is 0 (default)
       - false-ish (excluding None): assert return code is not 0
       - None: don't assert return code value
    """
    cp = subprocess.run((sys.executable, PYTHONBUNDLES, *args), encoding='utf-8',
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if success:
        assert cp.returncode == 0, cp.stderr
    elif success is not None:
        assert cp.returncode != 0, cp.stdout
    return cp


projects = pytest.mark.parametrize('project', ('pkg_resources', 'pip', 'pipenv'))


@projects
def test_output_consistency(project):
    cp = run_pythonbundles(TEST_DATA / f'{project}.in')
    expected = (TEST_DATA / f'{project}.out').read_text()
    assert cp.stdout == expected, cp.stdout
    assert cp.stderr == '', cp.stderr


@pytest.mark.parametrize('namespace', ('python2dist', 'python3.11dist', 'pypy2.7dist'))
@projects
def test_namespace(project, namespace):
    cp = run_pythonbundles(TEST_DATA / f'{project}.in', f'--namespace={namespace}')
    expected = (TEST_DATA / f'{project}.out').read_text().replace('python3dist', namespace)
    assert cp.stdout == expected, cp.stdout
    assert cp.stderr == '', cp.stderr


@projects
def test_compare_with_identical(project):
    expected = (TEST_DATA / f'{project}.out').read_text()
    cp = run_pythonbundles(TEST_DATA / f'{project}.in', '--compare-with', expected)
    assert cp.stdout == '', cp.stdout
    assert cp.stderr == '', cp.stderr


@projects
def test_compare_with_shuffled(project):
    expected = (TEST_DATA / f'{project}.out').read_text()
    lines = expected.splitlines()
    # some extra whitespace and comments
    lines[0] = f'  {lines[0]}  '
    lines.extend([''] * 3)
    lines.append('# this is a comment on a single line')
    random.shuffle(lines)
    shuffled = '\n'.join(lines)
    cp = run_pythonbundles(TEST_DATA / f'{project}.in', '--compare-with', shuffled)
    assert cp.stdout == '', cp.stdout
    assert cp.stderr == '', cp.stderr


@projects
def test_compare_with_missing(project):
    expected = (TEST_DATA / f'{project}.out').read_text()
    lines = expected.splitlines()
    missing = lines[0]
    del lines[0]
    shorter = '\n'.join(lines)
    cp = run_pythonbundles(TEST_DATA / f'{project}.in', '--compare-with', shorter, success=False)
    assert cp.stdout == '', cp.stdout
    assert cp.stderr == f'Missing expected provides:\n    - {missing}\n', cp.stderr


@projects
def test_compare_with_unexpected(project):
    expected = (TEST_DATA / f'{project}.out').read_text()
    unexpected = 'Provides: bundled(python3dist(brainfuck)) = 6.6.6'
    longer = f'{expected}{unexpected}\n'
    cp = run_pythonbundles(TEST_DATA / f'{project}.in', '--compare-with', longer, success=False)
    assert cp.stdout == '', cp.stdout
    assert cp.stderr == f'Redundant unexpected provides:\n    + {unexpected}\n', cp.stderr
