from pytube import YouTube

url = input("Enter URL: ")
my_video = YouTube(url)

print("Downloading ",my_video.title)

my_video = my_video.streams.get_highest_resolution()

my_video.download()


print("Succesfuly downloaded ",my_video.title)
wait = input()