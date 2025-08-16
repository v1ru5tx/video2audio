from moviepy import VideoFileClip

def main():
    ruta_video = "./video.mp4"
    ruta_audio = "./audio.wav"

    video = VideoFileClip(ruta_video)
    audio = video.audio

    audio.write_audiofile(ruta_audio)

    video.close()
    audio.close()
    

if __name__ == "__main__":
    main()
