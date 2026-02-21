# Socket - Assignment 

This project is a simple way to show how two programs (a Client and a Server) can talk to each other over a network using Python.



## 1. What this project does
I have created two Python files:
* **The Client**: This program asks you for a number, sends it to the server, and then waits for an answer.
* **The Server**: This program stays open and waits for the client. When it gets a message, it picks its own number, adds it to the client's number, and sends the information back.

## 2. How it works (Design)
I used **TCP Sockets** for this project because they are reliable.
- The server starts first and listens on **Port 5005**. 
- The client connects to the server's IP address.
- They exchange messages as simple strings (text). I used a comma to separate the Name and the Number so the programs can easily read them.

## 3. Why I made these choices
- **Language**: I used Python because it is easy to read and has a great `socket` library.
- **Protocol**: I used a simple comma-separated format. It's not as complex as professional formats, but it works perfectly for this assignment.
- **Port 5005**: I chose this because the instructions said to use a port number higher than 5000.

## 4. How to make it better
If I had more time, I would:
1. Make it a **Concurrent Server**: This means the server could talk to many students at the same time using "Threads."
2. Add a **GUI**: Instead of a black terminal screen, I could make a window with buttons.

## 5. Testing
I tested the code to make sure it doesn't crash:
* **Test 1**: I entered `10`. Result: Server replied correctly and we both got the right sum.
* **Test 2**: I entered `150` (Out of range). Result: The server closed its connection and shut down safely as required.
* **Test 3**: I connected to a classmate's IP. Result: It worked!

## 6. How to Run My Code
**Run Server**: Open a terminal and type `python server.py`.
**Run Client**: Open a second terminal and type `python client.py`.