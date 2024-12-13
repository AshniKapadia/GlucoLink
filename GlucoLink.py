"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os

# Load data from the Excel file
def load_data():
    file_path = os.path.expanduser("~/Downloads/glucose_data.xlsx")
    
    if not os.path.exists(file_path):
        messagebox.showerror("File Not Found", f"Cannot find the file at {file_path}")
        return [], []
    
    try:
        df = pd.read_excel(file_path)
        
        # Define thresholds for categorization
        warning_low_threshold = 70
        warning_high_threshold = 180
        
        # Filter data for Warning Zone (Glucose Level < 70 or > 180)
        warning_data = df[(df['Glucose Level'] < warning_low_threshold) | (df['Glucose Level'] > warning_high_threshold)]
        warning_data_list = [
            (
                f"\U0001F534 {row['Name']}",
                f"{row['Glucose Level']} mg/dL",
                row['Age'],
                row['Address'],
                row['Emergency Service']
            )
            for _, row in warning_data.iterrows()
        ]
        
        # Filter data for Caution Zone (70 <= Glucose Level <= 180)
        caution_data = df[(df['Glucose Level'] >= warning_low_threshold) & (df['Glucose Level'] <= warning_high_threshold)]
        caution_data_list = [
            (
                f"\U0001F7E1 {row['Name']}",
                f"{row['Glucose Level']} mg/dL",
                row['Duration']
            )
            for _, row in caution_data.iterrows()
        ]
        
        return warning_data_list, caution_data_list

    except Exception as e:
        messagebox.showerror("Error Loading Data", f"An error occurred while loading the data: {e}")
        return [], []

# Function to refresh data in the tables
def refresh_data():
    warning_data, caution_data = load_data()
    
    # Clear existing data in tables
    for i in warning_table.get_children():
        warning_table.delete(i)
    for i in caution_table.get_children():
        caution_table.delete(i)
    
    # Insert new warning data
    for row in warning_data:
        warning_table.insert("", "end", values=row)
    
    # Insert new caution data
    for row in caution_data:
        caution_table.insert("", "end", values=row)
    
    last_updated_label.config(text="Last updated a few seconds ago")
    messagebox.showinfo("Data Refreshed", "The data has been refreshed successfully.")

# Create the main application window
root = tk.Tk()
root.title("Glucose Alert System Dashboard")
root.state("zoomed")
root.configure(bg="#f4f4f4")

# Apply custom styling
style = ttk.Style()
style.theme_use("clam")

# Header
header = tk.Frame(root, bg="#2c3e50", height=70)
header.pack(fill="x")
header_label = tk.Label(
    header,
    text="Glucose Alert System Dashboard",
    bg="#2c3e50",
    fg="white",
    font=("Helvetica", 24, "bold"),
    padx=20
)
header_label.pack(pady=15)

