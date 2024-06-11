from GroupCommunication.main import run_script
import pytest

@pytest.fixture
def mock_os_system(mocker):
    return mocker.patch('os.system')

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('builtins.open', mocker.mock_open())

def test_run_script(mock_os_system):
    script_name = 'dummy_script.py'
    run_script(script_name)
    mock_os_system.assert_called_once_with(f'python {script_name}')

