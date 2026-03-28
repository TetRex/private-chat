from keypair_generate import generate_keypair

a = int(input("Are you sender(1) or reciever(2): "))

keypair = generate_keypair()

def massage_convert(massage):
    return massage == hash(message)

match a:
    case 1:
        print("You are sender")
        public_key = input("Insert reciever public_key")
        def encrypt(message, public_key):
            n, e = public_key
            encrypted_message = [pow(ord(char), e, n) for char in message]
            return encrypted_message
    case 2:
        print("You are reciever")