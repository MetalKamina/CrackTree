# CrackTree
CrackTree is a powerful machine learning model trained to detect cracks in images of concrete. Based on the Random Forest Classifier model, this model was tuned over the course of months and specifically trained to minimize false negatives.

## How it works
The model loads in each image as a bunch of numbers representing colors and energy in the pictures. It then runs the images through a bunch of decision trees, figuring out whether the image more closely resembles a piece of cracked concrete or a piece of whole concrete.

## Usage
To use CrackTree, follow these steps:
- Download from the [github repository].
- Gather desired test files into one folder
- Run with the command ```python predict.py "path/to/folder"```
- View results in ```output.csv``` stored in ```"path/to/folder"```

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

   [github repository]: <https://github.com/MetalKamina/CrackTree>