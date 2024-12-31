from PIL import Image

def encrypt_image(image_path, shift, output_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                
                if len(pixel) == 3:  # RGB Image
                    r, g, b = pixel
                    pixels[x, y] = ((r + shift) % 256, (g + shift) % 256, (b + shift) % 256)
                elif len(pixel) == 4:  # RGBA Image
                    r, g, b, a = pixel
                    pixels[x, y] = ((r + shift) % 256, (g + shift) % 256, (b + shift) % 256, a)

        image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(image_path, shift, output_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                
                if len(pixel) == 3:  # RGB Image
                    r, g, b = pixel
                    pixels[x, y] = ((r - shift) % 256, (g - shift) % 256, (b - shift) % 256)
                elif len(pixel) == 4:  # RGBA Image
                    r, g, b, a = pixel
                    pixels[x, y] = ((r - shift) % 256, (g - shift) % 256, (b - shift) % 256, a)

        image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption Tool 🖼️")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the path to the image: ").strip()
    shift = int(input("Enter the shift value (1-255): "))
    output_path = input("Enter the output image path: ").strip()

    if mode == "encrypt":
        encrypt_image(image_path, shift, output_path)
    elif mode == "decrypt":
        decrypt_image(image_path, shift, output_path)
    else:
        print("Invalid mode! Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
