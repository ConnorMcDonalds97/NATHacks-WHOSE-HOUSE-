import tkinter.filedialog
import os
import tkinter
import const

def invokeStartScreen():
    CONFIG = {
        "StartGameTrue": False,
        "SongFile": 'Queen - Bohemian Rhapsody',
        "Finger1": 0,
        "Finger2": 0,
        "Finger3": 0,
        "Finger4": 0
    }

    def btnSelectSongClicked():
        searchDir = os.path.join(os.getcwd(), "midi_songs")
        songPath = tkinter.filedialog.askopenfilename(
            initialdir=searchDir,
            filetypes=[("AllFiles", "*.mid")]
            )
        if (songPath):
            songName = os.path.basename(songPath).strip(".mid")
            songLabelText.set(songName)
            CONFIG["SongFile"] = songName
            

    def btnStartGame():
        CONFIG["StartGameTrue"] = True
        window.destroy()
        

    def clicked():
        if finger1.get() == 1:
            CONFIG["Finger1"] = 1
        else:
            CONFIG["Finger1"] = 0

        if finger2.get() == 1:
            CONFIG["Finger2"] = 1
        else:
            CONFIG["Finger2"] = 0

        if finger3.get() == 1:
            CONFIG["Finger3"] = 1
        else:
            CONFIG["Finger3"] = 0
        
        if finger4.get() == 1:
            CONFIG["Finger4"] = 1
        else:
            CONFIG["Finger4"] = 0

    window = tkinter.Tk()
    window.title("Placeholder Game Title")
    window.geometry(f"750x500")


    finger1 = tkinter.IntVar()
    finger2 = tkinter.IntVar()
    finger3 = tkinter.IntVar()
    finger4 = tkinter.IntVar()

    # Create checkboxes
    check1 = tkinter.Checkbutton(window, text='Finger 1', variable=finger1, onvalue=1, offvalue=0, font=("helvetica", 18), command = clicked)
    check1.place(x=10,y=100)

    check2 = tkinter.Checkbutton(window, text='Finger 2', variable=finger2, onvalue=1, offvalue=0, font=("helvetica", 18), command = clicked)
    check2.place(x=10, y=150)

    check3 = tkinter.Checkbutton(window, text='Finger 3', variable=finger3, onvalue=1, offvalue=0, font=("helvetica", 18), command = clicked)
    check3.place(x=10, y=200)

    check4 = tkinter.Checkbutton(window, text='Finger 4', variable=finger4, onvalue=1, offvalue=0, font=("helvetica", 18), command = clicked)
    check4.place(x=10, y=250)

    startGameButton = tkinter.Button(window, text="Start Game", command=btnStartGame, font=("helvetica", 35), width = 10, height = 1)
    startGameButton.place(x=350,y=350)

    selectSongButton = tkinter.Button(window, text="Select Song", command=btnSelectSongClicked, font=("helvetica", 25))
    selectSongButton.place(x=10, y=350)

    songLabelText = tkinter.StringVar(value=CONFIG["SongFile"])
    songLabel = tkinter.Label(window, textvariable=songLabelText, font=("Arial", 25))
    songLabel.place (x=270,y=300)

    window.mainloop()

    print(CONFIG)
    return CONFIG

if __name__ == "__main__":
    invokeStartScreen()
