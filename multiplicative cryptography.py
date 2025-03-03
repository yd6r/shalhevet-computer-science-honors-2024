import math

# The 'alphabet' is specific to this program, and does not contain many basic characters such as [], &, and "".
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?',.() "


# Checks if the key is coprime with the alphabet
def are_coprime(a, b):
    return math.gcd(a, b) == 1


# Function to find the modular inverse of a number
def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1


# Takes parameter 'multiply_key', the number which will be used in the multiplicative algorithm, and then asks for a message.
# The key MUST be prime or the program will not work correctly.
# The message is then run through the multiplicative algorithm to produce the encoded message. The encoded message will change
# depending on the value of 'multiply_key'.
def multiplicative_encode(multiply_key):
    message = input("What message would you like to encode?")
    for letter in message:
        pos = alphabet.find(letter)
        if pos == -1:
            print("ERROR", end="")
        else:
            convert = (pos * multiply_key) % len(alphabet)
            print(alphabet[convert], end="")


# Takes parameter 'multiply_key' and asks for an encoded message. If 'multiply_key' is not coprime with the size of the alphabet,
# the function will return an error. The key will be used in the algorithm to reverse-engineer the encoding process and return the decoded message.
def multiplicative_decode(multiply_key):
    if not are_coprime(multiply_key, len(alphabet)):
        print("The key is not coprime with the size of the alphabet. Please use a valid key.")
        return

    inverse_key = modular_inverse(multiply_key, len(alphabet))
    encoded_message = input("What message would you like to decode? ")
    for letter in encoded_message:
        pos = alphabet.find(letter)
        if pos == -1:
            print("ERROR", end="")
        else:
            convert = (pos * inverse_key) % len(alphabet)
            print(alphabet[convert], end="")


# This is the part the user interacts with. It asks the user to choose to encode or decode a message, and if the response
# matches neither, resets. It will run functions encode_multiplicative() or decode_multiplicative to encode or decode
# a given message.
encode_or_decode = input("For encoding a message, type 'encode'. For decoding a message, type 'decode'.")
if encode_or_decode != "encode" and encode_or_decode != "decode":
    while encode_or_decode != "encode" and encode_or_decode != "decode":
        print("'" + encode_or_decode + "' is not a valid response.")
        encode_or_decode = input("For encoding a message, type 'encode'. For decoding a message, type 'decode'.")

if encode_or_decode == "encode":
    try:
        multiply_key = int(input("What is the key?"))
    except ValueError:
            multiply_key = int(input("That is not a number key. Please enter a valid key."))
    while not are_coprime(multiply_key, len(alphabet)):
        multiply_key = int(input("That key is not coprime with the length of the alphabet used here("+str(len(alphabet))+"). Please enter a valid key."))
    multiplicative_encode(multiply_key)
elif encode_or_decode == "decode":
    try:
        multiply_key = int(input("What is the key?"))
    except ValueError:
        multiply_key = int(input("That is not a number key. Please enter a valid key."))
    while not are_coprime(multiply_key, len(alphabet)):
        multiply_key = int(input("That key is not coprime with the length of the alphabet used here("+str(len(alphabet))+"). Please enter a valid key."))
    multiplicative_decode(multiply_key)
