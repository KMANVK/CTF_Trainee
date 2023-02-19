from PIL import Image

img = Image.open(r"C:\Users\ASUS\Downloads\Task 2\Bài 3\2.png")
pixels = img.load()

def extract_message_from_lsb(pixels):

    message = ""

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = pixels[x, y]
            message += bin(r)[-1]
            message += bin(g)[-1]
            message += bin(b)[-1]

            if message.endswith("00000000"):
                message = message[:len(message)-8]
                message = ''.join([chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8)])
                return message

    return None

message = extract_message_from_lsb(pixels)
print(message)