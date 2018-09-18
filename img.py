from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('4096.png'))
print(img.shape)
print(img.dtype)
print(img.size)
print(type(img))


dot = 0
second = 0
for i in range(4096):
	for j in range(4096):		
		img[i, j, 2] = dot % 256
		second = dot // 256
		img[i, j, 0] = second // 256
		img[i, j, 1] = second % 256
		dot = dot + 1
		second = 0
		#print(img[i, j, 2], img[i, j, 1], img[i, j, 0], dot)

'''
total0 = 0
total1 = 0
total2 = 0
for i in range(4096):
	for j in range(4096):		
		total0 = total0 + img[i, j, 0]
		total1 = total1 + img[i, j, 1]
		total2 = total2 + img[i, j, 2]

print(total0, total1, total2)
'''

plt.figure("love")
plt.imshow(img)
plt.axis('off')
plt.show()        

im = Image.fromarray(img)
im.save('love.png')