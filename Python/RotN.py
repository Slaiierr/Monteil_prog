def rotN_chr_ord(message, n):
    rot = n
    transform = []
    for car in message:
        if car == car.lower():
            decalage = 97
        else:
            decalage = 65
        # print(car)
        # print(ord(car))
        # print((ord(car)+rot-97)%26+97)
        chiffree = ((ord(car)+rot-decalage) % 26) + decalage
        # print(chr(chiffree))
        transform.append(chr(chiffree))
    return ''.join(transform)


message = "doDO"
# message = message.lower() # Enlève les majuscules dans le msg
transf = rotN_chr_ord(message, 3)
print(transf)
print(rotN_chr_ord(transf, 23))
