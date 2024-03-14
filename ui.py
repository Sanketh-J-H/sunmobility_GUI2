import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGEFONT = ("Verdana", 35)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

	# initializing frames to an empty array
        self.frames = {}

	# iterating through a tuple consisting of the different page layouts
        for F in (Page4,):
            frame = F(container, self)
            
            # initializing frame of that object from startpage, page1, page2 respectively with for loop
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page4)
        
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



# fifth window frame BMS Value
class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
	
        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self,0,weight=0)        
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.rowconfigure(self,6,weight=1)
        Grid.rowconfigure(self,7,weight=1)

	# label of BMS Value page
        label = ttk.Label(self, text="BMS Value", font=LARGEFONT)
        label.grid(row=0, column=3, padx=20, pady=30, sticky="nsew")

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20,10), sticky="nsew")
    
        
        # Create a new frame for self.tree and use pack
        tree_frame = tk.Frame(self)
        tree_frame.grid(row=2, column=3, rowspan=3, padx=100, pady=10, sticky="nsew")
        
        B2T_TMax=0
        B2T_Tmin=0
        B2T_ScBatU_H=0
        B2T_ScBatU_L=0
        B2T_Mode=0
        B2T_TMSWorkMode=0
        B2T_BMUWorkMode=0
        B2T_HighVCtrl=0
        B2T_TargetT=0
        B2T_TAvg=0
        B2T_Life=0

        data = [
            {"Function": "Thermal Management 1", "Msg_Name": "B2T_BMS1", "Signal_Name": "Maximum termperature of single battery", "Signal": B2T_TMax},
            {"Function": "", "Msg_Name": "", "Signal_Name": "Minimum temperature of single battery", "Signal": B2T_Tmin},
            {"Function": "", "Msg_Name": "", "Signal_Name": "BMS current voltage high byte", "Signal": B2T_ScBatU_H}, 
            {"Function": "", "Msg_Name": "", "Signal_Name": "BMS current voltage low byte", "Signal": B2T_ScBatU_L}, 
            {"Function": "", "Msg_Name": "", "Signal_Name": "model", "Signal": B2T_Mode},
            {"Function": "", "Msg_Name": "", "Signal_Name": "Control TMS working mode", "Signal": B2T_TMSWorkMode},    
            {"Function": "", "Msg_Name": "", "Signal_Name": "BMS working mode", "Signal": B2T_BMUWorkMode},  
            {"Function": "", "Msg_Name": "", "Signal_Name": "High voltage control command", "Signal": B2T_HighVCtrl},
            {"Function": "", "Msg_Name": "", "Signal_Name": "Set target temperature", "Signal": B2T_TargetT},
            {"Function": "", "Msg_Name": "", "Signal_Name": "Average battery temperature", "Signal": B2T_TAvg},
            {"Function": "", "Msg_Name": "", "Signal_Name": "BMSLife value", "Signal": B2T_Life},
        ]
        
        self.tree = ttk.Treeview(tree_frame, columns=("Function", "Msg_Name", "Signal_Name", "Signal"), show="headings", selectmode="none")
        
        for col in ("Function", "Msg_Name", "Signal_Name", "Signal"):
            self.tree.heading(col, text=col)
            #self.tree.column(col, width=300)
            if col == "Signal_Name":
                self.tree.column(col, width=320)
            else:
                self.tree.column(col, width=180)

        for item in data:
            self.tree.insert("", "end", values=(item["Function"], item["Msg_Name"], item["Signal_Name"], item["Signal"]))

        # Configure the Treeview to expand and fill both directions
        self.tree.pack(fill=tk.BOTH)
            
        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))



app = tkinterApp()
app.mainloop()
