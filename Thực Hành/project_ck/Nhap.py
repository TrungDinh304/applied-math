import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from PIL import Image



img = mpimg.imread('eeao.png')
print(img.shape) 
rows, cols, colors = img.shape
#Showing the image

img_r = np.reshape(img, (rows, cols*colors))
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4), sharey=True, dpi=120)
ax1.imshow(img)


pca = PCA(32).fit(img_r) 
img_transformed = pca.transform(img_r) 
print(img_transformed.shape) 
print(np.sum(pca.explained_variance_ratio_) )


temp = pca.inverse_transform(img_transformed) 
print(temp.shape)
temp = np.reshape(temp, (rows, cols ,colors)) 
print(temp.shape) 


ax2.imshow(temp)

plt.show()

output_file = 'output.png'

# Export image to file
Image.fromarray(temp.astype(np.uint8)).save(output_file)