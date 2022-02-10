import socket
import time
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

    command = input()

    if (command == '0'):
        break

    print("Enter number of client: ")
    client_num = input()



    startTimer = time.time()


    s.send(command.encode())
    s.sned(client_num.encode())

    print(s.recv(1024))

    print()

    stopTimer = time.time()
    totalTime = round(stopTimer - startTimer, 2)
    avgTime = round(totalTime / client_num, 2)

    print("Total turn around time:", totalTime * 100, "ms")
    print()
    print("Average time of response:", avgTime * 100, "ms")



    print("--------------------")
    print()

s.close()