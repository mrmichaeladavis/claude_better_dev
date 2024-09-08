# /root/image_cropper/cropper_test.py
import os

import pytest
from cropper import crop_resize_png
from PIL import Image


@pytest.fixture
def test_image():
    # Create a test image with transparency
    img = Image.new("RGBA", (200, 200), (255, 0, 0, 0))
    img.save("test_input.png")
    yield "test_input.png"
    os.remove("test_input.png")
    if os.path.exists("test_output.png"):
        os.remove("test_output.png")


def test_crop_resize_png_transparency(test_image):
    crop_resize_png(test_image, "test_output.png")

    # Open the output image
    output_img = Image.open("test_output.png")

    # Check if the image has an alpha channel
    assert output_img.mode == "RGBA", "Output image should have an alpha channel"

    # Check if there are transparent pixels in the corners
    corners = [
        output_img.getpixel((0, 0)),
        output_img.getpixel((0, 99)),
        output_img.getpixel((99, 0)),
        output_img.getpixel((99, 99)),
    ]

    for corner in corners:
        assert corner[3] == 0, f"Corner pixel {corner} should be transparent"
        assert corner[3] == 0, f"Corner pixel {corner} should be transparent"
