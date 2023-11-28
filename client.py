import socket
import os

def client():
    # Create a socket object
    s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAMtets)
    server_address = './uds_socket'
    client_address = './uds_socket_client'
    # Connect the socket to the port where the server is listening
    print('connecting to {}'.format(server_address))
    try:
        os.unlink(client_address)
    except FileNotFoundError:
        pass

    s.bind(client_address)

    try:
        # Send data
        message = input("Enter message: ").encode()
        print('sending {!r}'.format(message))
        sent = s.sendto(message, server_address)

        # Look for the response
        data, server = s.recvfrom(4096)
        print('received {!r}'.format(data))
    finally:
        print('closing socket')
        s.close()


if __name__ == "__main__":
    # Create a socket object
    client()
