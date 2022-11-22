import socket

decryption_key = input("Enter your decryption key: ")

if len(decryption_key) == 64:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((socket.gethostname(), 3213))

    message = s.recv(1000)
    message = message.decode("utf-8")

    val = decryption_key[:: -1]
    decrypter = dict(zip(val, decryption_key))

    message = "".join([decrypter[words] for words in message])
    print("Your Decrypted Message is: ", message)
else:
    print("You entered a wrong key!. You're authorized for this info ")