from pytube import YouTube
from sys import argv

# where to save
SAVE_PATH = '../../Downloads'

# extracting the youtube video link from the command line
link = argv[1]

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# Print the title and number of views of the video
print("title:", yt.title)
print("views:", yt.views)


try:
    # downloading the video
    vd = yt.streams.get_highest_resolution()
    vd.download(SAVE_PATH)

except:
    print("Some Error!")
print('Task Completed!')
