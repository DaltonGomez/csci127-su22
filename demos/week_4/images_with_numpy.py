import matplotlib.image as img
import matplotlib.pyplot as plt

# load image as pixel array
vernaCat = img.imread("figs/Verna.JPG")
# summarize shape of the pixel array
print(vernaCat)
print(type(vernaCat))
print(vernaCat.dtype)
print(vernaCat.shape)

# remove all red
for row in range(vernaCat.shape[0]):
    for column in range(vernaCat.shape[1]):
        vernaCat[row][column][1] = 0
        vernaCat[row][column][2] = 0
# display the array of pixels as an image
plt.imshow(vernaCat)
plt.show()
