from tkinter import Label, Button, filedialog, messagebox
from lib import sync
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
        self.label2 = Label(master, text="Selecteaza al doilea folder:")
        self.label2.pack()
        self.buttonSelect = Button(master, text="Select Path", command=self.selectPath2)
        self.buttonSelect.pack()
        self.syncButton = Button(master, text="Sincronizeaza", command=self.askUserBeforeDelete)
        self.syncButton.pack()

    def selectPath(self):
        dirname = filedialog.askdirectory()
        self.label1['text'] = dirname
        return
    def selectPath2(self):
        dirname = filedialog.askdirectory()
        self.label2['text'] = dirname
        return
    def syncronFolder(self):
        folder1 = sync.Folder(self.label1['text'])
        folder2 = sync.Folder(self.label2['text'])
        folder1.sync(folder2.path)
    def askUserBeforeDelete(self):
        "This function is for dialog to ask user if he is sure."
        messagebox.askquestion("Warning!", "This action will remove all files from destination folder. Are you sure?", icon="warning")
        if 'yes':
            self.syncronFolder()
        else:
            return 0
