from PIL import Image
import sys

image = sys.argv[1]
img = Image.open(image)
filtered = img.copy()
width, height = img.size


for x in range(width):
    for y in range(height):
        col = img.getpixel((x, y))
        col = (256-col[0], 256-col[1], 256-col[2])
        grey = int((col[0] + col[1] + col[2])/3)
        col = grey, grey, grey
        filtered.putpixel((x, y), col)

filtered.save("filtered.png", "PNG")
filtered.show()
