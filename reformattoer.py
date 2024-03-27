import re
import tkinter as tk
from tkinter import filedialog


def reformat_text(original_text):
    match = re.match(
        r"([A-Za-z0-9]+(-[A-Za-z0-9]+)+) ([A-Za-z0-9]+(:[A-Za-z0-9]+)+)  [0-9]+ +[A-Za-z0-9]+ +[A-Za-z0-9]+ [0-9]*\.[0-9]+N",
        original_text,
    )
    if match:
        date_time = match.group(1).replace("-", "").replace(":", "")
        number = match.group(2)
        code = match.group(3)
        coordinate = match.group(5).removesuffix("N")
        other_number = match.group(4)

        reformatted_text = f"{date_time} {code}    {coordinate} {number} {other_number}"

        return reformatted_text
    else:
        return "Invalid input format"


def process_file(input_path, output_path):
    with open(input_path, "r") as input_file, open(output_path, "w") as output_file:
        for line in input_file:
            formatted_line = reformat_text(line.strip())
            output_file.write(formatted_line + "\n")


def choose_file():
    input_path = filedialog.askopenfilename(
        title="Select Input File", filetypes=[("Text files", "*.txt")]
    )
    if input_path:
        output_path = filedialog.asksaveasfilename(
            title="Save Output File",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
        )
        if output_path:
            process_file(input_path, output_path)
            status_label.config(text="File successfully reformatted and saved!")


# GUI setup
root = tk.Tk()
root.title("Text Reformatter")

# Create and place the Choose File button
choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
choose_file_button.pack(pady=20)

# Status label to display messages
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
