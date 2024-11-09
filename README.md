# YouTube Video Transcription and Translation Pipeline

This Python-based pipeline extracts audio from Creative Commons licensed Telugu YouTube videos, transcribes speech to text, and translates the transcriptions into English. The results are saved into an Excel file for further analysis. The project uses YouTube Data API, Google Speech Recognition, and the Deep Translator API.

## Features
- **Search for Creative Commons Telugu Videos**: Uses the YouTube Data API to search for Telugu videos based on a user-defined query.
- **Audio Extraction**: Downloads the videos as audio files in `.wav` format using `yt-dlp`.
- **Speech Recognition**: Converts audio to text using Google’s Speech-to-Text API.
- **Translation**: Translates transcribed text into English using the `deep-translator` library.
- **Results Output**: Saves video details (ID, transcription, translation) in an Excel file (`foodlinks08.ods`).

## Requirements

Before running the script, ensure you have the following Python packages installed:

```bash
pip install pandas google-api-python-client speechrecognition deep-translator nltk yt-dlp
```

You'll also need a valid YouTube Data API key, which you can obtain from the [Google Developers Console](https://console.developers.google.com/).

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/YouTube-Video-Transcription-Translation.git
   cd YouTube-Video-Transcription-Translation
   ```

2. Replace the `DEVELOPER_KEY` variable in the script with your actual YouTube Data API key.

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script by executing the following command:

```bash
python youtube_transcription_translation.py
```

This will:
- Search for Telugu videos related to the query `telugu food` (you can customize this).
- Download the audio from the videos.
- Transcribe the audio and translate the text into English.
- Save the results in an Excel file (`foodlinks08.ods`).

### Example Output

The script will generate an Excel file with the following columns:
- **SI.No**: Serial number of the video.
- **Video ID**: The unique ID of the YouTube video.
- **Transcription**: The transcribed text from the video.
- **Translation**: The English translation of the transcribed text.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this repository and submit pull requests if you want to add features or improvements!

## Acknowledgments

- [Google API Client](https://pypi.org/project/google-api-python-client/) for accessing the YouTube API.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for audio transcription.
- [Deep Translator](https://pypi.org/project/deep-translator/) for translating text.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading videos.

---

This `README.md` file includes all the essential information for someone to understand the purpose of the project, set it up, and use it. You can add more specific instructions or modify details according to your project needs. Let me know if you need any changes!
