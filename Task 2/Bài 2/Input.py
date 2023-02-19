from PIL import Image
img = Image.open(r"C:\Users\ASUS\Downloads\guitar.jpg")
pixel = img.load()

with open ("aaaa.txt", "w") as f:
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b= pixel[x, y]
            f.write("(" + str(r) + "," + str(g) + "," + str(b) + ") ")
        f.write("\n")