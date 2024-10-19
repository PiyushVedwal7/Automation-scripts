import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import random

# Function to create the handwritten image
def create_handwritten_image():
    try:
        # Get the text from the entry field
        text = text_input.get()
        if not text.strip():
            messagebox.showwarning("Input Error", "Please enter some text.")
            return

        # Create an image with white background
        img = Image.new('RGB', (800, 400), color='white')
        d = ImageDraw.Draw(img)

        # Set font (adjust the font path to where your fonts are located)
        try:
            font = ImageFont.truetype("DancingScript-Regular.ttf", 40)  # Use a handwriting font
        except IOError:
            font = ImageFont.load_default()  # Use default font if not found

        # Draw the text on the image with variability
        x, y = 50, 150
        for letter in text:
            # Randomly change the font size and angle to simulate handwriting
            size_variation = random.randint(-5, 5)  # Change font size slightly
            current_font = ImageFont.truetype("DancingScript-Regular.ttf", 40 + size_variation)
            d.text((x, y), letter, font=current_font, fill=(0, 0, 0))

            # Increment x position for the next letter
            x += current_font.getsize(letter)[0] + random.randint(0, 10)  # Add random spacing

        # Ask user for the location to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img.save(file_path)  # Save image
            messagebox.showinfo("Success", f"Successfully saved handwritten text as {file_path}")
        else:
            messagebox.showwarning("Save Canceled", "The file was not saved.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Handwritten Text Generator")

# Create and place a label and entry for text input
tk.Label(root, text="Enter text to convert to handwritten:").pack(pady=10)
text_input = tk.Entry(root, width=50)
text_input.pack(pady=10)

# Create and place a button to generate the handwritten image
generate_button = tk.Button(root, text="Generate Handwritten Image", command=create_handwritten_image)
generate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
