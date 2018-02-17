# Tkinter from Python 3 as tkinter
# The Python Imaging Library (PIL)

import tkinter as tk


class Application(tk.Frame):
    # Call the constructor for the parent class
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    # Test method
    def loadUp(self, button):
        content = button.get('1.0')
        print('Content: ')
        print(content)

    # Define the layout of the window
    def createWidgets(self):
        self.firstPathLabel = tk.Label(self, text="First Image")
        self.firstPathLabel.grid(column=0, row=0)
        self.firstPathText = tk.Text(self, height=1, width=30)
        self.firstPathText.grid(column=1, row=0, columnspan=3)

        self.firstPathLabel = tk.Label(self, text="Second Image")
        self.firstPathLabel.grid(column=0, row=1)
        self.secPathText = tk.Text(self, height=1, width=30)
        self.secPathText.grid(column=1, row=1, columnspan=3)

        self.loadUpButton = tk.Button(
                self, width=10, text='Load Images',
                command=self.loadUp(self.firstPathText))
        self.loadUpButton.grid(column=12, row=2)

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
