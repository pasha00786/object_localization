from skimage import io as skio 
url = '1.png'
img = skimage.io.imread(url)

print("shape of image: {}".format(img.shape))
print("dtype of image: {}".format(img.dtype))