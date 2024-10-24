import socket

host = '127.0.0.1'
port = 5010

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Server 1 running on {host}:{port}")
    while True:
        conn, addr = s.accept()
        with conn:
            # Sending a proper HTTP response
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type: text/html\r\n'
            response += 'Content-Length: 19\r\n'  # Specify the content length
            response += 'Connection: keep-alive\r\n'  # Keep the connection alive
            response += '\r\n'
            response += 'Hello from Server 1'  # Body content
            try:
                conn.sendall(response.encode('utf-8'))  # Send response
                print(f"Connected by {addr} because got request on this sever")
            except BrokenPipeError as e:
                print(f"Connected by {addr}" + " because HAProxy is doing health checkup.")
            except Exception as e:
                print(f"Unexpected error: {e}")

