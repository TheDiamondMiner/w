# Import necessary libraries
import time
import subprocess
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None  # on the PiOLED this pin isn't used
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Initialize the SSD1306 OLED display
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library
disp.begin()

# Clear display
disp.clear()
disp.display()

# Constants for OLED display
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
CHAR_WIDTH = 8  # Each character is approximately 8 pixels wide in the default font
MAX_CHARS_PER_LINE = DISPLAY_WIDTH // CHAR_WIDTH

# Function to print text on the OLED display
def print_text_on_display(display, text):
    display.clear()
    display.display()

    words = text.split()

    current_line = 0
    current_char_count = 0

    for word in words:
        word_length = len(word)

        if current_char_count + word_length + 1 <= MAX_CHARS_PER_LINE:
            display.text((current_char_count * CHAR_WIDTH, current_line * 8), word, fill=255)
            current_char_count += word_length + 1
        else:
            current_line += 1
            current_char_count = 0

            if current_line >= DISPLAY_HEIGHT // 8:
                display.clear()
                display.display()
                current_line = 0
                print_text_on_display(display, ' '.join(words[words.index(word):]))
                break

            display.text((current_char_count * CHAR_WIDTH, current_line * 8), word, fill=255)
            current_char_count += word_length + 1

        display.display()

# Example stats file to get text input
stats_text = """
this is a big paragraph to test the oled logic, i hope this works as if it does not then i am done for. Thank you everyone that helped in making this project a success and i reach natioanls. Steve kobs is such a nice guy.
"""

# Call the function with the stats text
print_text_on_display(disp, stats_text)