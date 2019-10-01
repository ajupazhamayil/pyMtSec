import socket
import threading
import time

host = "localhost"
# Ports for client and server
cport = 5454
sport = 5455

def receive(s, addr, stop_event):
  while(True and not stopEvent.is_set()):
    message=None
    addr=None
    s.settimeout(3.0)
    try:
      message = s.recv(2048)
    except Exception:
      pass
    if(message):
      print("partner"+" > "+str(message.decode()))

def send(s, addr, stop_event):
  while(True and not stopEvent.is_set()):
    message = input()
    s.send(message.encode())
    if(message=="bye"):
      stop_event.set()
    print(" > "+message)

# Create socket for the server, bind it to the port, listen to incoming connections and create threads for sender and receiver.
if __name__=="__main__":
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host, sport))
  s.listen(1)
  conn, addr = s.accept()
  stopEvent = threading.Event()
  sender=threading.Thread(target=send, args=(conn, addr, stopEvent))
  receiver=threading.Thread(target=receive, args=(conn, addr, stopEvent))
  sender.start()
  receiver.start()

  while not stopEvent.is_set():
    time.sleep(0.1)
  conn.close()
  s.close()
  print("Completed the chat!")
