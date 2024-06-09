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


def test_udp_comms_send_data(mock_socket):
    mock_sock_instance = mock_socket.return_value
    udp_comms = UdpComms("127.0.0.1", 8000, 8001)

    udp_comms.SendData("Test message")
    
    
def test_udp_comms_clock_socket(mock_socket):
    mock_sock_instance = mock_socket.return_value
    udp_comms = UdpComms("127.0.0.1", 8000, 8001)

    udp_comms.CloseSocket()
    
    
def test_udp_comms_receive_data(mock_socket):
    mock_sock_instance = mock_socket.return_value
    udp_comms = UdpComms("127.0.0.1", 8000, 8001, enableRX=False)
    with pytest.raises(ValueError, match="Attempting to receive data without enabling this setting. Ensure this is enabled from the constructor"):
        udp_comms.ReceiveData()

     
    
        
def test_udp_comms_read_received_data(mock_socket):
    mock_sock_instance = mock_socket.return_value
    udp_comms = UdpComms("127.0.0.1", 8000, 8001)

    assert udp_comms.ReadReceivedData() == None
    
def test_there(mock_socket):
    mock_sock_instance = mock_socket.return_value
    udp_comms_one = UdpComms("127.0.0.1", 8000, 8001, enableRX=True)
    
    # Simulate recvfrom returning an empty tuple
    mock_sock_instance.recvfrom.return_value = ()  # This will trigger the ValueError

    with pytest.raises(ValueError, match=r"not enough values to unpack \(expected 2, got 0\)"):
        udp_comms_one.ReceiveData()    