# Multi-Client Chat Application  

This project is a **multi-client chat application** built using Python, combining backend server programming with a GUI-based client interface. It enables real-time communication between multiple clients through a TCP-based server.  

## Features  
### Server-Side:
- Handles multiple client connections concurrently using Python's `socket` and `threading` modules.  
- Broadcasts messages dynamically to all connected clients.  
- Manages active users effectively.  

### Client-Side:
- Provides a user-friendly chat interface using `tkinter`.  
- Displays real-time messages in a scrollable chat window.  
- Handles errors gracefully, including invalid usernames and empty messages.  

## Tech Stack  
- Python  
  - `socket` for networking  
  - `threading` for concurrent connections  
  - `tkinter` for GUI development  

## How to Run  
1. **Run the Server**:  
   - Open a terminal and navigate to the directory containing `server.py`.  
   - Start the server using:  
     ```bash
     python server.py
     ```  
   - The server will start listening for connections on the specified `HOST` and `PORT`.  

2. **Run the Client**:  
   - Open another terminal and navigate to the directory containing `client.py`.  
   - Start the client using:  
     ```bash
     python client.py
     ```  
   - Enter a username to join the chat.  

## Demo  
- Connect multiple clients to the server and see real-time message broadcasting.  

## Future Improvements  
- Add user authentication.  
- Support for emojis and file sharing.  
- Deployment on a cloud server for remote access.  

## License  
This project is licensed under the MIT License. Feel free to use, modify, and share!  

---

Feel free to reach out with any questions or suggestions! 😊  
