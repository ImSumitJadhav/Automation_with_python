#library name: pytube
#link: https://pytube.io/en/latest/

#import
from pytube import YouTube

#function to download video
def download_video(url,save_path):
    try:
        yt=YouTube (url)
        #filter out with respect to file type and resolution
        streams=yt.streams.filter(progressive=True, file_extension="mp4")
        #select highest resolution
        highest_res_stream=streams.get_highest_resolution()
        #download video 
        highest_res_stream.download(output_path=save_path)
        #print "Video downloaded successfully!"
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

#give url of video
url = "https://www.youtube.com/watch?v=zT7niRUOs9o"
#give output path
save_path = ""

#call function
download_video(url, save_path)