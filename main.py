from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from moviepy.editor import *

win_user = os.environ['USERPROFILE']
output = f"{win_user}\\Videos"


def normalstate():
    button_down.config(state='normal')
    entrybox.config(state='normal')
    option_menu.config(state='normal')


def aboutme():
    about = Tk()
    about.title("INFO")
    about.minsize(width=400, height=100)
    about.maxsize(width=400, height=100)
    Label(about, text="Youtube Downloader INFO", font=("Arial", 20, "bold")).pack()
    Label(about, text="Autor: Piotr Zarzycki", font=("Arial", 10, "")).pack()
    Label(about, text="Wersja: 1.0.0", font=("Arial", 10, "")).pack()
    about.mainloop()


def settings():
    global output

    def change():
        global output  # Użyj zmiennej globalnej
        window_settings.lift()
        selected_path = filedialog.askdirectory()
        window_settings.lift()

        if selected_path:
            output = selected_path  # Zaktualizuj zmienną globalną
            path_change.set(output)
            otp.set(output)
            window.update_idletasks()
        window.lift()
        path_change.set(output)
        otp.set(output)
        window.update_idletasks()
        window_settings.lift()

    window_settings = Toplevel()
    path_change = StringVar()
    window_settings.iconbitmap("ico/settings.ico")

    path_change.set(output)
    window_settings.minsize(width=300, height=200)
    window_settings.maxsize(width=300, height=200)
    Label(window_settings, text="Ustawienia", font=("Arial", 30)).pack(padx=20, pady=15)
    window_settings.title("Ustawienia")
    window_settings.geometry("300x200")

    Label(window_settings,
          text="Ustawienia lokalizacji pobierania: ",
          font=("Arial", 10, "bold")).place(x=0, y=80)
    Label(window_settings, textvariable=path_change, width=20).place(x=0, y=100)
    Button(window_settings, text="Zmień", command=change).place(x=200, y=100)


def download():
    global tytul, video, format_pliku, mp3plik
    button_down.config(state='disabled')
    entrybox.config(state='disabled')
    option_menu.config(state='disabled')
    format_pliku = var.get()

    x = 0
    y = 100
    try:
        url = entrybox.get()
        if not url:
            messagebox.showwarning("Brak URL", "Proszę wprowadzić URL do wideo przed pobraniem.")
            normalstate()
            return

        bar['value'] += 10
        x += 10
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % pobrane!")
        window.update_idletasks()

        bar['value'] += 20
        x += 20
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % pobrane!")
        window.update_idletasks()

        # Aktualizacja postępu 1
        bar['value'] += 20
        x += 20
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % pobrane!")
        window.update_idletasks()

        # Aktualizacja postępu 2
        yt = YouTube(url)
        tytul = yt.title
        title.set(str(yt.title))
        alfabet = ['a', 'ą', 'ę', 'ć', 'ż', 'ź', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6',
                   '7', '8', '9', '0']
        for litera in tytul.lower():
            if litera not in alfabet:
                tytul = tytul.replace(litera, '')

        yt.title = tytul
        bar['value'] += 30
        x += 30
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % pobrane!")
        window.update_idletasks()

        if format_pliku == '.mp4':
            video = yt.streams.get_highest_resolution()
        if format_pliku == '.mp3':
            video = yt.streams.get_audio_only()

        window.update_idletasks()
        video.download(output)

        # Aktualizacja postępu 3
        bar['value'] += 20
        x += 20
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % pobrane!")
        window.update_idletasks()
        button_open.place(x=490, y=230)
        if format_pliku != '.mp4':
            video_clip = AudioFileClip(f"{output}\\{tytul}.mp4")
            video_clip.write_audiofile(f"{output}\\{tytul}.mp3")
            os.remove(f"{output}\\{tytul}.mp4")
        answer = messagebox.askquestion('Pobieranie zakończone!',
                                        f"Plik został pobrany do katalogu:\n{output}.\nCzy chcesz odtworzyć plik?")
        open_path = f"{output}\\{tytul}{format_pliku}"
        if answer == 'yes':
            try:
                # Otwieranie pliku wideo za pomocą domyślnego odtwarzacza
                os.startfile(open_path)

            except Exception as e:
                normalstate()
        else:
            pass
            normalstate()
        bar['value'] = 0
        percent.set("")
        tasks.set("")
    except Exception as e:
        bar['value'] = 0
        messagebox.showerror("Błąd podczas pobierania", f"Wystąpił błąd: {e}\nSprawdź URL i spróbuj ponownie.")
    normalstate()


def open_last():
    global output, format_pliku, tytul
    g1 = f"{output}\\{tytul}{format_pliku}"
    try:
        # Otwieranie pliku wideo za pomocą domyślnego odtwarzacza
        os.startfile(g1)

    except Exception as e:
        messagebox.showerror(f"Błąd", f"Błąd podczas otwierania pliku: {e}")


window = Tk()
window.bind('<Return>', lambda event: download())

window.title("Youtube Downloader")
window.geometry("600x400")
window.iconbitmap("ico/icon.ico")
window.configure(bg="#F0F0F0")
window.maxsize(width=600, height=320)
window.minsize(width=600, height=320)

Wybor_formatu = ['.mp4', '.mp3']

var = StringVar(window)
var.set(Wybor_formatu[0])  # Ustaw domyślną opcję

option_menu = OptionMenu(window, var, *Wybor_formatu)
option_menu.config(bg='#d5efff', width=6, height=1, font=('arial', 10, 'bold'))
option_menu.place(x=30, y=232)

label = Label(window,
              text="Youtube Downloader",
              font=("Helvetica", 24, "bold"),
              bg="#ff563c",
              fg="white",
              width="22")
label.pack(pady=10)

bar = Progressbar(window, length=500, mode='determinate')
bar.pack(pady=10)

percent = StringVar()
tasks = StringVar()
title = StringVar()
otp = StringVar()
otp.set(output)
Label(window, textvariable=percent, font=("Arial", 12)).pack()
Label(window, textvariable=tasks, font=("Arial", 12)).pack()

label_title = Label(window, textvariable=title, font=("Arial", 16, "bold"))
label_title.pack(pady=10)

Label(window, textvariable=otp, width=70).pack()

frame = Frame(window, bg="#F0F0F0")
frame.pack()

entrybox = Entry(frame, font=("Arial", 16), width=30)
entrybox.pack(pady=10)

button_open = Button(window, text="Otwórz", command=open_last, bg="#4303af", fg="white", font=("Arial", 14))

button_down = Button(window, text="Pobierz", command=download, bg="#4CAF50", fg="white", font=("Arial", 14))
button_down.place(x=245, y=270)

Aboutme = Button(window, text="About", command=aboutme, font=("Arial", 14), bg="white")
Aboutme.place(x=10, y=12)

setting_photo = PhotoImage(file="img/icons8-settings-32.png")

settings_button = Button(window, image=setting_photo, command=settings, bg="white")
settings_button.place(x=530, y=10)
window.mainloop()
