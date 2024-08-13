from PIL import Image
import os

def arrange_screenshots_on_a4(screenshot_dir, output_dir, dpi=100, margin_px=20):
    # A4 dimensions in pixels at the specified DPI
    a4_width_px = int(8.27 * dpi)  # A4 width: 8.27 inches
    a4_height_px = int(11.69 * dpi)  # A4 height: 11.69 inches
    
    # Screenshot dimensions in pixels
    screenshot_width = int(2.409 * dpi)
    screenshot_height = int(1.606 * dpi)
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize variables
    images = [f for f in os.listdir(screenshot_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()
    page_number = 1
    x_offset, y_offset = 0, 0
    a4_image = Image.new('RGB', (a4_width_px, a4_height_px), 'white')
    
    for img in images:
        screenshot_path = os.path.join(screenshot_dir, img)
        screenshot = Image.open(screenshot_path)
        
        # Resize the screenshot to the desired print size
        screenshot = screenshot.resize((screenshot_width, screenshot_height), Image.Resampling.LANCZOS)
        
        # Check if the image fits horizontally, else move to the next row
        if x_offset + screenshot_width > a4_width_px:
            x_offset = 0
            y_offset += screenshot_height + margin_px
        
        # Check if the image fits vertically, else save the page and start a new one
        if y_offset + screenshot_height > a4_height_px:
            a4_image.save(os.path.join(output_dir, f'page_{page_number}.png'))
            page_number += 1
            a4_image = Image.new('RGB', (a4_width_px, a4_height_px), 'white')
            x_offset, y_offset = 0, 0
        
        # Paste the screenshot onto the A4 image
        a4_image.paste(screenshot, (x_offset, y_offset))
        x_offset += screenshot_width + margin_px
    
    # Save the last page
    a4_image.save(os.path.join(output_dir, f'page_{page_number}.png'))

# Example usage:
screenshot_dir = r"C:\Users\Raoul\Desktop\Test screenshots"
output_dir = r"C:\Users\Raoul\Desktop\test output directory"

arrange_screenshots_on_a4(screenshot_dir, output_dir, dpi=100)
print(f"All screenshots arranged on A4 pages and saved to {output_dir}")
