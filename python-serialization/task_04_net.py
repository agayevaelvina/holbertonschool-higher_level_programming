#!/usr/bin/env python3

import socket
import json

def start_server(host='127.0.0.1', port=65432):
    "x"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            try:
                data = conn.recv(4096)  # Receive up to 4096 bytes
                if data:
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received dictionary:")
                    print(received_dict)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

def send_data(data_dict, host='127.0.0.1', port=65432):
    "x"
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            serialized_data = json.dumps(data_dict).encode('utf-8')
            client_socket.sendall(serialized_data)
            print("Data sent successfully.")
    except ConnectionRefusedError:
        print("Connection failed: server may not be running.")
    except Exception as e:
        print(f"An error occurred while sending data: {e}")
