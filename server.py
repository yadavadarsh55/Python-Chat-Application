# import modules required
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
# This will limit the server to the number of listeners
LISTENER_LIMIT = 5
# This list will contain the username of the clients which are currently connected to the server
active_clients = [] 

# Funtion to listen the upcoming messages sent by the client 
def listen_to_messages(client, username):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message sent from the client {username} is empty")

# Function to send the message to all the clients conected to the server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1],message)

# Funtion to seend message to a single client 
def send_message_to_client(client,message):
    client.sendall(message.encode())

# Function to handle client
def client_handler(client):
    # server will listen to the client message which contains the username
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != "":
            active_clients.append((username,client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("The client username is empty")

    threading.Thread(target=listen_to_messages, args=(client, username, )).start()

# main funtion
def main():
    # creating the server socket class obect
    # AF_INET : we are going to use IPv4 addresses
    # SOCK_STREAM : we are uisng the TCp packet for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # creating the try block
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} and {PORT}")
    except:
        print(f"Unable to bind the the HOST {HOST} and port {PORT}")

    # set server limit
    server.listen(LISTENER_LIMIT)

    # This loop will keep listening to the clients
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to the client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()


if __name__ == "__main__":
    main()
