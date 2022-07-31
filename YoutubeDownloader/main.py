from tkinter import *
from tkinter import ttk
from turtle import width
from pytube import YouTube


def download(*args):
    yt = YouTube(url.get())

    print(yt.title)
    yt.streams.filter(file_extension='mp4', res='720p').first().download()
    url.set('')


App = Tk()
App.title('Youtube Downloader')

mainFrame = ttk.Frame(App, padding=(25, 0, 25, 25))

titleImage = PhotoImage(file="./AppCover.png")
titleLabel = ttk.Label(mainFrame, padding=(15, 15, 15, 15))
titleLabel['image'] = titleImage

url = StringVar()
urlLabel = ttk.Label(mainFrame, text="URL:", padding=(0, 0, 15, 0))
urlEntry = ttk.Entry(mainFrame, textvariable=url)

downloadButton = ttk.Button(
    mainFrame, text="Download", command=download, padding=(1, 1, 1, 1))

mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))
titleLabel.grid(column=1, row=0, sticky=(N))
urlLabel.grid(column=0, row=1, sticky=(E, W))
urlEntry.grid(column=1, row=1, columnspan=2, sticky=(E, W))
downloadButton.grid(column=1, row=2, sticky=(S), pady=10)

App.columnconfigure(0, weight=1)
App.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=3)
mainFrame.columnconfigure(2, weight=1)
mainFrame.rowconfigure(0, weight=3)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)

urlEntry.focus()
App.bind("<Return>", download)

App.mainloop()
