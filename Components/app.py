import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from pathlib import Path
from .gaussjordan import gauss_jordan


class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Current Calculator")

        self.create_buttons()

        self.app.mainloop()

    def create_buttons(self):
        l_1 = tk.Label(self.app, text = "Select CSV file")
        l_2 = tk.Label(self.app, text = "Solve system")
        l_3 = tk.Label(self.app, text = "Select file type and save")

        l_list = [l_1, l_2, l_3]
        l_2["state"] = "disabled"
        l_3["state"] = "disabled"

        for i in l_list:
            i["wraplength"] = 80

        b_1 = tk.Button(self.app, text = "Load", command = self.load_file)
        b_2 = tk.Button(self.app, text = "Solve", command = self.solve)
        b_3 = tk.Button(self.app, text = "Save", command = self.save_file)

        b_2["state"] = "disabled"
        b_3["state"] = "disabled"

        b_list = [b_1, b_2, b_3]

        self.r_v = tk.StringVar(self.app, "1")

        r_1 = tk.Radiobutton(self.app, text = "CSV", variable = self.r_v, value = "1")
        r_1.select()
        r_2 = tk.Radiobutton(self.app, text = "JSON", variable = self.r_v, value = "2")

        rb_list = [r_1, r_2]

        self.element_list = [l_list, b_list, rb_list]

        elem = 0
        for i in self.element_list:
            if elem == 2:
                break
            count = 0
            for j in i:
                j.grid(row = elem, column = count)
                j["state"] = "disabled"
                if count == 0:
                    j["state"] = "normal"
                count += 1
            elem += 1

        count = 0
        for i in self.element_list[2]:
            i.grid(row = count, column = 3)
            i["state"] = "disabled"
            count += 1


    def load_file(self):
        solve_button_label = self.element_list[0][1]
        solve_button = self.element_list[1][1]
        save_button_label = self.element_list[0][2]
        save_button = self.element_list[1][2]
        radio_buttons = self.element_list[2]

        save_button_label["state"] = "disabled"
        save_button["state"] = "disabled"

        for i in radio_buttons:
            i["state"] = "disabled"

        file_ = askopenfile(mode = "r", filetypes = [("Comma Separated Values", "*.csv")])

        if file_ is not None:

            solve_button_label["state"] = "normal"
            solve_button["state"] = "normal"


            content = file_.read().split("\n")
            self.content = [i.split(",") for i in content]
            self.matrix, self.sol_matrix = [], []

            self.matrix = matrix_crop(self.content)
            self.sol_matrix = column(self.content)

        else:
            solve_button_label["state"] = "disabled"
            solve_button["state"] = "disabled"
        file_.close()

    def save_file(self):
        if self.r_v.get() == "1":
            filetype = [("Comma Separated Values", "*.csv")]
            file_ = asksaveasfile(filetypes = filetype, defaultextension = filetype)
            file_.write(self.csvify())
            file_.close()
        else:
            filetype = [("JSON", "*.json")]
            file_ = asksaveasfile(filetypes = filetype, defaultextension = filetype)
            file_.write(self.jsonify())
            file_.close()

    def solve(self):        
        solve_button_label = self.element_list[0][1]
        solve_button = self.element_list[1][1]
        save_button_label = self.element_list[0][2]
        save_button = self.element_list[1][2]
        radio_buttons = self.element_list[2]

        solve_button_label["state"] = "disabled"
        solve_button["state"] = "disabled"
        save_button_label["state"] = "normal"
        save_button["state"] = "normal"

        for i in radio_buttons:
            i["state"] = "normal"
        self.sol_matrix, self.matrix = gauss_jordan(self.matrix, self.sol_matrix)

    def jsonify(self):
        headers = self.content[0]
        body = matrix_joiner(self.matrix, self.sol_matrix)
        
        full = "[\n "
        for i in range(len(body)):
            full += "{\n"
            for j in range(len(headers)):
                if j < len(headers)-1:
                    full += "  \"" + headers[j] + "\"" + ": " + str(body[i][j]) + ",\n"
                else:
                    full += "  \"" + headers[j] + "\"" + ": " + str(body[i][j])
            if i < len(body)-1:
                full += "\n },\n "
            else:
                full += "\n }\n"
        full += "]"

        return full

    def csvify(self):
        headers = str(self.content[0]).strip("[]").replace("'", "") + "\n"
        matrix = matrix_joiner(self.matrix, self.sol_matrix)
        body = ""
        for i in matrix:
            body += str(i).strip("[]").replace("'", "") + "\n"
        
        full = headers + body

        return full

def matrix_joiner(mat_a, mat_b):
    count = 0
    for i in mat_a:
        i.append(mat_b[count][0])
        count += 1
    return mat_a

def column(matrix):
    new_matrix = []
    count = 0
    mat_count = 0
    for i in matrix:
        if mat_count > 0:
            new_matrix.append([])
            new_matrix[count].append(i[len(i)-1])
            count += 1
        mat_count +=1
    return new_matrix 

def matrix_crop(matrix):
    new_matrix = []
    count = 0
    for i in matrix:
        if count > 0:
            new_matrix.append(i[:len(i)-1])
        count += 1
    return new_matrix