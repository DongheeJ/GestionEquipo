from tkinter import Tk
# from view.Index_view import Index_view
from view.MainApp import MainApp
if __name__ == "__main__":
    root = Tk()
    # index_view = Index_view(root)
    mainApp = MainApp(root)
    root.mainloop()