from tkinter import Label, Button, filedialog
class Window:
    def __init__(self, master):
        self.root = master
        self.root.title("DirSync Application by Stoian Ioan-Catalin")
        self.root.geometry("600x300")
        self.root.grid()
        self.label1 = Label(master, text="Selecteaza primul folder:")
        self.label1.pack()
        self.buttonSelect = Button(master, text="Select Path", command=self.selectPath)
        self.buttonSelect.pack()

    def selectPath(self):
        dirname = filedialog.askdirectory()
        print(dirname)
        return
