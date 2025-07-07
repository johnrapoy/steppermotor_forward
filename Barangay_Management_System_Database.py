from tkinter import *
class Barangay:
    def _init_(self,root):
        self.root=root
        self.root.title("Barangay Management System")
        self.root.geometry("1350x700+0+0")


root=Tk()
ob=Barangay(root)
root.mainloop()
