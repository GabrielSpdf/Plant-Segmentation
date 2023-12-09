# Plant-Segmentation
This repository contains a technique for segmenting a set of plants and measuring their areas. Originally, this code was developed as my final project for the Digital Image Processing course, and the image included in this repository is one of many from the original dataset. However, due to limited access, I only had access to a single image. As a result, my code is designed to address the challenges of a single image. It's important to note that the solution may not perform optimally when applied to other plant images. Nevertheless, there is room for improvement, so feel free to use and implement a more general solution.

---

## Library
• OpenCV <br/>
• Numpy <br/>

## Implemented method
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

## Results


