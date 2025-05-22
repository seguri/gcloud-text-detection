def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

    return texts


def main():
    import os
    import sys
    from pathlib import Path

    # Set Google credentials
    credentials_path = Path(__file__).parent / "credentials.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(credentials_path)

    image_path = Path(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")

    # Check if the image file exists
    if not image_path.exists():
        print(f"{image_path}: no such file")
        sys.exit(1)

    print(f"Processing image: {image_path}")
    try:
        detect_text(image_path)
    except Exception as e:
        print(f"Error during text detection: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
