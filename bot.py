from dotenv import load_dotenv
import os
from google import generativeai as gen_ai
import pyttsx3
import random
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from upload import upload
from time import sleep



YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel('gemini-pro')

videos = ["sample_videos"]

prompts = [
    "Sample Prompts"
]



def get_story():
    try:
        prompt = random.choice(prompts)
        output = model.generate_content(prompt)
        return output.text[:900]
    except ValueError as e:
        return output.text


def get_audio(prompt_title,video):
    mytext = get_story()
    engine = pyttsx3.init()   
    engine.setProperty('rate', 150) 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    file_name = f"{prompt_title}.mp3"
    engine.save_to_file(mytext, file_name)
    engine.runAndWait()
    video_clip = VideoFileClip(video)
    audio_clip = AudioFileClip(file_name)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(f"{prompt_title}.mp4")


def main():
    for _ in range(3):
        prompt_title = random.choice(prompts).split(":")[0]  
        video = random.choice(videos)
        get_audio(prompt_title, video)
        video_path = f"{prompt_title}.mp4"
        title = prompt_title
        description = f"{prompt_title} #shorts #Story #Adventure #Mystery #random #stories #newworld #askreddit #newask #ask more "
        metadata = {
            "title": title,
            "description": description,
            "tags": ["shorts","random","stories","new","askreddit","stories","randomstoires"]
    }
        if upload(video_path,metadata):
      
            # os.remove(video_path)
            os.remove(f"{prompt_title}.mp3")
        else:
            print("Failed to upload video. Video file will not be deleted.")
        sleep(18000)



if __name__ == "__main__":
    main()
