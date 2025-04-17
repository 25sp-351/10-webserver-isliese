# main.py
# Main server file

import socket
import threading
import sys

from request_parser import parse_http_request
from response_builder import build_http_response
from handler_static import handle_static_request
from handler_calc import handle_calc_request

def handle_client_connection(client_socket: socket.socket):
    """
    Handle a single client request.
    """
    try:
        request_data = client_socket.recv(1024)
        if not request_data:
            print("No data received.")
            return

        print("=== Raw Request ===")
        print(request_data)
        print("===================")

        request = parse_http_request(request_data)
        method = request['method']
        path = request['path']
        headers = request['headers']

        print(f"Method: {method}, Path: {path}")

        # Process GET Method
        if method != 'GET':
            response = build_http_response(405, "text/plain", b"Method Not Allowed")
        elif path.startswith('/static'):  # Static path
            status, content_type, body = handle_static_request(path)
            response = build_http_response(status, content_type, body)
        elif path.startswith('/calc'):    # Calc path
            status, content_type, body = handle_calc_request(path)
            response = build_http_response(status, content_type, body)
        else:
            response = build_http_response(404, "text/plain", b"Not Found")

        client_socket.sendall(response)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_server(port: int):
    """
    Start the HTTP server.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(5)

    print(f"Server listening on port {port}...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            # Create a thread per client
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    # Default port 80
    port = 80

    # Parse command-line argument
    if len(sys.argv) >= 3 and sys.argv[1] == "-p":
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Invalid port number. Using default port 80.")

    start_server(port)