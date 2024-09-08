**Expert**: Software Engineer specializing in Python and Image Processing
**Objective**: Create a pytest test for the PNG cropping function and fix the transparency issue
**Assumptions**: The code is located in /root/image_cropper/cropper.py, and we need to create a test file at /root/image_cropper/cropper_test.py

Let's start by creating a pytest test to check if the output PNG has a transparent background. We'll write this test in the file /root/image_cropper/cropper_test.py:

```python
import pytest
from PIL import Image
import os
from cropper import crop_resize_png

@pytest.fixture
def test_image():
    # Create a test image with transparency
    img = Image.new('RGBA', (200, 200), (255, 0, 0, 0))
    img.save('test_input.png')
    yield 'test_input.png'
    os.remove('test_input.png')
    if os.path.exists('test_output.png'):
        os.remove('test_output.png')

def test_crop_resize_png_transparency(test_image):
    crop_resize_png(test_image, 'test_output.png')
    
    # Open the output image
    output_img = Image.open('test_output.png')
    
    # Check if the image has an alpha channel
    assert output_img.mode == 'RGBA', "Output image should have an alpha channel"
    
    # Check if any pixel in the image is fully transparent
    pixels = output_img.load()
    has_transparency = any(pixels[x, y][3] == 0 for x in range(output_img.width) for y in range(output_img.height))
    assert has_transparency, "Output image should have at least one fully transparent pixel"

    # Check if the image is circular
    center_x, center_y = output_img.width // 2, output_img.height // 2
    radius = output_img.width // 2
    for x in range(output_img.width):
        for y in range(output_img.height):
            distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            if distance > radius:
                assert pixels[x, y][3] == 0, f"Pixel at ({x}, {y}) should be transparent"
            else:
                assert pixels[x, y][3] > 0, f"Pixel at ({x}, {y}) should not be transparent"
```

This test creates a temporary test image with transparency, runs the `crop_resize_png` function, and then checks if the output image has the expected properties:
1. It should have an alpha channel (RGBA mode).
2. It should have at least one fully transparent pixel.
3. It should be circular, with transparent pixels outside the circle and non-transparent pixels inside.

Now, let's run this test. It should fail because the current implementation doesn't preserve transparency.

To fix the issue, we need to modify the `crop_resize_png` function in /root/image_cropper/cropper.py:

```python
from PIL import Image, ImageDraw

def crop_resize_png(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGBA mode to ensure it has an alpha channel
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
1. Convert the input image to RGBA mode instead of RGB.
2. Create the result image with an RGBA mode and a fully transparent background.

These changes should fix the transparency issue. Now, when you run the pytest, it should pass. The output PNG will have a transparent background outside the circular crop area.

To run the test, use the following command in the terminal:

```
pytest /root/image_cropper/cropper_test.py
```

This should now pass all the assertions in the test, confirming that the `crop_resize_png` function correctly handles transparency in PNG images.