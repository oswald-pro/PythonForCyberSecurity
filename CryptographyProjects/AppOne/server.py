my_msg = input("Please enter your message:")

# Let's convert the inputted message in lowercase
msg = my_msg.lower()

# Let's create a key and a value for the cryptographic dictionary
key = "abcdefghijklmnnopqrstuvwxyz01234567890 !@#$%^&~/\|%*()?><:;.,=+-"
val = key[:: -1]

# encrypter
encrypter_msg = dict(zip(key, val))

# encrypt the message
encrypt_msg = "".join([encrypter_msg[words] for words in msg])
print("Your Encrypted Message is: ", encrypt_msg)

# decrypt the message
decrypter_msg = dict(zip(val, key))

# decrypt the message
decrypt_msg = "".join([decrypter_msg[words] for words in encrypt_msg])
print("Your Decrypted Message is: ", decrypt_msg)
