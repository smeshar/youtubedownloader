from pytube import YouTube

def download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download()
    except:
        print("Error")
    print("download is correct")

url = input("Enter URL ")
download(url)
a = input()