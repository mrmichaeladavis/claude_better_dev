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
