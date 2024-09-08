import os

import pytest
from PIL import Image

from original.cropper import crop_resize_png


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

    # Check if any pixel in the image is fully transparent
    pixels = output_img.load()
    has_transparency = any(
        pixels[x, y][3] == 0
        for x in range(output_img.width)
        for y in range(output_img.height)
    )
    assert (
        has_transparency
    ), "Output image should have at least one fully transparent pixel"

    # Check if the image is circular
    center_x, center_y = output_img.width // 2, output_img.height // 2
    radius = output_img.width // 2
    for x in range(output_img.width):
        for y in range(output_img.height):
            distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            if distance > radius:
                assert (
                    pixels[x, y][3] == 0
                ), f"Pixel at ({x}, {y}) should be transparent"
            else:
                assert (
                    pixels[x, y][3] > 0
                ), f"Pixel at ({x}, {y}) should not be transparent"
