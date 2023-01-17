import os
import subprocess

def transcode_videos(directory, codec):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".mkv"):
            input_file = f"{directory}/{filename}"
            output_file = f"{directory}/transcoded_{filename}"
            subprocess.run(["ffmpeg", "-i", input_file, "-c:v", codec, output_file])

directory = "/path/to/videos"
codec = "libx264"
transcode_videos(directory, codec)
