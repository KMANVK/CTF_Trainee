from PIL import Image
imgt = Image.open(r"C:\Users\ASUS\Downloads\Task 2\Bài 3\Messi.png")
img = imgt.convert("RGB")
pix = img.load()
messi = Image.new(img.mode, img.size)
goat = messi.load()

def lenbuf(val):
    while len(val) < 8:
        val = '0' + val
    return val

txt = input("Name to hide: ")
cipher = ""
for i in txt:
    cipher += lenbuf(bin(ord(i))[2:])
index = 0

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b = pix[x, y]
        if index < len(cipher):
            red = lenbuf(bin(r)[2:]); red = int(red[-1] + cipher[index])
            index += 1
        else:
            red = r
        
        if index < len(cipher): 
            green = lenbuf(bin(g)[2:]); green = int(green[-1] + cipher[index])
            index += 1
        else:
            green = g

        if index < len(cipher):
            blue = lenbuf(bin(b)[2:]); blue = int(blue[-1] + cipher[index])
            index += 1
        else:
            blue = b
        goat[x, y] = red, green, blue

messi.save("2.png")
