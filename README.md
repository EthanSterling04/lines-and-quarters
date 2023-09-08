# lines-and-quarters

Computer vision algorithms to detect slopes and the number of quarters in an image.

## Description

Each function receives a 2D structure of size 200x200 representing the intensity of pixels of a 200x200 pixel image and returns information about the content of it.

### _detect_slope_intercept(image)_

The function receives:
- A 2d structure called image[y][x] containing the pixel intensities of the image.

The function returns:
- A Line structure (see common.py) with the m and b fields containing the parameters
of the line function (mx+b=y).

Notes:
- The voting space is 2000x2000 “bins”
- m is bound to -10 and +10
- b is bound to -1000 and +1000
- The margin for correctness is +/-.1 for m and +/-3 for b

### _detect_circles(image)_

The function receives:
- A 2d structure called image[y][x] containing the pixel intensities of the image.

The function must return:
- An integer with the number of circles detected in the image.

Notes:
- The voting space is 200x200 (size of the image)
- The radius is always 30 (all circles have the same footprint)
- There are no overlapping circles or circles partially outside the image
