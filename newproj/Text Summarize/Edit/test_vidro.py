"""
install the needed library pytube so you can interact with video url
use pip3/pip install pytube
"""
import pytube

#"""
#add the url video to start download from it 
#"""
## video = input("enter your url here :  ")
#
#ls = [
#       'https://www.youtube.com/watch?v=FvGBifoc1-A',
#      'https://www.youtube.com/watch?v=K2V6Y7zQ8NU']
#for i in ls:
#    video = i
#    youtube = pytube.YouTube(video)
#    video = youtube.streams.first()
#    video.download(r'C:\Users\samo\Downloads\Video\Recycleview')
#    
    
def  load_video (url ,name) : 
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download(r'video/')
    
url= 'https://www.aljazeera.net/news/alquds/2019/12/24/%D8%A7%D9%84%D9%82%D8%AF%D8%B3-%D9%81%D9%84%D8%B3%D8%B7%D9%8A%D9%86-%D8%A7%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%8A%D9%85%D8%A9-%D8%A8%D8%A7%D8%A8-%D8%A7%D9%84%D8%AE%D9%84%D9%8A%D9%84-%D8%A8%D8%A7%D8%A8-%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D9%88%D8%AF-%D8%A7%D9%84%D9%85%D8%B3%D8%AC%D8%AF-%D8%A7%D9%84%D8%A3%D9%82%D8%B5%D9%89'
name= '434'



from  urllib import request  as rq
dwn_link = url

file_name = 'video/video' 
rq.urlretrieve(dwn_link, file_name)






# video = "https://www.youtube.com/watch?v=PEofA7Z8e_Q"
"""
now let's use pytube function names youtube
"""
# youtube = pytube.YouTube(video)

"""
now let's choose the format in this example we will use the first format
"""

# video = youtube.streams.first()

"""
after that specify the location where you want to store it  
"""

# video.download(r'C:\Users\samo\Downloads\Video\Recycleview')

"""
it may take same time to download
"""

"""
How to get video information ?
# open python shell 
from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=d3D7Y_ycSms')
video.title
output : u'Tom y Jerry en Espa\xf1ol | Ho Ho Horrors  + Jolly Friends Pet Oasis  | Dibujos animados para ni\xf1os'
c= video.video_id
output : 'PxrnoGyBw4E'
video.age_restricted
output : False
"""


"""
How to get video stream formats?

# open python shell
from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=PxrnoGyBw4E')
video.streams.all()
output : [
<Stream: itag="43" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp8.0" acodec="vorbis">,
 <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">, 
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e">,
 <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9">, 
 <Stream: itag="396" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08">, 
 <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015">, 
 <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9">, 
 <Stream: itag="395" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08">, 
 <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c">, 
 <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9">, 
 <Stream: itag="394" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08">, 
 <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">, 
 <Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">, 
 <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">, 
 <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">, 
 <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">
 ]
 
 
stream = video.streams.all()
for i in stream:
  print(i)
# press enter
<Stream: itag="43" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp8.0" acodec="vorbis">
<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">
<Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e">
<Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9">
<Stream: itag="396" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08">
<Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015">
<Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9">
<Stream: itag="395" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08">
<Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c">
<Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9">
<Stream: itag="394" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.05M.08">
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">
<Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">
<Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">
<Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">
<Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">
"""


"""
How to change Stream format?

Select any one itag from stream format (here we have selected ‘134', see above code).

video.streams.get_by_itag(134).download("/home/jay/Downloads")
"""

