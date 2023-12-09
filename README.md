# 🌱 Plant-Segmentation
This repository contains a technique for segmenting a set of plants and measuring their areas. Originally, this code was developed as my final project for the Digital Image Processing course, and the image included in this repository is one of many from the original dataset. However, due to limited access, I only had access to a single image. As a result, my code is designed to address the challenges of a single image. It's important to note that the solution may not perform optimally when applied to other plant images. Nevertheless, there is room for improvement, so feel free to use and implement a more general solution.

---

## *🗃️ Library*
• OpenCV <br/>
• NumPy <br/>

## *📄 Implemented method*
1. Process the image
2. Use Canny Edge Detection
3. Dilate the image
4. Find contours in the resulting image
5. Create a vector to store each area
6. Use Contour Approximation
7. Find the area for a closed contour
8. Create a vector to store each area
9. For each area, convert the measurement from pixel^2 to mm^2
10. In the source image, add text to each plant indicating its index

## *🔍️ Area approximation method*
In the image, there was a ruler that could be used to assist in measurement transformation
<img src="https://github.com/GabrielSpdf/Plant-Segmentation/blob/main/assets/aprox.png" width = 400>

## *📝 Results*
The results were good and significant; most plants have a concrete and feasible area. However... <br/>
<img src="https://github.com/GabrielSpdf/Plant-Segmentation/blob/main/assets/dilatedImage.jpg" width = 400> <img src="https://github.com/GabrielSpdf/Plant-Segmentation/blob/main/assets/enumImage.jpg" width = 400> <img src="https://github.com/GabrielSpdf/Plant-Segmentation/blob/main/assets/finalResult.jpg" width = 800>

## *🚨 Problems*
However, three plants have an incorrect area. Even though the code can handle most plants, it's important to note that there are errors <br/>
<img src="https://github.com/GabrielSpdf/Plant-Segmentation/blob/main/assets/error1.jpg" width = 400>
<img src="https://github.com/GabrielSpdf/Plant-Segmentation/blob/main/assets/error2.jpg" width = 400>

## *🔧 Possible solution*
For those who are reading and want to explore the code, I believe that a possible solution is to use the Otsu method to segment the plants, as the application of the threshold is automatic and efficient

## *ℹ️ Documentation*
For more information about the OpenCV library, please visit: [OpenCV](https://opencv.org/)

For additional details on the NumPy library, visit: [NumPy](https://numpy.org/)

To learn more about the Canny Edge Detection method, refer to: [Canny Edge Detection](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)

For in-depth information on Contour methods, explore:  [Contours](https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html)
