import tkinter as tk

from PIL import ImageTk, Image

from demos.week_5.gui_demo.Backend import Backend


class Gui:

    def __init__(self):
        """Constructor of GUI"""
        # Backend object
        self.backend = Backend()
        # Initialize the Tkinter
        self.window = tk.Tk()
        self.window.wm_title("Demo Gui")
        self.window.geometry("600x600")
        # Create frames
        self.menuFrame = tk.Frame(master=self.window, height=400, width=200)
        self.displayFrame = tk.Frame(master=self.window, height=400, width=200)
        self.messageFrame = tk.Frame(master=self.window, height=400, width=200)

        # Build menu frame
        menuTitle = tk.Label(master=self.menuFrame, text="Menu", font=("Arial", 12))
        menuTitle.pack(padx=5, pady=5)
        self.userInputStringVariable = tk.StringVar(master=self.menuFrame, value="<Enter String>")
        userInputStringEntry = tk.Entry(master=self.menuFrame, textvariable=self.userInputStringVariable)
        userInputStringEntry.pack(padx=5, pady=5)
        setStringButton = tk.Button(master=self.menuFrame, text="Sets String", width=12, height=1, bg="green",
                                    command=self.setStringEvent)
        setStringButton.pack(pady=5, padx=5)
        printStringButton = tk.Button(master=self.menuFrame, text="Prints String", width=12, height=1, bg="blue",
                                      command=self.printStringEvent)
        printStringButton.pack(pady=5, padx=5)
        catPicPlzButton = tk.Button(master=self.menuFrame, text="Cat Pic Plz", width=12, height=1, bg="red",
                                    command=self.displayCatPic)
        catPicPlzButton.pack(pady=5, padx=5)

        # Build Message Frame
        messageTitle = tk.Label(master=self.messageFrame, text="Message", font=("Arial", 12))
        messageTitle.pack(padx=5, pady=5)
        self.messageText = tk.StringVar(master=self.messageFrame, value="Set a string to begin...")
        messageBoard = tk.Message(master=self.messageFrame, textvariable=self.messageText, relief="raised")
        messageBoard.pack(pady=5, padx=5)

        # Pack frames
        self.menuFrame.pack(side="left", padx=5, pady=5)
        self.displayFrame.pack(side="left", padx=5, pady=5)
        self.messageFrame.pack(side="left", padx=5, pady=5)

    def setStringEvent(self):
        stringToSet = self.userInputStringVariable.get()
        self.backend.setString(stringToSet)
        print("Set string to " + stringToSet)

    def printStringEvent(self):
        stringToPrint = self.backend.getString()
        stringLength = self.backend.calculateStringLength()
        self.messageText.set("String = " + stringToPrint + "\nLength = " + str(stringLength))
        self.buildGridEvent()

    def buildGridEvent(self):
        for element in self.displayFrame.winfo_children():
            element.destroy()
        vowels = ["a", "e", "i", "o", "u"]
        backendString = self.backend.getString()
        for y in range(2):
            for x in range(self.backend.calculateStringLength()):
                letter = backendString[x]
                canvas = tk.Canvas(master=self.displayFrame, width=30, height=30)
                canvas.create_text(15, 15, text=str(x), font=("Arial", 8))
                canvas.grid(row=0, column=x)
                if letter in vowels:
                    canvas = tk.Canvas(master=self.displayFrame, width=30, height=30, bg="light goldenrod")
                    canvas.create_text(15, 15, text=letter, font=("Arial", 12), fill="red")
                    canvas.grid(row=1, column=x)
                else:
                    canvas = tk.Canvas(master=self.displayFrame, width=30, height=30, bg="salmon")
                    canvas.create_text(15, 15, text=letter, font=("Arial", 12), fill="green")
                    canvas.grid(row=1, column=x)
        self.displayFrame.pack()

    def displayCatPic(self):
        for element in self.displayFrame.winfo_children():
            element.destroy()
        imageCanvas = tk.Canvas(master=self.displayFrame, width=500, height=600)
        catImg = ImageTk.PhotoImage(Image.open("cat.png"))
        imageCanvas.create_image(10, 10, anchor="nw", image=catImg)
        imageCanvas.image = catImg
        imageCanvas.pack()


if __name__ == "__main__":
    gui = Gui()
    tk.mainloop()