# Main Content Frame
content_frame = tk.Frame(root, bg="#f4f4f4")
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Grid configuration for layout control
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_rowconfigure(1, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

# Styled Frame Function for consistency
def create_section_frame(parent, title, icon):
    frame = tk.Frame(parent, bg="white", bd=2, relief="groove")
    title_label = tk.Label(
        frame,
        text=f"{icon} {title}",
        bg="white",
        fg="#34495e",
        font=("Helvetica", 20, "bold"),
        anchor="w"
    )
    title_label.pack(pady=10, padx=10, fill="x")
    return frame

# Warning Zone
warning_frame = create_section_frame(content_frame, "Warning Zone", "\U0001F6A8")
warning_frame.grid(row=0, column=0, sticky="nsew", pady=10)

warning_table = ttk.Treeview(
    warning_frame,
    columns=("Name", "Glucose Level", "Age", "Address", "Emergency Services"),
    show="headings",
    height=10
)

columns = [
    ("Name", 250),
    ("Glucose Level", 200),
    ("Age", 100),
    ("Address", 400),
    ("Emergency Services", 200),
]

for col, width in columns:
    warning_table.heading(col, text=col.upper())
    anchor = "w" if col == "Name" else "center"
    warning_table.column(col, width=width, anchor=anchor)

warning_table.pack(fill="both", expand=True, padx=10, pady=10)

# Caution Zone
caution_frame = create_section_frame(content_frame, "Caution Zone", "\u26A0\uFE0F")
caution_frame.grid(row=1, column=0, sticky="nsew", pady=10)

caution_table = ttk.Treeview(
    caution_frame,
    columns=("Name", "Glucose Level", "Duration"),
    show="headings",
    height=10
)

caution_columns = [
    ("Name", 300),
    ("Glucose Level", 200),
    ("Duration", 200),
]

for col, width in caution_columns:
    caution_table.heading(col, text=col.upper())
    anchor = "w" if col == "Name" else "center"
    caution_table.column(col, width=width, anchor=anchor)

caution_table.pack(fill="both", expand=True, padx=10, pady=10)

# Refresh Button and Last Updated Label Frame
footer_frame = tk.Frame(root, bg="#f4f4f4")
footer_frame.pack(pady=10)

refresh_button = tk.Button(
    footer_frame,
    text="\U0001F504 Refresh Data",
    bg="#3498db",
    fg="white",
    font=("Helvetica", 18, "bold"),
    padx=20,
    pady=10,
    command=refresh_data
)
refresh_button.pack(side="left", padx=10)

last_updated_label = tk.Label(
    footer_frame,
    text="Last updated 15 seconds ago",
    bg="#f4f4f4",
    fg="#7f8c8d",
    font=("Helvetica", 14)
)
last_updated_label.pack(side="left", padx=10)

# Run the application
root.mainloop()
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os


import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

def show_dashboard():
    # Destroy the splash window
    splash.destroy()

    # Create the main dashboard window
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("800x600")  # Adjust size as needed

    # Add any dashboard content here (optional)
    dashboard_label = tk.Label(dashboard, text="Welcome to GlucoLink!", font=("Arial", 16))
    dashboard_label.pack(pady=50)

    dashboard.mainloop()

# Create a splash screen
splash = tk.Tk()
splash.title("Splash Screen")
splash.geometry("800x600")  # Adjust size as needed

# Load the image
image_path = "/Users/ashnikapadia/Downloads/Glucolinkpic.png"
image = Image.open(image_path)
image = image.resize((800, 600), Image.Resampling.LANCZOS)  # Adjust size to fit the splash window
img = ImageTk.PhotoImage(image)

# Display the image
img_label = Label(splash, image=img)
img_label.pack(fill="both", expand=True)

# Set a timer to close the splash screen and show the dashboard
splash.after(3000, show_dashboard)  # Adjust time (milliseconds) as needed

splash.mainloop()


try:
    # Import Fetch.ai libraries
    from fetchai.ledger.crypto import Entity
    from fetchai.ledger.agent import Agent
    import requests  # Used for web scraping functionality

    class WebScraperAgent(Agent):
        def __init__(self):
            super().__init__(Entity())
            print("Fetch.ai Web Scraper Agent initialized.")

        def scrape_website(self, url):
            """
            Placeholder method for scraping a website.
            This function performs a simple GET request to fetch the HTML content.
            """
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Successfully scraped content from {url}")
                    print(response.text[:100])  
                else:
                    print(f"Failed to scrape {url}, Status Code: {response.status_code}")
            except Exception as e:
                print(f"Error occurred while scraping {url}: {e}")

    if __name__ == "__main__":
        agent = WebScraperAgent()
        print("Web Scraper Agent is idle.")  # Placeholder idle state message

        
except ModuleNotFoundError as e:
    # Skip Fetch.ai-related code if the module is not installed
    print("Fetch.ai module not found. Skipping Fetch.ai functionality.")






# Load data from the Excel file
def load_data():
    file_path = os.path.expanduser("~/Downloads/glucose_data.xlsx")
    
    if not os.path.exists(file_path):
        messagebox.showerror("File Not Found", f"Cannot find the file at {file_path}")
        return [], []
    
    try:
        df = pd.read_excel(file_path)
        
        # Define thresholds for categorization
        warning_low_threshold = 70
        warning_high_threshold = 180
        
        # Filter data for Warning Zone (Glucose Level < 70 or > 180)
        warning_data = df[(df['Glucose Level'] < warning_low_threshold) | (df['Glucose Level'] > warning_high_threshold)]
        warning_data_list = [
            (
                f"\U0001F534 {row['Name']}",
                f"{row['Glucose Level']} mg/dL",
                row['Age'],
                row['Address'],
                row['Emergency Service']
            )
            for _, row in warning_data.iterrows()
        ]
        
        # Filter data for Caution Zone (70 <= Glucose Level <= 180)
        caution_data = df[(df['Glucose Level'] >= warning_low_threshold) & (df['Glucose Level'] <= warning_high_threshold)]
        caution_data_list = [
            (
                f"\U0001F7E1 {row['Name']}",
                f"{row['Glucose Level']} mg/dL",
                row['Duration']
            )
            for _, row in caution_data.iterrows()
        ]
        
        return warning_data_list, caution_data_list

    except Exception as e:
        messagebox.showerror("Error Loading Data", f"An error occurred while loading the data: {e}")
        return [], []

# Function to refresh data in the tables
def refresh_data():
    warning_data, caution_data = load_data()
    
    # Clear existing data in tables
    for i in warning_table.get_children():
        warning_table.delete(i)
    for i in caution_table.get_children():
        caution_table.delete(i)
    
    # Insert initial warning data
    for row in warning_data:
        warning_table.insert("", "end", values=row)
    
    # Insert initial caution data
    for row in caution_data:
        caution_table.insert("", "end", values=row)
    
    # Add tag styles for flashing
    style.configure("Treeview.tag_flash", background="yellow", foreground="black")
    style.configure("Treeview.tag_normal", background="white", foreground="black")
    caution_table.tag_configure("flash", background="yellow", foreground="black")
    caution_table.tag_configure("normal", background="white", foreground="black")

    # Flash and move Ronald Hicks from Caution Zone to Warning Zone
    def flash_and_move():
        for item in caution_table.get_children():
            values = caution_table.item(item, "values")
            if "Ronald Hicks" in values:
                # Flash entry
                def toggle_flash(state, count=4):  # Flash for 4 cycles (2 seconds total)
                    if count <= 0:
                        caution_table.item(item, tags=("normal",))
                        # Move to Warning Zone after flashing
                        caution_table.delete(item)
                        warning_table.insert("", "end", values=values)
                    else:
                        caution_table.item(item, tags=("flash",) if state else ("normal",))
                        root.after(500, lambda: toggle_flash(not state, count - 1))
                toggle_flash(True)
                break

    flash_and_move()

    messagebox.showinfo("Data Refreshed", "The data has been refreshed successfully.")
    
    # Start the timer for hardcoded data after refresh
    root.after(100, add_hardcoded_data)

# Function to hardcode additional data after delays
# Function to hardcode additional data after delays
# Function to hardcode additional data after delays
def add_hardcoded_data():
    root.after(6000, lambda: warning_table.insert("", "end", values=(
        "\U0001F534 William Ballard", "210 mg/dL", "50", "4228 Kemp Glens Suite 484, Port Jenniferton", "On Route"
    )))
    root.after(10000, lambda: caution_table.insert("", "end", values=(
        "\U0001F7E1 Micheal King", "120 mg/dL", "2 hours"
    )))
    root.after(11000, lambda: warning_table.insert("", "end", values=(
        "\U0001F534 Ray Myers", "65 mg/dL", "30", "60127 Riley Alley Suite 098, Hardyshire, WI", "Dispatched"
    )))
    root.after(16000, lambda: caution_table.insert("", "end", values=(
        "\U0001F7E1 Kelly Mores", "150 mg/dL", "1.5 hours"
    )))
    # Flash and move Hardcoded Caution 2
    root.after(8500, flash_and_move_hardcoded_caution_2)

# Flash and move Hardcoded Caution 2 from Caution Zone to Warning Zone
def flash_and_move_hardcoded_caution_2():
    for item in caution_table.get_children():
        values = caution_table.item(item, "values")
        if "Hardcoded Caution 2" in values:
            # Flash entry
            def toggle_flash(state, count=4):  # Flash for 4 cycles (2 seconds total)
                if count <= 0:
                    caution_table.item(item, tags=("normal",))
                    # Move to Warning Zone after flashing
                    caution_table.delete(item)
                    warning_table.insert("", "end", values=values)
                else:
                    caution_table.item(item, tags=("flash",) if state else ("normal",))
                    root.after(500, lambda: toggle_flash(not state, count - 1))
            toggle_flash(True)
            break

# Create the main application window
root = tk.Tk()
root.title("Glucose Alert System Dashboard")
root.state("zoomed")
root.configure(bg="#f4f4f4")

# Apply custom styling
style = ttk.Style()
style.theme_use("clam")

# Header
# Header
header = tk.Frame(root, bg="#2c3e50", height=100)
header.pack(fill="x")

header_label = tk.Label(
    header,
    text="GlucoLink",
    bg="#2c3e50",
    fg="white",
    font=("Helvetica", 36, "bold"),
    padx=20
)
header_label.pack(pady=5)

subheader_label = tk.Label(
    header,
    text="Glucose Alert System Dashboard",
    bg="#2c3e50",
    fg="white",
    font=("Helvetica", 16),
    padx=20
)
subheader_label.pack(pady=5)


# Main Content Frame
content_frame = tk.Frame(root, bg="#f4f4f4")
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Grid configuration for layout control
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_rowconfigure(1, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

# Styled Frame Function for consistency
def create_section_frame(parent, title, icon):
    frame = tk.Frame(parent, bg="white", bd=2, relief="groove")
    title_label = tk.Label(
        frame,
        text=f"{icon} {title}",
        bg="white",
        fg="#34495e",
        font=("Helvetica", 20, "bold"),
        anchor="w"
    )
    title_label.pack(pady=10, padx=10, fill="x")
    return frame

# Warning Zone
warning_frame = create_section_frame(content_frame, "Warning Zone", "\U0001F6A8")
warning_frame.grid(row=0, column=0, sticky="nsew", pady=10)

warning_table = ttk.Treeview(
    warning_frame,
    columns=("Name", "Glucose Level", "Age", "Address", "Emergency Services"),
    show="headings",
    height=10
)

columns = [
    ("Name", 250),
    ("Glucose Level", 200),
    ("Age", 100),
    ("Address", 400),
    ("Emergency Services", 200),
]

for col, width in columns:
    warning_table.heading(col, text=col.upper())
    anchor = "w" if col == "Name" else "center"
    warning_table.column(col, width=width, anchor=anchor)

warning_table.pack(fill="both", expand=True, padx=10, pady=10)

# Caution Zone
caution_frame = create_section_frame(content_frame, "Caution Zone", "\u26A0\uFE0F")
caution_frame.grid(row=1, column=0, sticky="nsew", pady=10)

caution_table = ttk.Treeview(
    caution_frame,
    columns=("Name", "Glucose Level", "Duration"),
    show="headings",
    height=10
)

caution_columns = [
    ("Name", 300),
    ("Glucose Level", 200),
    ("Duration", 200),
]

for col, width in caution_columns:
    caution_table.heading(col, text=col.upper())
    anchor = "w" if col == "Name" else "center"
    caution_table.column(col, width=width, anchor=anchor)

caution_table.pack(fill="both", expand=True, padx=10, pady=10)

# Refresh Button and Last Updated Label Frame
footer_frame = tk.Frame(root, bg="#f4f4f4")
footer_frame.pack(pady=10)

refresh_button = tk.Button(
    footer_frame,
    text="\U0001F504 Refresh Data",
    bg="#3498db",
    fg="black",
    font=("Helvetica", 18, "bold"),
    padx=20,
    pady=10,
    command=refresh_data
)
refresh_button.pack(side="left", padx=10)

last_updated_label = tk.Label(
    footer_frame,
    text="Last updated 2 seconds ago",
    bg="#f4f4f4",
    fg="#7f8c8d",
    font=("Helvetica", 14)
)
last_updated_label.pack(side="left", padx=10)

# Run the application
root.mainloop()
