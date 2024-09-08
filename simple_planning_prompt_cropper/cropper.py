import os

from PIL import Image, ImageDraw


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
