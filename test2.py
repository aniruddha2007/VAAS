import pandas as pd
import numpy as np

columns = [
    "Date",
    "Time",
    "Serial_Number",
    "Employee_Number",
    "Employee_Code",
    "Temperature",
]
df = pd.read_fwf("test.txt", header=None, names=columns)
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
df.to_csv("test_new.txt", index=False, header=None, sep="\t")
