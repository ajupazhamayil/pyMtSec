import socket
import threading
import time

host = "localhost"
#cport = 5454
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
      print(str(addr)+" > "+str(message.decode()))

def send(s, addr, stop_event):
  while(True and not stopEvent.is_set()):
    message = input()
    s.send(message.encode())
    if(message=="bye"):
      stop_event.set()
    print(" > "+message)

if __name__=="__main__":
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, sport))
  stopEvent = threading.Event()
  conn = s
  addr = host
  sender=threading.Thread(target=send, args=(conn, addr, stopEvent))
  receiver=threading.Thread(target=receive, args=(conn, addr, stopEvent))
  sender.start()
  receiver.start()

  while not stopEvent.is_set():
    time.sleep(0.1)
  conn.close()
  print("Completed the chat!")
