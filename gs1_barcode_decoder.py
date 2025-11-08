import tkinter as tk
from tkinter import messagebox
import re
from PIL import Image, ImageTk
import os

def parse_gs1_barcode(barcode):
    # Ignore the predefined prefix ']d2'
    barcode = barcode.replace("]d2", "").strip()
    
    # Define GS1 application identifiers (AIs)
    gs1_patterns = {
        '01': 'GTIN',
        '21': 'Serial Number',
        '17': 'Expiry Date',
        '10': 'Batch Number'
    }
    
    extracted_data = {}
    
    # Custom regex pattern to match GS1 Application Identifiers (AIs)
    pattern = r'(01\d{14})|(21[\w\d]+)|(17\d{6})|(10[\w\d\W]+)'
    matches = re.findall(pattern, barcode)
    
    for match in matches:
        for value in match:
            if value and value.startswith("01"):
                extracted_data['GTIN'] = value[2:]
            elif value and value.startswith("21"):
                extracted_data['Serial Number'] = value[2:]
            elif value and value.startswith("17"):
                expiry_date = value[2:]
                extracted_data['Expiry Date'] = f"{expiry_date[4:]}-{expiry_date[2:4]}-20{expiry_date[:2]}"
            elif value and value.startswith("10"):
                extracted_data['Batch Number'] = value[2:]
    
    return extracted_data

def on_scan():
    barcode = entry.get().strip()
    if barcode:
        extracted_data = parse_gs1_barcode(barcode)
        if extracted_data:
            result_text.set('\n'.join([f"{key}: {value}" for key, value in extracted_data.items()]))
        else:
            result_text.set("No valid GS1 data found.")
        entry.delete(0, tk.END)  # Clear input field for the next scan

def check_for_scan():
    barcode = entry.get().strip()
    if barcode:
        root.after(200, on_scan)  # Slight delay to prevent multiple triggers

def on_keyrelease(event):
    if event.keysym in ["Return", "Tab"]:
        return "break"

# Create GUI
root = tk.Tk()
root.title("GS1 Barcode Scanner")
root.geometry("600x600")

label = tk.Label(root, text="Scan or Enter GS1 Barcode:", font=("Arial", 24))
label.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 24))
entry.pack(pady=5)
entry.focus_set()
entry.bind("<KeyRelease>", on_keyrelease)
entry.bind("<Return>", lambda event: on_scan())  # Ensure scan triggers on Enter

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Arial", 28, "bold"))
result_label.pack(pady=10)

# Load and display the logo
logo_path = os.path.join(os.path.dirname(__file__), "image.png")
try:
    if os.path.exists(logo_path):
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((150, 150), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(root, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.pack(pady=10)
    else:
        raise FileNotFoundError("Logo file not found.")
except Exception as e:
    print("Error loading logo:", e)
    logo_label = tk.Label(root, text="[Logo not found]", font=("Arial", 14, "bold"))
    logo_label.pack(pady=10)

# Footer section with company details
footer_frame = tk.Frame(root)
footer_frame.pack(pady=10, fill="x")

footer_label = tk.Label(footer_frame, text="Developed by Muhammad Faisal", font=("Arial", 14, "bold"))
footer_label.pack()

email_label = tk.Label(footer_frame, text="Email: alfaisaluae34@gmail.com", font=("Arial", 12))
email_label.pack()

address_label = tk.Label(footer_frame, text="Dubai, United Arab Emirates", font=("Arial", 12))
address_label.pack()

# Start checking for scans
root.after(200, check_for_scan)

root.mainloop()
