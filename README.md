# VIDEO-TRANSCODER

This script will look for all files with .mp4 or .mkv extension in the directory passed in and transcode them using codec specified in the codec variable,
and then save them in the same directory with "transcoded_" prefixing the original filename.

The script uses the os.listdir() function to get a list of all files in the directory,
subprocess.run() function to execute ffmpeg command. The -i flag specifies the input file, the -c:v flag specifies the codec to use for the video.

Please note that this script will overwrite the original videos. If you want to keep the original videos
and save the transcoded videos with new names, you can modify the script accordingly.
Also, you need to have FFmpeg installed on your machine to run this script. If you don't have it,
you can install it by following instructions on ffmpeg website.
