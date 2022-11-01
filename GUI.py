from tkinter import StringVar, Tk, PhotoImage
from tkinter.ttk import Button, Label, Frame, Radiobutton
from lib.Hand import Hand

# All now need to do is update the pictures, as the winning works now

class App():
    def __init__(self) -> None:
        self.win: Tk = Tk() #creating the main window and storing the window object in 'win'
        self.choice: StringVar = StringVar() #stores result of radio buttons
        self.InitializePhotoImages()
        # Configure main window
        self.win.title("Rock Paper Scissors") # title of the window
        self.win.geometry("600x400") # changes size of window 

    def runApp(self):
        #We create the widgets here

        self.createGrid()

        self.createFrames()

        self.createLabels()

        self.createRadiobuttons()

        self.createButton()

        self.win.mainloop() # finally run the GUI/app

    def createGrid(self) -> None:
        """Creates grid for the main window of the GUI."""
        self.win.rowconfigure(index=0, weight=1)
        self.win.rowconfigure(index=1, weight=1)
        self.win.rowconfigure(index=2, weight=1)
        self.win.columnconfigure(index=0, weight=1)
        self.win.columnconfigure(index=1, weight=1)

    def createFrames(self) -> None:
        """Creates and place the 3 frames."""
        self.leftFrame:Frame = Frame(self.win)
        self.leftFrame.grid(row=1, column=0)

        self.rightFrame:Frame = Frame(self.win)
        self.rightFrame.grid(row=1, column=1)

        self.radiobuttonFrame:Frame = Frame(self.win)
        self.radiobuttonFrame.grid(row=2, column=0)

    def InitializePhotoImages(self) -> None:
        """Initializes the photo images."""
        self.rockImage: PhotoImage = PhotoImage(file="assets/rock.png")
        self.paperImage: PhotoImage = PhotoImage(file="assets/paper.png")
        self.scissorsImage: PhotoImage = PhotoImage(file="assets/scissors.png")
    
    def createLabels(self):
        """Creates the labels that tells the result and show what player and cpu throw."""
        self.result: Label = Label(self.win, text="Result")
        self.result.grid(row=0, column=0, columnspan=2, sticky='n', ipady=20)   
        #puts label onto the GUI (there are 2 other ways to do so which involves placing on a grid)

        # Other two methods are .grid() and .place()
        #Pack: it packs all the widgets in the center and places widgets in a sequence.
        #Grid: Grid places widgets in a row and column-wise.
        #Place: Place positions widgets in X and Y coordinates#running the loop that works as a trigger to show and update GUI

        self.playerImageLabel: Label = Label(self.leftFrame, image=self.rockImage)
        self.cpuImageLabel: Label = Label(self.rightFrame, image=self.paperImage)
        self.playerLabel: Label = Label(self.leftFrame, text="Player")
        self.cpuLabel: Label = Label(self.rightFrame, text="CPU")

        self.playerLabel.pack()
        self.cpuLabel.pack()
        self.playerImageLabel.pack()
        self.cpuImageLabel.pack()

    def createRadiobuttons(self) -> None:
        """Create the radio buttons. The radio buttons are the choices user gets to make."""
        rock_Radiobutton: Radiobutton = Radiobutton(self.radiobuttonFrame, text="Rock", value="Rock", variable=self.choice)
        paper_Radiobutton: Radiobutton = Radiobutton(self.radiobuttonFrame, text="Paper", value="Paper", variable=self.choice)
        scissors_Radiobutton: Radiobutton = Radiobutton(self.radiobuttonFrame, text="Scissors", value="Scissors", variable=self.choice)
        rock_Radiobutton.pack()
        paper_Radiobutton.pack()
        scissors_Radiobutton.pack()

    def createButton(self) -> None:
        """Create the button which "throws" the choice of the player."""
        self.button: Button = Button(self.win, text="Throw hand", command=self.play)
        self.button.grid(row=2, column=1)

    def play(self):
        # First figure out our two hands
        playerHand: Hand = Hand.stringToHand(self.choice.get())
        cpuHand: Hand = Hand.randomHand()

        # Update playerImageLabel and cpuImageLabel to match the hands
        self.updateImage(playerHand=playerHand, cpuHand=cpuHand)

        # Update result Text to tell who won
        #There is a case when first start and player doesn't click on a radio button
        if playerHand is None:
            self.result.config(text="Please pick a hand to throw.")
        # Now check if both are equal
        elif playerHand == cpuHand:
            self.result.config(text="Tie")
        # If not equal, then figure out the winner.
        elif playerHand > cpuHand:
            self.result.config(text="Player wins.")
        else:
            self.result.config(text="CPU wins.")

    def updateImage(self, playerHand: Hand, cpuHand: Hand):
        """Updates playerImageLabel and cpuImageLabel to match the hands they both will throw."""
        # First update playerHand
        if playerHand == Hand.ROCK:
            self.playerImageLabel.config(image=self.rockImage)
        elif playerHand == Hand.PAPER:
            self.playerImageLabel.config(image=self.paperImage)
        elif playerHand == Hand.SCISSORS:
            self.playerImageLabel.config(image=self.scissorsImage)
        
        # Now update cpuHand
        if cpuHand == Hand.ROCK:
            self.cpuImageLabel.config(image=self.rockImage)
        elif cpuHand == Hand.PAPER:
            self.cpuImageLabel.config(image=self.paperImage)
        elif cpuHand == Hand.SCISSORS:
            self.cpuImageLabel.config(image=self.scissorsImage)

if __name__ == "__main__":
    app = App()
    app.runApp()
