# import the necessary libraries
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from pytube import YouTube
import os


# function to download the video
def download_video():
    # get the video URL from the entry field
    url = entry.get()
    try:
        # create a YouTube object and get the highest resolution stream
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()

        # ask the user to select the save directory and filename
        save_path = filedialog.asksaveasfilename(defaultextension='.mp4', filetypes=[("MP4 files", "*.mp4")])

        # download the video to the selected directory
        stream.download(output_path=os.path.dirname(save_path), filename=os.path.basename(save_path))

        # show a message when the download is complete
        messagebox.showinfo("Download Complete", "Video has been downloaded.")

    except:
        # show an error message if the download fails
        messagebox.showerror("Error", "Invalid URL or download failed.")


# function to open the directory where the video is saved
def open_directory():
    # get the directory where the video is saved
    save_path = filedialog.askdirectory()
    # open the directory in the file explorer
    os.startfile(save_path)


# function to play the downloaded video
def play_video():
    # ask the user to select the video file
    video_path = filedialog.askopenfilename(defaultextension='.mp4', filetypes=[("MP4 files", "*.mp4")])
    # play the video using the default media player
    os.startfile(video_path)


# function to clear the entry field
def clear_entry():
    entry.delete(0, END)


# create the main window
root = Tk()
root.title("YouTube downloader")
root.geometry("600x300")
root.resizable(False, False)

# create the widgets
label = Label(root, text="Enter URL of Video:")
entry = Entry(root, width=50)
button_save_to = Button(root, text="Save to", command=download_video)
button_download = Button(root, text="Download", command=download_video)
button_open_directory = Button(root, text="Open Directory", command=open_directory)
button_play = Button(root, text="Play", command=play_video)
button_clear = Button(root, text="x", command=clear_entry)

# arrange the widgets using grid layout
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=W)
button_save_to.grid(row=1, column=0, padx=10, pady=10)
button_download.grid(row=1, column=1, padx=10, pady=10)
button_open_directory.grid(row=1, column=2, padx=10, pady=10)
button_play.grid(row=2, column=1, padx=10, pady=10)
button_clear.grid(row=0, column=3, padx=10, pady=10)

# start the main event loop
root.mainloop()
