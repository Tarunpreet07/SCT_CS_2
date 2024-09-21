import cv2
import numpy as np

# Function to encrypt the image
def encrypt_image(image, key):
    # Apply XOR operation to each pixel with the key
    encrypted_image = cv2.bitwise_xor(image, key)
    return encrypted_image

# Function to decrypt the image
def decrypt_image(encrypted_image, key):
    # XOR again with the same key will retrieve the original image
    decrypted_image = cv2.bitwise_xor(encrypted_image, key)
    return decrypted_image

# Load the image
image_path = "your_image_path"
image = cv2.imread(image_path)

# Check if the image was loaded
if image is None:
    print("Image not found!")
    exit()

# Define a key for encryption (random matrix of the same shape as the image)
key = np.random.randint(0, 256, size=image.shape, dtype='uint8')

# Encrypt the image
encrypted_image = encrypt_image(image, key)

# Save the encrypted image
cv2.imwrite("encrypted_image.jpg", encrypted_image)

# Decrypt the image (to verify)
decrypted_image = decrypt_image(encrypted_image, key)

# Save the decrypted image
cv2.imwrite("decrypted_image.jpg", decrypted_image)

# Show the images
cv2.imshow("Original Image", image)
cv2.imshow("Encrypted Image", encrypted_image)
cv2.imshow("Decrypted Image", decrypted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
