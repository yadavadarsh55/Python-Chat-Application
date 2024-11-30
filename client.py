# import required modules 
import socket
import threading
import tkinter as tk
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 13)

# # Creating the Style Object 
# style = Style()
# style.configure('TButton', font = (BUTTON_FONT, 10), foreground = OCEAN_BLUE, bg = WHITE)

# creating the socket object as client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def adding_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')

def connect():
    # Connect to the server
    try:
        client.connect((HOST, PORT)) 
        print("Sucsessfully connected to the server")
        adding_message("[SERVER]: Succsfully Connected to the SERVER")
    except:
        messagebox.showerror("ERROR",f"Unable to connect with the Server {HOST} {PORT}")
        exit(0)

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid Username", "Username cannot be empty")
        exit(0)

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    username_button.config(tk.DISABLED)
    username_textbox.config(tk.DISABLED)

def send_message():
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0,len(message))
    else:
        messagebox.showerror("Error","Message is empty")



root = tk.Tk()
root.geometry("600x600")
root.title("Chat Application")
root.resizable(False,False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, height=100, width=600, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, height=400, width=600, bg=MEDIUM_GREY)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, height=100, width=600, bg=DARK_GREY)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text="Enter Username: ",bg=DARK_GREY, font=FONT, fg=WHITE)
username_label.pack(side=tk.LEFT,padx=10)

username_textbox = tk.Entry(top_frame, bg=MEDIUM_GREY, fg=WHITE, width=50)
username_textbox.pack(side=tk.LEFT)

username_button = tk.Button(top_frame, text="Join", font=BUTTON_FONT, command=connect)
username_button.pack(side=tk.LEFT, padx=15)

message_textbox = tk.Entry(bottom_frame, bg=MEDIUM_GREY, fg=WHITE, width=80)
message_textbox.pack(side=tk.LEFT, padx=15)

message_button = tk.Button(bottom_frame, text="Send", font= BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=15)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=27.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


HOST = '192.168.56.133'
PORT = 1234

def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split("~")[1]
            adding_message(f"[{username}]: {content}")
        else:
            messagebox.showerror("Message Error","The message received from the client is empty")

# main funtion 
def main():

    # This mainloop will start a window of tk 
    root.mainloop()

if __name__ == "__main__":
    main()