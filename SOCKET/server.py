import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    conn, address = s.accept()
    print(f"Connection from {address} has been established.")
    full_msg = ''
    while conn:
        msg = s.recv(8)
        full_msg += msg.decode("utf-8")
    print(full_msg)