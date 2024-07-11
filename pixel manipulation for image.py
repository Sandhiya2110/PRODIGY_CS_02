from PIL import Image
def encrypt_image(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        encrypted_pixels = []
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                encrypted_pixel = tuple([255 - value for value in pixel])
                encrypted_pixels.append(encrypted_pixel)
        
        encrypted_img = Image.new(img.mode, img.size)
        encrypted_img.putdata(encrypted_pixels)
        encrypted_img.save("encrypted_image.png") 
        print("Image encrypted successfully!")
        return encrypted_img
    
    except IOError:
        print(f"Unable to open image: {image_path}")

def decrypt_image(image_path):
    try:
        encrypted_img = Image.open(image_path)
        width, height = encrypted_img.size
        decrypted_pixels = []
        for y in range(height):
            for x in range(width):
                encrypted_pixel = encrypted_img.getpixel((x, y))
                decrypted_pixel = tuple([255 - value for value in encrypted_pixel])
                decrypted_pixels.append(decrypted_pixel)
        
        decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
        decrypted_img.putdata(decrypted_pixels)
        decrypted_img.save("decrypted_image.png")
        
        print("Image decrypted successfully!")
        return decrypted_img
    
    except IOError:
        print(f"Unable to open image: {image_path}")
input_image_path = r"C:\Users\sandh\OneDrive\Pictures\car.jpeg"
# Encrypt image
encrypted_image = encrypt_image(input_image_path)
# Decrypt image
decrypted_image = decrypt_image("encrypted_image.png")
