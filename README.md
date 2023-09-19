# FourierTransformations
My implementation of Fourier Transformations, and some explanations. I've used Manim to render stuff here.
Required libraries are svgpathtools, manim(and its dependencies) and numpy.

## How this works
  I highly encourage you to watch 3Blue1Brown's video on Fourier Series. That will be what I assume you know. Hopefully this explains how 3b1b made his animations. 
  Anyways lets go. f(t), the same function as 3b1b shows in his video, is the function that parametrically describes the path we wish to trace out. It takes in the parameter t and outputs a complex number. As t ranges between 0 and 1, it covers all points on the path. Say if you put t as 0.5, it would return a value 2+3i. Note that the parameter t can vary outside of 0 and 1 too, it would just retrace the path.
  This f(t) is the function `point_t(t)` in `generate_coefficients.py`. For a given t, it returns a complex number from the svg imported.
  The SVGs are read using the library svgpathtools. The path from the svg is obtained, and this is what `point_t(t)` uses. 
  To find the coefficients, as mentioned in the video, we have the formula $$c_n = \int_{0}^{1} f(t) \cdot e^{2n \pi it} \thinspace dt$$
  To achieve the integration, I've performed numerical integration, where one selects a very small dt(1e-4 in this case) and then sums up the values. This is also called the Simpson's rule if you wish to learn more.
  
  $$ \sum_{n=0}^{10^4} f(t/10^4) \cdot e^{2n \pi i(\frac{t}{10^4})} \cdot 10^{-4} $$

  This is what the code does. It integrates(numerically) for a specific value of n to find $c_n$. This was the part where I just could not comprehend what was being done. I watched a lot of videos to explain what was being done, but ultimately ended up understanding it through hit and trial.

## To make images
  You need a single path svg firstly. Then, change the file name in `generate_coefficients.py`. Then change the value of the variable N. For a value of N, the number of vectors used are 2N-1. This is because my code has the vectors objects split in two lists, one containing the ones that rotate counter-clockwise(coefficients stored in c_pos) and the negative ones(c_neg). Run `generate_coefficients.py`, and it will output two lists. Paste the first one into c_pos and second into c_neg in `fourier.py`.  I recommend changing the first coefficient in both c_pos and c_neg to something small. That way the output is centered about the center of the viewport. Then, change the value of p to whatever you used for N in `generate_coefficients.py`. This again, is sort-of the number of vectors. Run `fourier.py`. You should have the output, now check if the output is actually oriented correctly. For whatever reason, there's an issue with svgpathtools' `point.path(t)` function and it decides to invert vertically the output for certain types of svgs. If it is the case, go to line 18 in `generate_coefficients.py` and replace the `-` with a `+`. You might also have the output too small or too large to fit in the viewport. In that case, change the value of the variable `SCALE`. Increasing this zooms out, decreasing zooms in.
  Tweak these and you should have your output ready. 
  Sample output:

https://github.com/RockSolid1106/FourierTransformations/assets/84492239/bcbbf401-e7ab-487b-b2f1-2aa19fe9dd28

## Don't understand part of the code?
  Start an issue here, or PM me on the linustechtips.com forum. I go by the same username there too.
