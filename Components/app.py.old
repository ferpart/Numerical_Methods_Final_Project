from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import sys
from .gaussjordan import gauss_jordan

class App:
    def __init__(self):
        self.voltages = []
        self.resistances = []
        self.app = tk.Tk()
        self.app.title("Current Calculator")

        background = tk.PhotoImage(file = image_selector("Bottom.png"))
        foreground = tk.PhotoImage(file = image_selector("Resistance.png"))
        self.final = tk.PhotoImage(file = image_selector("Result.png"))
        self.width = background.width()
        self.height = background.height()

        frame = tk.Frame(self.app)
        frame.pack()

        self.canvas = tk.Canvas(frame, bg="white", width=self.width, height=self.height+30)
        self.canvas.pack()
        
        self.canvas.create_image(self.width/2, self.height/2, image = background, tags = "background")
        self.canvas.create_image(self.width/2, self.height/2, image = foreground, tags="foreground")

        resistance_list, voltage_list = self.entries()
        v_submit_butt = tk.Button(text = "Submit Values")
        v_submit_butt["command"] = lambda binst=v_submit_butt: self.get_values(resistance_list, voltage_list, binst)

        self.canvas.create_window(self.width/2, 255, window=v_submit_butt)
        self.app.mainloop()

    def get_values(self, resistance_list, voltage_list, binst):
        self.resistances = get_elem_values(resistance_list)
        self.voltages = get_elem_values(voltage_list)
        binst.destroy()
        self.canvas.delete("foreground")
        self.final_disp(self.set_matrix(self.resistances, self.voltages))

    def final_disp(self, results):
        self.canvas.create_image(self.width/2, self.height/2, image = self.final)

        voltage = int(self.voltages[0])
        new_voltages = []
        for i in range(4):
            if (i == 0):
                voltage = round(voltage - (results[0]*int(self.resistances[i])), 3)
            else:
                voltage = round(voltage - (results[1]*int(self.resistances[i])), 3)
            new_voltages.append(voltage)

        # resulting voltages
        self.canvas.create_text(355, 28, text=new_voltages[0], font="Times 15", fill="black")
        self.canvas.create_text(160, 28, text=new_voltages[1], font="Times 15", fill="black")
        self.canvas.create_text(160, 215, text=new_voltages[2], font="Times 15", fill="black")
        self.canvas.create_text(355, 215, text=new_voltages[3], font="Times 15", fill="black")
        self.canvas.create_text(600, 43, text=self.voltages[0], font="Times 15", fill="black")
        self.canvas.create_text(600, 195, text=self.voltages[1], font="Times 15", fill="black")
        
        # resulting currents
        self.canvas.create_text(450, 125, text=results[0], font="Times 15", fill="black")
        self.canvas.create_text(250, 125, text=results[1], font="Times 15", fill="black")


    def entries(self):

        #Resistance entry box creation
        res_1 = tk.Entry(self.app, width=5)
        res_2 = tk.Entry(self.app, width=5)
        res_3 = tk.Entry(self.app, width=5)
        res_4 = tk.Entry(self.app, width=5)
        res_5 = tk.Entry(self.app, width=5)
        res_6 = tk.Entry(self.app, width=5)

        resistance_list = [res_1, res_2, res_3, res_4, res_5, res_6]

        #Voltage entry box creation
        volt_1 = tk.Entry(self.app, width=5)
        volt_2 = tk.Entry(self.app, width=5)

        voltage_list = [volt_1, volt_2]

        #Adding Resistance boxes to canvas
        self.canvas.create_window(453, 16, window=res_1)
        self.canvas.create_window(250, 16, window=res_2)  
        self.canvas.create_window(96, 120, window=res_3)
        self.canvas.create_window(250, 222, window=res_4)
        self.canvas.create_window(448, 222, window=res_5)
        self.canvas.create_window(410, 120, window=res_6)

        #Adding voltage boxes to canvas
        self.canvas.create_window(610, 45, window=volt_1)
        self.canvas.create_window(610, 190, window=volt_2)

        return (resistance_list, voltage_list)

    def int_converter(self, list):
        temp_list = []
        for i in list:
            if (i.isdigit()):
                temp_list.append(int(i))
            else:
                messagebox.showerror("Error", "Element \"%s\" not a digit" %(i))
                sys.exit()
                break
        return temp_list           

    def set_matrix(self, r, v):

        r = self.int_converter(r)
        v = self.int_converter(v)

        matrix = [
                    #  i12   i52   i32   i65   i54   i43
                    [    1,    1,    1,    0,    0,    0],    #i12
                    [    0,   -1,    0,    1,   -1,    0],    #i52
                    [    0,    0,   -1,    0,    0,    1],    #i32
                    [    0,    0,    0,    0,    1,   -1],    #i65 
                    [    0, r[5],-r[1],    0,-r[3],-r[2]],    #i54
                    [ r[0],-r[5],    0,-r[4],    0,    0]     #i43
        ]
        sol_matrix = [
                    [0],
                    [0], 
                    [0], 
                    [0],
                    [v[1]],
                    [v[0]]
        ]
        
        return gauss_jordan(matrix, sol_matrix)

def get_elem_values(list):
    values = []
    for i in list:
        values.append(i.get()) 
        i.destroy()
    return values   


def image_selector(image_name):
    image_folder = Path("Backgrounds")
    return (image_folder/image_name)