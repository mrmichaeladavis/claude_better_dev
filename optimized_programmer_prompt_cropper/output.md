**Expert**: Software Developer specializing in Python, Image Processing, and Test-Driven Development
**Objective**: Create a pytest test for the PNG cropping function and fix the transparency issue in the original code.
**Assumptions**: 

- The existing code is located in /root/image_cropper/cropper.py
- We need to create a new file /root/image_cropper/cropper_test.py for the tests
- The current implementation incorrectly adds a white background to PNGs
- We have pytest installed in the environment

Let's start by reviewing the existing code:

<CODE_REVIEW>
The current implementation in cropper.py has the following issues:
1. It converts the input image to RGB mode, which removes any transparency.
2. It creates a new RGB image with a white background for the result.
3. It doesn't preserve the alpha channel of the original PNG.

These issues explain why the function is adding a white background to the cropped picture instead of maintaining transparency.
</CODE_REVIEW>

Now, let's create a test file to verify this behavior and then fix the issue.

<PLANNING>
1. Create a pytest file (cropper_test.py) with a test that:
   a. Creates a temporary PNG image with transparency
   b. Runs the crop_resize_png function
   c. Checks if the output image has transparency
2. Run the test to confirm it fails
3. Modify the crop_resize_png function to preserve transparency
4. Run the test again to confirm it passes
</PLANNING>

Let's start by creating the test file:

/root/image_cropper/cropper_test.py
```python
import pytest
from PIL import Image
import os
from cropper import crop_resize_png

@pytest.fixture
def temp_png():
    # Create a temporary PNG with transparency
    img = Image.new('RGBA', (200, 200), (255, 0, 0, 0))
    img.save('temp.png')
    yield 'temp.png'
    os.remove('temp.png')
    if os.path.exists('output.png'):
        os.remove('output.png')

def test_crop_resize_png_transparency(temp_png):
    crop_resize_png(temp_png, 'output.png')
    
    # Open the output image
    output_img = Image.open('output.png')
    
    # Check if the image has an alpha channel
    assert output_img.mode == 'RGBA', "Output image should have an alpha channel"
    
    # Check if any pixel is transparent
    pixels = output_img.getdata()
    assert any(pixel[3] < 255 for pixel in pixels), "Output image should have transparent pixels"
```

Now, let's run this test to confirm it fails:

```
pytest /root/image_cropper/cropper_test.py
```

The test should fail because the current implementation doesn't preserve transparency.

Now, let's fix the `crop_resize_png` function in the original file:

/root/image_cropper/cropper.py
```python
from PIL import Image, ImageDraw

def crop_resize_png(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGBA mode if it's not already
    img = img.convert("RGBA")

    # Resize the image to 100×100
    img = img.resize((100, 100), Image.LANCZOS)

    # Create a new image with an alpha channel
    mask = Image.new("L", (100, 100), 0)

    # Create a draw object
    draw = ImageDraw.Draw(mask)

    # Draw a white circle on the mask
    draw.ellipse((0, 0, 100, 100), fill=255)

    # Create a new transparent image for the result
    result = Image.new("RGBA", (100, 100), (0, 0, 0, 0))

    # Paste the original image onto the result using the mask
    result.paste(img, (0, 0), mask)

    # Save the result as PNG
    result.save(output_path, "PNG")

if __name__ == "__main__":
    crop_resize_png("input_image.png", "output_image.png")
```

The main changes are:
1. Converting the input image to RGBA mode instead of RGB.
2. Creating a transparent RGBA image for the result instead of a white RGB image.

Now, let's run the test again:

```
pytest /root/image_cropper/cropper_test.py
```

The test should now pass, confirming that we've fixed the transparency issue.

To further improve the code, we could add error handling and input validation. Here's an enhanced version of the `crop_resize_png` function:

```python
from PIL import Image, ImageDraw
import os

def crop_resize_png(image_path, output_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Input file not found: {image_path}")

    try:
        # Open the image
        with Image.open(image_path) as img:
            # Convert the image to RGBA mode if it's not already
            img = img.convert("RGBA")

            # Resize the image to 100×100
            img = img.resize((100, 100), Image.LANCZOS)

            # Create a new image with an alpha channel
            mask = Image.new("L", (100, 100), 0)

            # Create a draw object
            draw = ImageDraw.Draw(mask)

            # Draw a white circle on the mask
            draw.ellipse((0, 0, 100, 100), fill=255)

            # Create a new transparent image for the result
            result = Image.new("RGBA", (100, 100), (0, 0, 0, 0))

            # Paste the original image onto the result using the mask
            result.paste(img, (0, 0), mask)

            # Save the result as PNG
            result.save(output_path, "PNG")
    except Exception as e:
        raise RuntimeError(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    crop_resize_png("input_image.png", "output_image.png")
```

This version includes error handling for file not found and general processing errors, which will make the function more robust in real-world usage.