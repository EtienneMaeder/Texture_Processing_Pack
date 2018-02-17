# Tkinter from Python 3 as tkinter
# The Python Imaging Library (PIL)
# Textfield -> Sourcefile path
# Textfield -> Destination file path
# 4 Buttons -> one for each channel

import tkinter as tk


class Application(tk.Frame):
    # Call the constructor for the parent class
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Texture Processing")
        self.grid()
        self.createWidgets()

    # Check the color of each button
    def moveChannelContent(self):
        # TODO: Check the color of each button

    # load the image into memory
    def loadUpImage(self):
        print('Load Image')

    # Define the layout of the window
    def createWidgets(self):
        self.firstPathLabel = tk.Label(self, text="First Image")
        self.firstPathLabel.grid(column=0, row=0, columnspan=2)
        self.firstPathText = tk.Text(self, height=1, width=30)
        self.firstPathText.grid(column=2, row=0, columnspan=3)

        self.firstPathLabel = tk.Label(self, text="Second Image")
        self.firstPathLabel.grid(column=0, row=1, columnspan=2)
        self.secPathText = tk.Text(self, height=1, width=30)
        self.secPathText.grid(column=2, row=1, columnspan=3)

        self.loadUpButton = tk.Button(
                self, width=10, height=2, text='Load Images',
                command=lambda: self.loadUpImage())
        self.loadUpButton.grid(column=5, row=0, rowspan=2)

        self.firstRChannel = tk.Button(self, width=2, text='R')
        self.firstRChannel.configure(
                command=lambda: ToggleButtonState(self.firstRChannel))
        self.firstRChannel.grid(column=1, row=3)
        self.firstGChannel = tk.Button(self, width=2, text='G')
        self.firstGChannel.configure(
                command=lambda: ToggleButtonState(self.firstGChannel))
        self.firstGChannel.grid(column=1, row=4)
        self.firstBChannel = tk.Button(self, width=2, text='B')
        self.firstBChannel.configure(
                command=lambda: ToggleButtonState(self.firstBChannel))
        self.firstBChannel.grid(column=1, row=5)
        self.firstAChannel = tk.Button(self, width=2, text='A')
        self.firstAChannel.configure(
                command=lambda: ToggleButtonState(self.firstAChannel))
        self.firstAChannel.grid(column=1, row=6)

        self.secondRChannel = tk.Button(self, width=2, text='R')
        self.secondRChannel.configure(
                command=lambda: ToggleButtonState(self.secondRChannel))
        self.secondRChannel.grid(column=4, row=3)
        self.secondGChannel = tk.Button(self, width=2, text='G')
        self.secondGChannel.configure(
                command=lambda: ToggleButtonState(self.secondGChannel))
        self.secondGChannel.grid(column=4, row=4)
        self.secondBChannel = tk.Button(self, width=2, text='B')
        self.secondBChannel.configure(
                command=lambda: ToggleButtonState(self.secondBChannel))
        self.secondBChannel.grid(column=4, row=5)
        self.secondAChannel = tk.Button(self, width=2, text='A')
        self.secondAChannel.configure(
                command=lambda: ToggleButtonState(self.secondAChannel))
        self.secondAChannel.grid(column=4, row=6)

        self.printButton = tk.Button(
                self, width=8, height=2, text='Move',
                command=lambda: self.moveChannelContent())
        self.printButton.grid(column=1, row=3, columnspan=4, rowspan=3)


def ToggleButtonState(button):
    # Background color flip flop
    if (button.cget('bg') == 'SystemButtonFace'):
        button.configure(bg='gray')
    elif (button.cget('bg') == 'gray'):
        button.configure(bg='SystemButtonFace')

# app = Application()
# app.mainloop()
