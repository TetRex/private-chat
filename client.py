a = int(input("Are reciever(1) or sender(2): "))
p = 456
q = 324
e = 40
N = p * q
fN = (p - 1) * (q - 1)
public_key = {fN,e}
print(public_key)
"""
def sender():
    print("You are sender")
    massege = input()
    public_key = input("Input recievers public key: ")
    
if a == 1:
    print("You are reciever")
    print(f"Your public key: {public_key}")
elif a == 2:
    sender()
else:
    raise Exception("Wrong answer")


"""