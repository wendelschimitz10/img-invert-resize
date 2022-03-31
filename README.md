#2 code made in the PDI class, to resize image size and invert.
Using Python libraries, called: cv2.
1) Reading the original image.
```
imageOriginal = cv2.imread("img/praia_invertida.png")
```
2) Decreasing the image size
```
imageResized = cv2.resize(imageOriginal, None, fx = 0.3, fy = 0.3)

```
3) Taking axes
```
height = imageResized.shape[0]
width = imageResized.shape[1]
middle = (width/2, height/2)
```
4) Getting rotation image
```
matrix = cv2.getRotationMatrix2D(middle, 180,1)
```
5) Rotating the image
```
imageRotate = cv2.warpAffine(imageResized, matrix,(width, height)) 
```
