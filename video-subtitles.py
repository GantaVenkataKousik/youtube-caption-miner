from youtube_transcript_api import YouTubeTranscriptApi 
import os
import json

srt = YouTubeTranscriptApi.get_transcript("SBmSRK3feww") 
text = ""
with open("file.txt", "w") as file:
    for i in srt:
        text += i["text"] + "," 
    file.write(text)

transcript_list=[]
    
for i in srt:
    # Replace newline characters with a space
    text = i["text"].replace("\n", " ")
    transcript_list.append(text)

# Create a dictionary to hold the transcript data
transcript_dict = {
    "yt-subtitles": transcript_list
}

# Define the file path for the JSON file
json_file_path = "yt-subtitles.json"

# Write the transcript data to the JSON file
with open(json_file_path, "w") as json_file:
    json.dump(transcript_dict, json_file, indent=4)
