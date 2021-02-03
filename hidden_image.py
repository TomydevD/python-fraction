from PIL import Image

img = Image.open("C:/Users/Tomda/OneDrive/Bureau/Desktop/Dev/code.jpg")

binary = []
longueur = img.size[0]
hauteur = img.size[1]
send_convert = 0

def convert(color):
    binary = []
    send_convert = 0
    # print(color)
    for puissance in range(7,-1,-1):
        if color-2**puissance >= 0:
            color -= 2**puissance
            binary.append(1)
        else:
            binary.append(0)
    # print(binary)
    for octet in range(4,8):
        # print(octet)
        # print(binary[-1]*2**octet)
        send_convert += binary[-1]*2**octet
        del binary[-1]

    return send_convert

convert(182)

for i in range(hauteur):
    for y in range(longueur):
        my_pixel = img.getpixel((y,i))
        print(i)
        # print(my_pixel)
        new_color = convert(my_pixel)
        # print(new_color)
        img.putpixel((y,i),(new_color))


img.save("C:/Users/Tomda/OneDrive/Bureau/Desktop/Dev/resultat.jpg", "JPEG")