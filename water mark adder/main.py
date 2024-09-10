import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont


# Function to upload the image
def upload_image():
    global img
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        img = Image.open(file_path)
        label_status.config(text="Image Uploaded Successfully")
        button_watermark.config(state="normal")
        return img


# Function to add the watermark to the image
def add_watermark():
    watermark_text = entry_watermark.get()
    if not watermark_text:
        messagebox.showerror("Error", "Please enter the watermark text!")
        return

    # Add watermark to the image
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Default font, you can use custom fonts if you have
    textwidth, textheight = draw.textsize(watermark_text, font)

    # Position for the watermark
    width, height = img.size
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # Add text to the image
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255))

    # Save the watermarked image
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", "Watermark added and image saved successfully!")
    else:
        messagebox.showwarning("Warning", "Image not saved!")


# Create the main window
root = tk.Tk()
root.title("Watermark App")
root.geometry("400x300")

# Instructions and input
label_instruction = tk.Label(root, text="Upload an image and add a watermark:", font=("Helvetica", 14))
label_instruction.pack(pady=10)

# Button to upload image
button_upload = tk.Button(root, text="Upload Image", command=upload_image)
button_upload.pack(pady=10)

# Status label for image upload
label_status = tk.Label(root, text="")
label_status.pack(pady=5)

# Entry for watermark text
entry_watermark = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_watermark.pack(pady=10)
entry_watermark.insert(0, "Enter Watermark Text")

# Button to add watermark
button_watermark = tk.Button(root, text="Add Watermark", command=add_watermark, state="disabled")
button_watermark.pack(pady=20)

# Run the application
root.mainloop()
