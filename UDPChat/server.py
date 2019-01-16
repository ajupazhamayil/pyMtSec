import socket
import threading
import time

host = "localhost"
sport = 5454
cport = 5455

def receive(s, stop_event):
  while(True and not stopEvent.is_set()):
    message=None
    addr=None
    s.settimeout(3.0)
    try:
      message, addr = s.recvfrom(2048)
    except Exception:
      pass
    if(message):
      print(str(addr)+" > "+str(message.decode()))

def send(s, stop_event):
  while(True and not stopEvent.is_set()):
    message = input()
    s.sendto(message.encode(), (host, cport))
    if(message=="bye"):
      stop_event.set()
    print(" > "+message)

if __name__=="__main__":
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((host, sport))
  stopEvent = threading.Event()
  sender=threading.Thread(target=send, args=(s, stopEvent))
  receiver=threading.Thread(target=receive, args=(s, stopEvent))
  sender.start()
  receiver.start()

  while not stopEvent.is_set():
    time.sleep(0.1)
  s.close()
  print("Completed the chat!")
