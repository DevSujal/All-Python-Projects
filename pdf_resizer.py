import cv2


source = "sujal.pdf"
scale = 0.5
destination = "newPdf.pdf"

pdf = cv2.imread(source)  # reading the image

cv2.imshow('my pdf', pdf)
cv2.waitKey(0)


# newwidth = int(image.shape[1] * scale)  # changing width of the image
# newheight = int(image.shape[0] * scale)  # changing height of the image

# output = cv2.resize(image, (newwidth, newheight))  # storing new image in a variable
# cv2.imwrite(
#     destination, output
# )  # generating image with extention .jpg if you want to change you can change it
# cv2.waitKey(0)
