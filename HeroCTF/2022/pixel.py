from PIL import Image

# Get value of file 
# Template = r,g,b-r,g,b-r,g,b...
f = open("input.txt", "r")
data = f.read().split("-")

######################### First Image #########################
# create new image (3500 width, 1500 height)
first = Image.new('RGB', (3500, 1500))
i = j = a = 0

# for every line in image
while a < 1499:
    # parse value
    red, green, blue = data[i].split(",")

    # reset width counter
    if j % 3500 == 0:
        a += 1
        j = 0

    # Parse int
    red = int(red)
    green = int(green)
    blue = int(blue)

    # put pixel
    first.putpixel((j,a), (red,green,blue))

    i += 1
    j += 1

# save the first image
first = first.save("first.png")

######################### Poney Image #########################
# create new image (3500 width, 1500 height)
poney = Image.new('RGB', (3500, 1500))
i = j = a = 0
redSave = greenSave = blueSave = 0

# for every line in image
while a < 1499:
    # parse value
    red, green, blue = data[i].split(",")

    # reset width counter
    if j % 3500 == 0:
        a += 1
        j = 0

    # Parse int
    red = int(red)
    green = int(green)
    blue = int(blue)

    # Manage pixel
    # We part with all the pixel % 7 == 0
    # We save the last data of pixel because we haven't 3500 pixel of poney
    if j % 7 == 0:
        poney.putpixel((j,a), (red,green,blue))
        redSave = red
        greenSave = green
        blueSave = blue
    else:
        poney.putpixel((j,a), (redSave,greenSave ,blueSave))

    i += 1
    j += 1

# save image
poney = poney.save("poney.png")