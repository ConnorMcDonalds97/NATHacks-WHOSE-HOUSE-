import tkinter as tk
from tkinter import filedialog
import os

def invokeEndScreen(score):
    window = tk.Tk()
    window.geometry("1000x500")
    window.title("Music Reflex Game")

    main_frame = tk.Frame(window, bg="#0D1E34")
    main_frame.pack(expand=True, fill="both")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    tk.Label(
        text=f"Thanks For Playing\nScore: {score}\n\nWhose House? MACS House",
        font=("Helvetica", int(40 * screen_height / 1000), "bold"),
        bg="#0D1E34",
        fg="white",
    ).place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

def invokeStartScreen():
    DIFFS = ["Easy", "Medium", "Hard"]
    DIFFSCOLOURS = ["#0DD41E", "#DAED08", "#D40D0D"]
    MODES = ["Tempo", "Melody"]
    CONFIG = {
        "StartGameTrue": False,
        "SongFile": "Queen - Bohemian Rhapsody",
        "DifficultyIndex": 0,
        "ModeIndex": 0,
        "Finger1": 0,
        "Finger2": 0,
        "Finger3": 0,
        "Finger4": 0,
    }

    def btnDifficultyCycle(button):
        if CONFIG["DifficultyIndex"] >= 2:
            CONFIG["DifficultyIndex"] = 0
        else:
            CONFIG["DifficultyIndex"] += 1

        button.config(text=DIFFS[CONFIG["DifficultyIndex"]], bg=DIFFSCOLOURS[CONFIG["DifficultyIndex"]])

    def btnModeCycle(button):
        if CONFIG["ModeIndex"] == 1:
            CONFIG["ModeIndex"] = 0
        else:
            CONFIG["ModeIndex"] = 1

        button.config(text=MODES[CONFIG["ModeIndex"]])

    def btnSelectSongClicked():
        searchDir = os.path.join(os.getcwd(), "midi_songs")
        songPath = filedialog.askopenfilename(
            initialdir=searchDir,
            filetypes=[("MIDI files", "*.mid")],
        )
        if songPath:
            songName = os.path.basename(songPath).replace(".mid", "")
            songLabelText.set(songName)
            CONFIG["SongFile"] = songName

    def btnStartGame():
        CONFIG["StartGameTrue"] = True
        window.destroy()

    def updateFingerConfig():
        CONFIG["Finger1"] = finger1.get()
        CONFIG["Finger2"] = finger2.get()
        CONFIG["Finger3"] = finger3.get()
        CONFIG["Finger4"] = finger4.get()

    # === WINDOW SETUP ===
    window = tk.Tk()
    window.title("Music Reflex Game")
    window.attributes("-fullscreen", True)  # Start fullscreen

    # Allow toggling fullscreen with F11 / Esc
    def toggle_fullscreen(event=None):
        window.attributes("-fullscreen", not window.attributes("-fullscreen"))

    def end_fullscreen(event=None):
        exit(0)
        window.attributes("-fullscreen", False)

    window.bind("<F11>", toggle_fullscreen)
    window.bind("<Escape>", end_fullscreen)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Use a scaling factor for font sizes based on screen size
    scale = screen_height / 1080
    base_font = ("Helvetica", int(18 * scale))
    title_font = ("Helvetica", int(40 * scale), "bold")
    button_font = ("Helvetica", int(28 * scale))

    # === LAYOUT ===
    main_frame = tk.Frame(window, bg="#0D1E34", padx=40, pady=40)
    main_frame.pack(expand=True, fill="both")

    title = tk.Label(
        main_frame,
        text="🎵 Music Reflex Game 🎵",
        font=title_font,
        fg="white",
        bg="#202020",
    )
    title.grid(row=0, column=0, columnspan=2, pady=30)

    # Checkboxes for fingers
    finger1, finger2, finger3, finger4 = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

    check_frame = tk.Frame(main_frame, bg="#202020")
    check_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)

    for i, (text, var) in enumerate(
        [("Finger 1", finger1), ("Finger 2", finger2), ("Finger 3", finger3), ("Finger 4", finger4)]
    ):
        tk.Checkbutton(
            check_frame,
            text=text,
            variable=var,
            onvalue=1,
            offvalue=0,
            font=button_font,
            bg="#202020",
            fg="white",
            selectcolor="#303030",
            command=updateFingerConfig,
        ).grid(row=i, column=0, pady=10, sticky="w")

    # Song selector and labels
    right_frame = tk.Frame(main_frame, bg="#202020")
    right_frame.grid(row=1, column=1, sticky="nsew", padx=40, pady=20)

    songLabelText = tk.StringVar(value=CONFIG["SongFile"])
    tk.Label(
        right_frame,
        text="Selected Song:",
        font=base_font,
        fg="white",
        bg="#202020",
    ).pack(pady=10)
    tk.Label(
        right_frame,
        textvariable=songLabelText,
        font=("Arial", int(22 * scale)),
        fg="#FFD700",
        bg="#202020",
    ).pack(pady=10)

    tk.Button(
        right_frame,
        text="Select Song",
        command=btnSelectSongClicked,
        font=button_font,
        width=12,
        height=1,
        bg="#404040",
        fg="white",
        activebackground="#505050",
    ).pack(pady=10)

    # Start game button at the bottom
    tk.Button(
        main_frame,
        text="▶ Start Game",
        command=btnStartGame,
        font=("Helvetica", int(36 * scale), "bold"),
        bg="#28A745",
        fg="white",
        activebackground="#2ECC71",
        width=15,
        height=2,
    ).grid(row=3, column=0, columnspan=2, pady=0)

    # difficulty button
    difficultyButton = tk.Button(
        main_frame,
        text=DIFFS[CONFIG["DifficultyIndex"]],
        command=lambda: btnDifficultyCycle(difficultyButton),
        font=button_font,
        width=12,
        height=1,
        bg=DIFFSCOLOURS[CONFIG["DifficultyIndex"]],
        fg="white",
        activebackground="#F7F3F3",
    )
    difficultyButton.grid(row=2, column=1, columnspan=1, pady=80)

    # mode button (melody/Tempo)
    modeButton = tk.Button(
        main_frame,
        text=MODES[CONFIG["ModeIndex"]],
        command=lambda: btnModeCycle(modeButton),
        font=button_font,
        width=12,
        height=1,
        bg="#404040",
        fg="white",
        activebackground="#F7F3F3",
    )
    modeButton.grid(row=2, column=0, columnspan=1, pady=80)

    window.mainloop()
    print(CONFIG)
    return CONFIG


if __name__ == "__main__":
    # invokeStartScreen()
    invokeEndScreen(1000)
