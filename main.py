import socket

ip = input("Enter IP address to scan:")


for ports in range(1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if s.connect_ex((ip, ports)) == 0:
        print("Success for the address: " + ip + ":" + str(ports))

        try:
            s.send(b'HEAD / HTTP/1.0\r\n\r\n')
            response = s.recv(1024)
            response_dec = response.decode('utf-8')
            print(response_dec)
        except:
            print("No banner retrieved")
