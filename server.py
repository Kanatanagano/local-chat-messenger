from faker import Faker
import socket
import os

def server():
    # Create a socket object
    s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server_address = './uds_socket'
    # Bind the socket to the port
    print('starting up on {}'.format(server_address))
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    s.bind(server_address)
    # Listen for incoming connections
    print('waiting for a connection')

    data, address = s.recvfrom(4096)
    print('received {!r}'.format(data))

    if data:
        print('sending data back to the client')
        fake = Faker()
        fake_text = fake.text().encode()
        sent = s.sendto(fake_text, address)
        print('sent data : {}'.format(fake_text))

    print('closing socket')
    s.close()   

if __name__ == "__main__":
    server()