from PIL import Image

# RGB values for recoloring.
red = (214, 45, 62)
blue = (0, 87, 231)
green = (0, 135, 68)
yellow = (255, 167, 0)

# Import image.
my_image = Image.open("ColorExplosion.jpeg")
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#find intensity
def Intense(arr):
    sum = 0
    for item in arr:
        sum+=item
    return sum

#change pixel data
for pix in image_list:
    i = Intense(pix)
    if i < 182:
        recolored.append(red)
    elif i > 182 and i < 364:
        recolored.append(blue)
    elif i > 364 and i < 546:
        recolored.append(green)
    else:
        recolored.append(yellow)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
