import youtube_dl
import getpass

def mp3_download(url):
    """
    Takes in youtube url and downloads mp3

    Parameter:url(string)
    """
    try:
    #Ask the user for the video they want to download
        path_to_download_folder = f"/home/{getpass.getuser()}/Downloads"
        #Download and convert the file into mp3 and store in downloads folder
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=url, download=False
        )
        
        filename = f"{video_info['title']}.mp3"
        if (len(filename)>34):
            filename = filename[0:30]+'.mp3'
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': f'/home/{getpass.getuser()}/Downloads/{filename}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality':'192',
                }]
            }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        return 0
    except:
        return 1