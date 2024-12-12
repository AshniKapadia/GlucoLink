import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Glucose Alert System Dashboard")
root.geometry("800x600")
root.configure(bg="#f4f4f4")

# Header
header = tk.Frame(root, bg="#007bff", height=60)
header.pack(fill="x")
header_label = tk.Label(
    header,
    text="🚨 Glucose Alert System Dashboard",
    bg="#007bff",
    fg="white",
    font=("Arial", 18, "bold"),
)
header_label.pack(pady=10)

# Section: Caution Zone
caution_frame = tk.Frame(root, bg="#f4f4f4")
caution_frame.pack(pady=20, padx=20, fill="x")

caution_label = tk.Label(
    caution_frame,
    text="⚠️ Caution Zone",
    bg="#f4f4f4",
    fg="black",
    font=("Arial", 16, "bold"),
    anchor="w",
)
caution_label.pack(fill="x", pady=5)

caution_table = ttk.Treeview(caution_frame, columns=("Name", "Glucose Level", "Condition"), show="headings", height=4)
caution_table.heading("Name", text="NAME")
caution_table.heading("Glucose Level", text="GLUCOSE LEVEL")
caution_table.heading("Condition", text="CONDITION")
caution_table.column("Name", anchor="w", width=200)
caution_table.column("Glucose Level", anchor="center", width=150)
caution_table.column("Condition", anchor="w", width=300)

# Add caution zone data
caution_data = [
    ("🟡 John Smith", "68 mg/dL", "BG < 70 mg/dL (≥54 mg/dL)"),
    ("🟡 Alice Green", "192 mg/dL", "BG > 180 mg/dL (≤250 mg/dL)"),
    ("🟡 Michael Brown", "65 mg/dL", "BG < 70 mg/dL (≥54 mg/dL)"),
]
for row in caution_data:
    caution_table.insert("", "end", values=row)

caution_table.pack(fill="x", pady=10)

# Section: Warning Zone
warning_frame = tk.Frame(root, bg="#f4f4f4")
warning_frame.pack(pady=20, padx=20, fill="x")

warning_label = tk.Label(
    warning_frame,
    text="🚨 Warning Zone",
    bg="#f4f4f4",
    fg="black",
    font=("Arial", 16, "bold"),
    anchor="w",
)
warning_label.pack(fill="x", pady=5)

warning_table = ttk.Treeview(
    warning_frame,
    columns=("Name", "Glucose Level", "Condition", "Address", "Emergency Services"),
    show="headings",
    height=4,
)
warning_table.heading("Name", text="NAME")
warning_table.heading("Glucose Level", text="GLUCOSE LEVEL")
warning_table.heading("Condition", text="CONDITION")
warning_table.heading("Address", text="ADDRESS")
warning_table.heading("Emergency Services", text="EMERGENCY SERVICES")
warning_table.column("Name", anchor="w", width=200)
warning_table.column("Glucose Level", anchor="center", width=150)
warning_table.column("Condition", anchor="w", width=200)
warning_table.column("Address", anchor="w", width=200)
warning_table.column("Emergency Services", anchor="center", width=150)

# Add warning zone data
warning_data = [
    ("🔴 Emma Johnson", "44 mg/dL", "BG < 54 mg/dL", "123 Maple St", "Not On Route"),
    ("🔴 David White", "43 mg/dL", "BG < 54 mg/dL", "456 Oak St", "Not On Route"),
    ("🔴 Sophia Clark", "257 mg/dL", "BG > 250 mg/dL", "789 Pine Ave", "Not On Route"),
]
for row in warning_data:
    warning_table.insert("", "end", values=row)

warning_table.pack(fill="x", pady=10)

# Legend
legend_frame = tk.Frame(root, bg="#f4f4f4")
legend_frame.pack(pady=10, padx=20, fill="x")

legend_label = tk.Label(
    legend_frame,
    text="🟡 Caution: Glucose Levels < 70 mg/dL (≥54 mg/dL) or > 180 mg/dL (≤250 mg/dL)\n🔴 Warning: Glucose Levels < 54 mg/dL or > 250 mg/dL",
    bg="#f4f4f4",
    fg="black",
    font=("Arial", 12),
    justify="left",
    anchor="w",
)
legend_label.pack(fill="x")

# Run the application
root.mainloop()