import os
from PIL import Image

#You will need pythand and the pillow package to run this

#Get it by entering this into your command prompt "pip install pillow"


# Size of A4 page
A4_WIDTH, A4_HEIGHT = 2480, 3508

# Size of pictures
SCREENSHOT_WIDTH, SCREENSHOT_HEIGHT = 240, 160

# Margins
MARGIN = 10

def arrange_screenshots_on_a4(screenshot_dir, output_dir):
    
    os.makedirs(output_dir, exist_ok=True)

    # Get list of screenshot files and sort them
    screenshots = [os.path.join(screenshot_dir, f) for f in os.listdir(screenshot_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    screenshots.sort()

    # Calculate the number of screenshots that fit 
    max_cols = (A4_WIDTH - 2 * MARGIN) // (SCREENSHOT_WIDTH + MARGIN)
    max_rows = (A4_HEIGHT - 2 * MARGIN) // (SCREENSHOT_HEIGHT + MARGIN)
    screenshots_per_page = max_cols * max_rows

    # Initialize counters
    page_number = 1
    total_screenshots = len(screenshots)

    for start_idx in range(0, total_screenshots, screenshots_per_page):
        # Create a blank A4 image with a white background
        a4_image = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
        x, y = MARGIN, MARGIN
        col, row = 0, 0

        # Pasting onto A4 size image
        for idx in range(start_idx, min(start_idx + screenshots_per_page, total_screenshots)):
            screenshot = Image.open(screenshots[idx])
            a4_image.paste(screenshot, (x, y))

            # Update position
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
                x = MARGIN
                y = MARGIN + row * (SCREENSHOT_HEIGHT + MARGIN)
            else:
                x = MARGIN + col * (SCREENSHOT_WIDTH + MARGIN)

        # Saving final image
        output_path = os.path.join(output_dir, f'output_a4_page_{page_number}.png')
        a4_image.save(output_path)
        print(f"Page {page_number} saved to {output_path}")
        page_number += 1

# User Instructions:
# Replace 'screenshots' with the directory containing your screenshots/pictures
# Replace 'output' with the directory where you want to save the A4 pages
# Remember to enclose the paths in "quotation marks" and put double slahes into path

screenshot_dir = "C:\\Users\\Raoul\\Desktop\\Test screenshots"
output_dir = "C:\\Users\\Raoul\\Desktop\\test output directory"

arrange_screenshots_on_a4(screenshot_dir, output_dir)

print(f"All images were arranged on A4 pages and saved to {output_dir}!")
