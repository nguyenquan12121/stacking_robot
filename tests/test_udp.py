import pytest
from unittest.mock import patch, MagicMock

# Import the UdpComms class
from client.UdpComms import UdpComms

@pytest.fixture
def mock_socket(mocker):
    """Mock the socket module"""
    return mocker.patch('socket.socket')

@pytest.fixture
def mock_threading(mocker):
    """Mock the threading module"""
    return mocker.patch('threading.Thread')

def test_udp_comms_initialization(mock_socket, mock_threading):
    mock_sock_instance = mock_socket.return_value
    mock_sock_instance.bind.return_value = None

    udp_comms = UdpComms("127.0.0.1", 8000, 8001, enableRX=True)

    mock_threading.return_value.start.assert_called_once()

def test_udp_comms_send_data(mock_socket):
    mock_sock_instance = mock_socket.return_value
    udp_comms = UdpComms("127.0.0.1", 8000, 8001)

    udp_comms.SendData("Test message")