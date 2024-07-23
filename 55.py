import socket
def get_local_ip_address():
    return socket.gethostbyname(socket.gethostname())
if __name__ == "__main__":
    local_ip = get_local_ip_address()
    print(local_ip)