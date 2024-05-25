import cv2


source = "C:Users/SUJAL NIMJE/OneDrive/Pictures/Saved Pictures/RCOEM-Nagpur-Logo.webp"
scale = 0.8
destination = "newImage.jpg"

image = cv2.imread(source)  # reading the image

# cv2.imshow('my image', image)
# cv2.waitKey(0)


newwidth = int(image.shape[1] * scale)  # changing width of the image
newheight = int(image.shape[0] * scale)  # changing height of the image

output = cv2.resize(image, (newwidth, newheight))  # storing new image in a variable
cv2.imwrite(
    destination, output
)  # generating image with extention .jpg if you want to change you can change it
# cv2.waitKey(0)
