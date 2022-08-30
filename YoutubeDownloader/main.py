from tkinter import *
from tkinter import ttk
import time
from pytube import YouTube
from threading import Thread


class AsyncDownload(Thread):
    def __init__(self, url, formatSelectionVar, downloadTitleLabel, downloadProgressBar):
        super().__init__()

        self.url = url
        self.formatSelectionVar = formatSelectionVar.get()
        self.downloadTitleLabel = downloadTitleLabel
        self.progressBar = downloadProgressBar

    def getBestResolution(self, streams):
        resolutions = ['720p', '480p', '240p', '144p']

        for resolution in resolutions:
            if streams.filter(res=resolution):
                return streams.filter(res=resolution, progressive=True)

    def run(self):
        yt = YouTube(self.url.get())

        self.downloadTitleLabel['text'] = "You're now donwloading {}".format(
            yt.title)
        self.downloadTitleLabel.grid(column=0, row=3, sticky=(E, W))

        progressBarThread = AsyncProgressBar(self.progressBar)

        progressBarThread.start()

        if self.formatSelectionVar == 'Audio':
            yt.streams.filter(
                only_audio=True).first().download(output_path='./Downloads')
        elif self.formatSelectionVar == 'Video':
            self.getBestResolution(yt.streams).first().download(
                output_path='./Downloads')

        print(yt.title)
        self.url.set('')


class AsyncProgressBar(Thread):
    def __init__(self, progressBar):
        super().__init__()

        self.progressBar = progressBar

    def run(self):

        self.progressBar.grid(column=1, row=3, sticky=(S), pady=10)

        self.progressBar.start()


class YoutubeDownloader:
    def __init__(self, App):
        self.App = App
        App.title('Youtube Downloader')

        self.mainFrame = ttk.Frame(App, padding=(25, 0, 25, 25))

        self.titleImage = PhotoImage(file="./data/AppLogo.png")
        self.titleLabel = ttk.Label(self.mainFrame, padding=(15, 15, 15, 15))
        self.titleLabel['image'] = self.titleImage

        appIcon = PhotoImage(file="./data/AppIcon.png")
        App.iconphoto(False, appIcon)

        self.url = StringVar()
        self.urlLabel = ttk.Label(
            self.mainFrame, text="URL:", padding=(0, 0, 15, 0), justify="right")
        self.urlEntry = ttk.Entry(self.mainFrame, textvariable=self.url)

        self.formatSelectionVar = StringVar()
        self.formatSelectionVar.set('Video')
        self.formatSelection = ttk.Combobox(
            self.mainFrame, textvariable=self.formatSelectionVar)
        self.formatSelection['value'] = ('Audio', 'Video')

        self.downloadButton = ttk.Button(
            self.mainFrame, text="Download", command=self.downloadHandler, padding=(1, 1, 1, 1))

        self.mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))
        self.titleLabel.grid(column=1, row=0, sticky=(N))
        self.urlLabel.grid(column=0, row=1, sticky=(E, W))
        self.urlEntry.grid(column=1, row=1, sticky=(E, W))
        self.formatSelection.grid(column=2, row=1, sticky=(E, W), padx=10)
        self.downloadButton.grid(column=1, row=2, sticky=(S), pady=10)

        App.columnconfigure(0, weight=1)
        App.rowconfigure(0, weight=1)
        self.mainFrame.columnconfigure(0, weight=3)
        self.mainFrame.columnconfigure(1, weight=3)
        self.mainFrame.columnconfigure(2, weight=3)
        self.mainFrame.rowconfigure(0, weight=3)
        self.mainFrame.rowconfigure(1, weight=1)
        self.mainFrame.rowconfigure(2, weight=1)

        self.urlEntry.focus()
        App.bind("<Return>", self.downloadHandler)

    def threadMonitor(self, thread):
        if thread.is_alive():
            self.App.after(100, lambda: self.threadMonitor(thread))
        else:
            self.downloadProgressBar.stop()
            self.downloadTitleLabel['text'] = 'Download completed'
            time.sleep(2)
            self.downloadProgressBar.destroy()
            self.downloadTitleLabel.destroy()

    def downloadHandler(self):

        self.downloadTitleLabel = ttk.Label(
            self.mainFrame, padding=(0, 0, 15, 0))
        self.downloadProgressBar = ttk.Progressbar(
            self.mainFrame, orient=HORIZONTAL, length=280, mode='indeterminate')

        downloadThread = AsyncDownload(
            self.url, self.formatSelectionVar, self.downloadTitleLabel, self.downloadProgressBar)

        downloadThread.start()

        self.threadMonitor(downloadThread)


App = Tk()
YoutubeDownloader(App)
App.mainloop()
