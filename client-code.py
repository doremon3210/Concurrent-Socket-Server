import socket
import time
import threading
# import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '139.62.210.153'
# Host = sys.argv[1]
PORT = 1111
# Host = sys.argv[2]

s.connect((HOST, PORT))


while (True):
    print("--------------------")
    print("1: Get the server's Date and Time")
    print("2: Get the server's Uptime")
    print("3: Get the server's Memory Usage")
    print("4: Get the server's Netstat")
    print("5: Get the server's Current Users")
    print("6: Get the server's Running Processes")
    print("0: Exit")

    command = int(input())

    if (command == '0'):
        print("Exiting the Program")
        break

    print("Enter number of client: ")
    client_num = int(input())



    startTimer = time.time()

    for i in range(client_num):
        t = threading.Thread(target = s.send(command.encode()))
        #t = threading.Thread(target = s.send(), args = (command.encode(),))
        t.start()
        
        #s.send(client_num.encode())

        print(s.recv(1024))

        t.join()

    print()

    stopTimer = time.time()
    totalTime = stopTimer - startTimer
    avgTime = totalTime / client_num

    print("Total turn around time:", round(totalTime * 100, 3), "ms")
    print()
    print("Average time of response:", round(avgTime * 100, 3), "ms")



    print("--------------------")
    print()

s.close()