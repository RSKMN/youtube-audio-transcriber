#import required packages
import pandas as pd
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import subprocess
import speech_recognition as sr
from deep_translator import GoogleTranslator
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')


# Set your API key here
DEVELOPER_KEY = 'API-KEY'  # Replace with your actual API key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Build the YouTube API client
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)



# def is_less_than_4_minutes(duration):
#     # """Check if the video duration is less than 4 minutes."""
#     # Duration is in ISO 8601 format (e.g., PT2M30S)
#     if duration.startswith('PT'):
#         minutes = int(duration[2:duration.index('M')]) if 'M' in duration else 0
#         return minutes < 4
#     return False

# Function to search for Telugu videos with Creative Commons license
def youtube_search(query='telugu food', max_results=2):
    try:
        # Make the search request
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results,
            videoLicense='creativeCommon',  # Filter for Creative Commons videos
            videoDuration='short'
        ).execute()
        
        # Collect results
        results = []
        i=0
        r = sr.Recognizer()
        for video in search_response.get('items', []):
            i=i+1
            video_id = video['id']['videoId']
            
            url = f"https://www.youtube.com/watch?v={video_id}"
            custom_file_name = f"{i}.wav"
            subprocess.run(["yt-dlp", "-x", "--audio-format", "wav", "-o", custom_file_name , url])

            audio = sr.AudioFile(custom_file_name)
            duration = len(audio.frame_data) / audio.sample_rate
            num_segments = int(duration // 60) + 1
            for j in range(num_segments):
                start_time = j * 60  # Start time in seconds
                end_time = min((j + 1) * 60, duration)  # End time in seconds

    # Create a new audio segment
                segment_data = audio[start_time:end_time]
                
                with segment_data as source:
                    segment_data = r.record(source)                  
                    result = result + " "+ r.recognize_google(segment_data, language="te-IN")
                    

                
                translation = word_tokenize(result)
                


                results.append({
                'SI.No': i,
                'Video ID': video_id,
                'Transcription': translation
                })

        print("Results collected:", results)


        # Convert results to DataFrame
        df = pd.DataFrame(results)
        df.to_excel('foodlinks08.ods', index=False)
        # Save to Excel
        # df.to_excel('food_links_08.ods', index=False)

        print("Search results saved to 'foodlinks08.ods'.")

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")


youtube_search()


#Downloading .wav from excell

