from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os


def download():
    win_user = os.environ['USERNAME']
    x = 0
    y = 100
    try:
        url = entrybox.get()
        if not url:
            messagebox.showwarning("Brak adresu URL", "Wprowadź adres URL do filmu przed rozpoczęciem pobierania.")
            return

        yt = YouTube(url)

        bar['value'] += 10
        x += 10
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % downloaded!")
        window.update_idletasks()

        title.set(str(yt.title))

        bar['value'] += 20
        x += 20
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % downloaded!")
        window.update_idletasks()

        output = f"C:\\Users\\{win_user}\\Videos"

        # Progress update 1
        bar['value'] += 20
        x += 20
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % downloaded!")
        window.update_idletasks()

        # Progress update 2
        yt = YouTube(url)
        title.set(str(yt.title))
        bar['value'] += 30
        x += 30
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % downloaded!")
        window.update_idletasks()

        # Download video
        video = yt.streams.get_highest_resolution()
        window.update_idletasks()
        video.download(output)

        # Progress update 3
        bar['value'] += 20
        x += 20
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} % downloaded!")
        window.update_idletasks()

        print(f"Video downloaded successfully to {output}")
        messagebox.showinfo("Pobieranie zakończone!", f"Film został pobrany w katalogu: {output}")
        bar['value'] = 0
        percent.set("")
        tasks.set("")
    except Exception as e:
        print(f"Error message: {e}")
        bar['value'] = 0
        messagebox.showerror("Błąd podczas pobierania", f"Wystąpił błąd: {e}\nSprawdź URL i spróbuj ponownie.")



window = Tk()
window.title("Youtube Downloader")
window.geometry("600x400")
window.iconbitmap("icon.ico")
window.configure(bg="#F0F0F0")
window.maxsize(width=600, height=320)
window.minsize(width=450, height=300)

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

Label(window, textvariable=percent, font=("Arial", 12)).pack()
Label(window, textvariable=tasks, font=("Arial", 12)).pack()

label_title = Label(window, textvariable=title, font=("Arial", 16, "bold"))
label_title.pack(pady=10)

frame = Frame(window, bg="#F0F0F0")
frame.pack()

entrybox = Entry(frame, font=("Arial", 16), width=30)
entrybox.pack(pady=10)

button = Button(frame, text="Download", command=download, bg="#4CAF50", fg="white", font=("Arial", 14))
button.pack(pady=10)

window.mainloop()
