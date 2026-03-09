import socket

def grab_banner(target, port):

    try:
        sock = socket.socket()
        sock.settimeout(2)

        sock.connect((target, port))

        sock.send(b"HEAD / HTTP/1.1\r\nHost: test\r\n\r\n")

        banner = sock.recv(1024).decode(errors="ignore")

        sock.close()

        return banner

    except:
        return "Unknown"
