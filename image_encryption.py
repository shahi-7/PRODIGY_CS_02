from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, shift_value, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Load the pixel data
    
    # Encrypt the image by shifting the pixel values
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Apply shift to each RGB value
            pixels[i, j] = ((r + shift_value) % 256, (g + shift_value) % 256, (b + shift_value) % 256)
    
    # Save the encrypted image
    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image
def decrypt_image(image_path, shift_value, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Load the pixel data
    
    # Decrypt the image by reversing the pixel shift
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Reverse the shift on each RGB value
            pixels[i, j] = ((r - shift_value) % 256, (g - shift_value) % 256, (b - shift_value) % 256)
    
    # Save the decrypted image
    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function to run the encryption/decryption
def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    image_path = input("Enter the path to the image: ")
    shift_value = int(input("Enter the shift value (1-255): "))
    output_path = input("Enter the path to save the output image: ")

    if choice == 'e':
        encrypt_image(image_path, shift_value, output_path)
    elif choice == 'd':
        decrypt_image(image_path, shift_value, output_path)
    else:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
