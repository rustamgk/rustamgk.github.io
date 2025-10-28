from PIL import Image
import sys

def image_to_ascii(image_path, width=60):
    # ASCII characters from darkest to lightest
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']
    
    # Open and convert image to grayscale
    img = Image.open(image_path)
    
    # Calculate height to maintain aspect ratio
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)  # 0.55 to account for character height
    
    # Resize image
    img = img.resize((width, height))
    img = img.convert('L')  # Convert to grayscale
    
    # Convert pixels to ASCII
    pixels = img.getdata()
    ascii_str = ''
    
    for i, pixel in enumerate(pixels):
        # Map pixel value (0-255) to ASCII character
        ascii_str += ascii_chars[pixel // 25]
        
        # Add newline at end of each row
        if (i + 1) % width == 0:
            ascii_str += '\n'
    
    return ascii_str

if __name__ == "__main__":
    image_path = r"c:\Users\rusta\My Drive (rustam.gk@gmail.com)\Pictures\Misc\IMG_4144.jpg"
    ascii_art = image_to_ascii(image_path, width=50)
    
    # Save to file
    with open('ascii_avatar.txt', 'w', encoding='utf-8') as f:
        f.write(ascii_art)
    
    print(ascii_art)
    print("\nASCII art saved to ascii_avatar.txt")
