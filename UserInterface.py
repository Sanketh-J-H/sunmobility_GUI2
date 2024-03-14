import tkinter as tk
from tkinter import ttk, Grid
import os
import time
import socket
import threading

formatted_data = {
    "B2T_TMax": 0,
    "B2T_Tmin": 0,
    "B2T_ScBatU_H": 0,
    "B2T_ScBatU_L": 0,
    "B2T_Mode": 0,
    "B2T_TMSWorkMode": 0,
    "B2T_BMUWorkMode": 0,
    "B2T_HighVCtrl": 0,
    "B2T_TargetT": 0,
    "B2T_TAvg": 0,
    "B2T_Life": 0
}

try:
    # Get the current directory
    current_directory = os.getcwd()
    # Construct the full path to the file
    file_path = os.path.join(current_directory, "receiveData_for_GUI.py")
    
    # Open and execute the file
    with open(file_path, 'r') as file:
        exec(file.read())
except Exception as e:
    print(f"Error running file: {e}")


def generate_numbers():   
    while True:
        file_path = "CANT_Test.log"
        
        with open(file_path, "r") as file:
            file_content = file.read().strip()
            try:
                data_dict = eval(file_content)
            except Exception as e:
                print(f"Error parsing file content: {e}")
                continue
            
            # Get the IDs of all children items
            children_ids = root.tree.get_children()
            for child_id in children_ids:
                item_values = root.tree.item(child_id, "values")
                # Clear the "Signal_Name" and "Signal" columns while preserving "Function" and "Msg_Name"
                item_values = (item_values[0], item_values[1], "", "")
                root.tree.item(child_id, values=item_values)
            
            # Clear existing items in the tree
            root.tree.delete(*root.tree.get_children())
            
            # Insert new items into the tree
            for key, value in data_dict.items():
                root.tree.insert("", "end", values=("", "", key, value))
        
        time.sleep(0.1)
        root.update()


root = tk.Tk()
root.title("SunMobility")

# root.attributes('-fullscreen',True)
# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window geometry to fill the screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

tree_frame = tk.Frame(root)
tree_frame.grid(row=2, column=3, rowspan=3, padx=100, pady=10, sticky="nsew")

columns = ("Function", "Msg_Name", "Signal_Name", "Signal")
root.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="none")

for col in columns:
    root.tree.heading(col, text=col)
    if col == "Signal_Name":
        root.tree.column(col, width=320)
    else:
        root.tree.column(col, width=180)

# Insert data into the tree and keep references to the items
data = [
        {"Function": "Thermal Management 1", "Msg_Name": "B2T_BMS1", "Signal_Name": "Maximum termperature of single battery", "Signal": formatted_data["B2T_TMax"]},
        {"Function": "", "Msg_Name": "", "Signal_Name": "Minimum temperature of single battery", "Signal": formatted_data["B2T_Tmin"]},
        {"Function": "", "Msg_Name": "", "Signal_Name": "BMS current voltage high byte", "Signal": formatted_data["B2T_ScBatU_H"]}, 
        {"Function": "", "Msg_Name": "", "Signal_Name": "BMS current voltage low byte", "Signal": formatted_data["B2T_ScBatU_L"]}, 
        {"Function": "", "Msg_Name": "", "Signal_Name": "model", "Signal": formatted_data["B2T_Mode"]},
        {"Function": "", "Msg_Name": "", "Signal_Name": "Control TMS working mode", "Signal": formatted_data["B2T_TMSWorkMode"]},    
        {"Function": "", "Msg_Name": "", "Signal_Name": "BMS working mode", "Signal": formatted_data["B2T_BMUWorkMode"]},  
        {"Function": "", "Msg_Name": "", "Signal_Name": "High voltage control command", "Signal": formatted_data["B2T_HighVCtrl"]},
        {"Function": "", "Msg_Name": "", "Signal_Name": "Set target temperature", "Signal": formatted_data["B2T_TargetT"]},
        {"Function": "", "Msg_Name": "", "Signal_Name": "Average battery temperature", "Signal": formatted_data["B2T_TAvg"]},
        {"Function": "", "Msg_Name": "", "Signal_Name": "BMSLife value", "Signal": formatted_data["B2T_Life"]},
    ]

tree_items = []  # List to keep references to tree items

for item in data:
    tree_item = root.tree.insert("", "end", values=(item["Function"], item["Msg_Name"], item["Signal_Name"], item["Signal"]))
    tree_items.append(tree_item)

root.tree.pack()

Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=0)        
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
Grid.rowconfigure(root,3,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.rowconfigure(root,5,weight=1)
Grid.rowconfigure(root,6,weight=1)
Grid.rowconfigure(root,7,weight=1)

# HOME
button0 = tk.Button(root, text="HOME", command=generate_numbers)
button0.grid(row=0, column=1, padx=10, pady=(20,10), sticky="nsew")

button1 = tk.Button(root, text="BMS RLY Command", command=generate_numbers)
button1.grid(row=1, column=1, padx=10, pady=(20,10), sticky="nsew")

button2 = tk.Button(root, text="BMS Status", command=generate_numbers)
button2.grid(row=2, column=1, padx=10, pady=(20,10), sticky="nsew")

button3 = tk.Button(root, text="VCU Command", command=generate_numbers)
button3.grid(row=3, column=1, padx=10, pady=(20,10), sticky="nsew")

button4 = tk.Button(root, text="BMS Value", command=generate_numbers)
button4.grid(row=4, column=1, padx=10, pady=(20,10), sticky="nsew")

button5 = tk.Button(root, text="BMS Temp and Voltage", command=generate_numbers)
button5.grid(row=5, column=1, padx=10, pady=(20,10), sticky="nsew")

button6 = tk.Button(root, text="BMS Alarms", command=generate_numbers)
button6.grid(row=6, column=1, padx=10, pady=(20,10), sticky="nsew")

button7 = tk.Button(root, text="GB/T Cmd and Status", command=generate_numbers)
button7.grid(row=7, column=1, padx=10, pady=(20,10), sticky="nsew")

root.mainloop()
