import socket
import server


def Receiver():
    yourEmail = input("Enter your Email Address: ")
    yourEmail = yourEmail.lower()

    if len(yourEmail) ==len(server.Receiver_email) and len(server.EmailKey) == 64:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((socket.gethostname(), 3232))

        message = s.recv(1000)
        message = message.decode("utf-8")

        val = server.EmailKey[:: -1]
        decrypter = dict(zip(val, server.EmailKey))

        message = "".join([decrypter[words] for words in message])
        print("Your Decrypted Message is:\n", message)
    else:
        print("You entered a wrong key!. You're authorized for this info")


if __name__ == '__main__':
    Receiver()