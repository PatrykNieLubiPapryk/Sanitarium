import random
pword = 0
selection = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
q = int(input("Podaj długość hasła: "))
if q <= 0:
    print("Nieprawidłowa długość hasła")
else:
    character = random.choice(selection)
    pword = character
    for i in range(q-1):
        character = random.choice(selection)
        pword += character
    print(pword)