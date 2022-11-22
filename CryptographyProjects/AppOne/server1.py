import socket

msg = input("Enter your message: ")
message = msg.lower()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3213))

s.listen(5)

while True:
    client, address = s.accept()
    key = "abcdefghijklmnnopqrstuvwxyz01234567890 !@#$%^&~/\|%*()?><:;.,=+-"
    val = key[:: -1]

    # encrypter
    encrypter_msg = dict(zip(key, val))

    message = "".join([encrypter_msg[words] for words in message])

    client.send(bytes(message, "utf-8"))
