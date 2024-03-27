# imports
import pandas as pd
import customtkinter as ctk
from customtkinter import filedialog
from tkinter import PhotoImage, messagebox


# process_data function
def process_data():
    columns = [
        "Date",
        "Time",
        "Serial_Number",
        "Employee_Number",
        "Employee_Code",
        "Temperature",
    ]
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return  # Cancelled file selection

    df = pd.read_fwf(file_path, header=None, names=columns)

    # Perform the data processing
    df["Date"] = df["Date"].str.replace("-", "")
    df["Time"] = df["Time"].str.replace(":", "")
    df["Time"] = df["Time"].str[:4]
    df["Temperature"] = df["Temperature"].str.removesuffix("N")
    df = df.reindex(
        columns=[
            "Date",
            "Time",
            "Employee_Number",
            "Temperature",
            "Serial_Number",
            "Employee_Code",
        ]
    )

    # Save the reformatted data to a new file
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")]
    )
    if not save_path:
        return  # Cancelled file selection
    df.to_csv(save_path, index=False, header=None, sep="\t")

    # Show completion message using standard messagebox
    messagebox.showinfo("完成", "資料處理成功完成！")


# Set up the GUI
root = ctk.CTk()
root.geometry("600x600")
root.title("VAAS 資料轉換應用程式V1.0")

# Add a banner with three steps
banner_label = ctk.CTkLabel(root, text="VAAS 資料轉換應用程式", font=("Song", 32))
banner_label.pack(pady=12, padx=10)

step1_label = ctk.CTkLabel(
    root, text="步驟1：點選「轉換檔案」選擇欲轉換的VAAS手動抛轉文字檔。", font=("Song", 22)
)
step1_label.pack(pady=12, padx=10)

step2_label = ctk.CTkLabel(root, text="步驟2：輸入欲存的路徑及新檔名、另存轉換後的文字檔。", font=("Song", 22))
step2_label.pack(pady=12, padx=10)

step3_label = ctk.CTkLabel(root, text="步驟 3：資料轉換完成。", font=("Song", 22))
step3_label.pack(pady=12, padx=10)

# Add a logo
# logo_path = ".\logo.png"  # Change this to the path of your logo
# logo_img = PhotoImage(file=logo_path)
# logo_label = ctk.CTkLabel(root, image=logo_img)
# logo_label.image = logo_img  # To prevent garbage collection
# logo_label.pack(pady=12)

# Create a button to trigger the data processing
process_button = ctk.CTkButton(
    root, text="轉換檔案", font=("Song", 22), command=process_data
)
process_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
