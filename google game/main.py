import time
from PIL import ImageGrab, ImageOps
import pyautogui
import numpy as np
from selenium import webdriver

# pip install selenium Pillow pyautogui
# Set up Selenium to open the Dinosaur game in Chrome
def launch_dino_game():
    driver = webdriver.Chrome()  # Make sure you have chromedriver installed and added to PATH
    driver.get("chrome://dino")  # Launch the Dino Game in Chrome
    time.sleep(2)  # Wait for the game to load
    return driver


# Make the dinosaur jump by pressing the space bar
def jump():
    pyautogui.press('space')


# Capture a portion of the screen (the game window) to monitor obstacles
def grab_image(region):
    image = ImageGrab.grab(region)
    gray_image = ImageOps.grayscale(image)  # Convert the image to grayscale for easier processing
    image_array = np.array(gray_image)
    return image_array.sum()


# Main function to automate the Dino game
def play_dino():
    # Define the region of the screen to monitor for obstacles
    # (Adjust the coordinates based on your screen resolution)
    region = (150, 500, 500, 560)

    print("Game starting in 3 seconds...")
    time.sleep(3)  # Wait before starting

    # Play the game continuously
    while True:
        # Check for obstacles by monitoring the grayscale sum of the region
        screen_sum = grab_image(region)

        # If an obstacle is detected (e.g., changes in the screen sum), make the dinosaur jump
        if screen_sum < 20000:  # Adjust the threshold based on obstacle detection sensitivity
            jump()
            time.sleep(0.1)  # Add a slight delay after jumping to avoid multiple jumps


# Start the game automation
if __name__ == "__main__":
    driver = launch_dino_game()  # Launch the game in Chrome
    jump()  # Start the game by making the dino jump once
    play_dino()  # Automate the game
