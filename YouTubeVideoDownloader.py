from pytube import YouTube


def downloadVideo(yt):
    ys = yt.streams.get_highest_resolution()
    ys.download(r'C:\Users\Elamine\Downloads')

while True:
    link = input("Enter the youtube video link: ").strip()
    yt = YouTube(link)
    downloadVideo(yt)
