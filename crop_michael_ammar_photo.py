from PIL import Image

# Open the original image
img_path = 'assets/Photo with Michael Ammar.jpeg'
img = Image.open(img_path)

# Get image dimensions
width, height = img.size

# Calculate crop box for upper 2/3 and make it square
crop_height = int(height * 2 / 3)
square_size = min(width, crop_height)

# Center crop horizontally, upper 2/3 vertically
left = (width - square_size) // 2
upper = 0
right = left + square_size
lower = upper + square_size

# Crop the image
cropped_img = img.crop((left, upper, right, lower))

# Save the cropped image
cropped_img.save('assets/Photo with Michael Ammar Cropped.jpeg')
print('Cropped image saved as Photo with Michael Ammar Cropped.jpeg')
