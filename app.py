import tkinter as tk

from tkinter import messagebox
import pandas as pd

# Load the dataset
df = pd.read_excel(""C:\Users\Rithesh\Downloads\PG WORKS\Bhogle project\Copy of srinivas_blah(1).xlsx"")

# User Interface 1
def get_crop_info():
    crop_name = crop_entry.get()
    if crop_name in df['Crop Name'].values:
        crop_info = df[df['Crop Name'] == crop_name].iloc[0].to_dict()
        output_text = "\n".join([f"{key}: {value}" for key, value in crop_info.items()])
        output_label.config(text=output_text)
    else:
        messagebox.showerror("Error", f"Crop '{crop_name}' not found in the dataset")

root1 = tk.Tk()
root1.title("Crop Information")

crop_label = tk.Label(root1, text="Enter Crop Name:")
crop_label.pack()

crop_entry = tk.Entry(root1)
crop_entry.pack()

get_info_button = tk.Button(root1, text="Get Crop Info", command=get_crop_info)
get_info_button.pack()

output_label = tk.Label(root1, text="")
output_label.pack()

# User Interface 2
def get_crops_for_growing():
    temperature = float(temperature_entry.get())
    precipitation = float(precipitation_entry.get())
    soil_type = soil_type_entry.get()

    suitable_crops = df[(df['Average Temperature'] <= temperature) &
                        (df['Average Precipitation'] <= precipitation) &
                        (df['Soil Type'] == soil_type)]['Crop Name'].tolist()

    output_text = "\n".join(suitable_crops)
    crops_label.config(text=output_text)

root2 = tk.Tk()
root2.title("Suitable Crops for Growing")

temperature_label = tk.Label(root2, text="Temperature:")
temperature_label.pack()

temperature_entry = tk.Entry(root2)
temperature_entry.pack()

precipitation_label = tk.Label(root2, text="Precipitation:")
precipitation_label.pack()

precipitation_entry = tk.Entry(root2)
precipitation_entry.pack()

soil_type_label = tk.Label(root2, text="Soil Type:")
soil_type_label.pack()

soil_type_entry = tk.Entry(root2)
soil_type_entry.pack()

get_crops_button = tk.Button(root2, text="Get Suitable Crops", command=get_crops_for_growing)
get_crops_button.pack()

crops_label = tk.Label(root2, text="")
crops_label.pack()

root1.mainloop()
root2.mainloop()