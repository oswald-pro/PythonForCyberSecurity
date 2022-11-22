import socket

Receiver_email = input("Enter your Receiver Email Address: ")
Receiver_email = Receiver_email.lower()

EmailKey = "abcdefghijklmnnopqrstuvwxyz01234567890 !@#$%^&~/\n|%*()?><:;.,=+-"


def Sender():
    msg = input("Enter your message: ")

    msg = msg.lower()

    message = ("    from: {}\n     message: {}".format(Receiver_email, msg))
    print(message)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 3232))

    s.listen(5)

    while True:
        my_client, address = s.accept()
        key = EmailKey
        val = key[:: -1]

        # encrypter
        encrypter_msg = dict(zip(key, val))

        email = "".join([encrypter_msg[words] for words in Receiver_email])
        message = "".join([encrypter_msg[words] for words in message])

        # my_client.send(bytes(email, "utf-8"))
        my_client.send(bytes(message, "utf-8"))


if __name__ == '__main__':
    Sender()



