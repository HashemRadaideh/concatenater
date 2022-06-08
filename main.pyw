from tkinter import *
from tkinter import filedialog, messagebox
import os
from concatenate import Concatenate

window = Tk()

w = 350
h = 650
window.geometry(f"{w}x{h}")
window.resizable(True, True)
window.title("File concatenate")
window.config(background="#282c34")

files = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp = f.read()
        temp = temp.split(',')
        files = [x for x in temp if x.strip()]


def remove():
    for index in reversed(fileList.curselection()):
        fileList.delete(index)
        files.pop(index)
    fileList.config(height=fileList.size())


def select():
    fileList.delete(0, END)
    filename = filedialog.askopenfilename(
        initialdir="\\", title="Select File", filetypes=(
            ("Text Files", "*.txt"), ("All Files", "*.*")))
    if filename != '':
        files.append(filename)
    for file in files:
        fileList.insert(files.index(file) + 1, file)
    fileList.config(height=fileList.size())


def error(msg):
    messagebox.showwarning(title='Warning', message=f'{msg}')


def merge():
    for widget in output.winfo_children():
        widget.destroy()
    try:
        clean()
        output.config(state=NORMAL)
        concat = Concatenate(files)
        output.insert('1.0', concat)
        output.config(state=DISABLED)
    except ValueError:
        error("Please select files first")
    except:
        error("Something Went wrong")


def clean():
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.config(state=DISABLED)


def save():
    concat = Concatenate(files)
    concat.create_file()


fileList = Listbox(window, bg='white', width=20, selectmode=MULTIPLE)
fileList.pack(side=TOP, fill=BOTH, expand=False, padx=10, pady=10)

output = Text(window, bg='white', height=20, width=20,)
output.pack(side=TOP, fill=BOTH, expand=False, padx=10, pady=10)

opener = Button(window, text="Locate", fg="white",
                bg="#223344", command=select, pady=10)
opener.pack(side=TOP, fill=BOTH, expand=False, padx=10)

remover = Button(window, text="Remove", fg="white",
                 bg="#223344", command=remove, pady=10)
remover.pack(side=TOP, fill=BOTH, expand=False, padx=10)

merger = Button(window, text="Merge", fg="white",
                bg="#223344", command=merge, pady=10)
merger.pack(side=TOP, fill=BOTH, expand=False, padx=10)

clear = Button(window, text="Clear", fg="white",
               bg="#223344", command=clean, pady=10)
clear.pack(side=TOP, fill=BOTH, expand=False, padx=10)

clear = Button(window, text="Save", fg="white",
               bg="#223344", command=save, pady=10)
clear.pack(side=TOP, fill=BOTH, expand=False, padx=10)

for file in files:
    fileList.insert(files.index(file) + 1, file)

fileList.config(height=fileList.size())

window.mainloop()

with open('save.txt', 'w') as f:
    for file in files:
        f.write(file + ',')

# C:/Users/hashe/Studies/Python/App/files/test1.txt,C:/Users/hashe/Studies/Python/App/files/test2.txt,C:/Users/hashe/Studies/Python/App/files/test3.txt,C:/Users/hashe/Studies/Python/App/files/test4.txt,C:/Users/hashe/Studies/Python/App/files/test5.txt,
