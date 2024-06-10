import pytest
from unittest import mock
from unittest.mock import patch, MagicMock
import os
# Import the UdpComms class
from client.UdpComms import UdpComms

@patch('socket.socket')
def test_send_data(mock_socket):
    # Set up the mock socket
    mock_sock_instance = MagicMock()
    mock_socket.return_value = mock_sock_instance

    udp_ip = "127.0.0.1"
    port_tx = 5005
    port_rx = 5006
    message = "Test Message"

    # Create an instance of UdpComms for sending
    udp_comms = UdpComms(udpIP=udp_ip, portTX=port_tx, portRX=port_rx)

    # Call the SendData method
    udp_comms.SendData(message)

    # Assert that the sendto method was called with the correct parameters
    mock_sock_instance.sendto.assert_called_with(bytes(message, 'utf-8'), (udp_ip, port_tx))
    
def test_udp_comms_clock_socket():
    udp_comms = UdpComms("127.0.0.1", 8000, 8001)
    udp_comms.CloseSocket()
    
def test_udp_comms_receive_data_false():
    udp_comms = UdpComms("127.0.0.1", 8000, 8001, enableRX=False)
    with pytest.raises(ValueError, match="Attempting to receive data without enabling this setting. Ensure this is enabled from the constructor"):
        udp_comms.ReceiveData()
        
def test_udp_comms_read_received_data_none():
    udp_comms = UdpComms("127.0.0.1", 8000, 8001)
    assert udp_comms.ReadReceivedData() == None
    
@patch('socket.socket')
def test_read_data(mock_socket):
    if os.name == 'posix':
        udp_comms = UdpComms("127.0.0.1", 8000, 8001, enableRX=True)
        with pytest.raises(NameError):
            udp_comms.ReceiveData()
    else:
        # Set up the mock socket
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance

        udp_ip = "127.0.0.1"
        port_tx = 5005
        port_rx = 5006
        message = "Test Message"
        encoded = bytes(message, "utf-8")

        mock_sock_instance.readData.return_value = (encoded, (udp_ip, port_tx))
        # Create an instance of UdpComms for sending
        udp_comms = UdpComms(udpIP=udp_ip, portTX=port_tx, portRX=port_rx, enableRX=True)

        # Call the SendData method
        data = udp_comms.ReceiveData()

        assertEqual(encoded, data)
