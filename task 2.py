from PIL import Image # type: ignore

#This is the encrypted session
def encrypt_image(input_image_path, output_image_path, key):
    image = image.open(input_image_path)
    encrypt_image = image.new("RGB", image.size)

    for a in range (image.width):
        for b in range (image.height):
            r,g,b = image.getpixel((a,b))
            #Encrypt pixel using a simple addition
            encrypted_pixel = (r + key) % 256, (g + key) % 256, (b + key) % 256
            encrypt_image.putpixel((a,b), encrypted_pixel)

            encrypt_image.save(output_image_path)
            print(f"image encrypted and saved as (output_image_path)")

           
def decrypt_image(input_image_path, output_image_path, key): 
    image = image.open(input_image_path)
    decrypt_image = image.new("RGB", image.size)

    for a in range (image.width):
        for b in range (image.height):
            r,g,b = image.getpixel((a,b))
            #Decrypt pixel using a simple substraction
            decrypted_pixel = (r - key) % 256, (g - key) % 256, (b - key) % 256
            decrypt_image.putpixel((a,b), decrypted_pixel)

            decrypt_image.save(output_image_path)
            print(f"image decrypted and saved as (output_image_path)")

if_name_=="_main_": # type: ignore
action = input('encrypt')
image_path = input("image path") 
output_path = input("output image path:") 
key = int(input("Encryption key (0-255)"))

if action == 'encrypt':
    encrypt_image(image_path, output_path, key)
elif action == 'decrypt':
    decrypt_image(image_path, output_path, key)
else:
    print("invalid actin, Please Choose 'encrypt' or 'decrypt'.")