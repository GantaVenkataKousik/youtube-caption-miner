# YouTube Caption Miner
Overview
YouTube Caption Miner is a Python-based tool for extracting and mining captions/subtitles from YouTube videos. It automates the process of scraping, processing, and saving subtitles, making it easier for users to analyze or reuse video captions.

### Features
Scraping Captions: Extracts captions/subtitles from YouTube videos via web scraping.
JSON Output: Stores extracted subtitles in a structured yt-subtitles.json file.
Multiple Formats: Supports processing subtitles in different languages and formats.

### Custom Scripts:
chatgpt.py: A script for interacting with captions using a model like ChatGPT for further analysis or insights.
scraping-youtube.py: A script to scrape and retrieve video captions from YouTube.
video-subtitles.py: A script to handle and manage the subtitles once scraped.
Files Included
chatgpt.py: Script to interact with the captions and derive insights.
scraping-youtube.py: Main script for scraping YouTube captions.
video-subtitles.py: Script to process and manage extracted captions.
yt-subtitles.json: JSON file where the scraped subtitles are saved.

### How to Use
### Clone the repository:

git clone https://github.com/GantaVenkataKousik/youtube-caption-miner.git
<br>
Install the required dependencies:

pip install -r requirements.txt
<br>
Run the scraping script to extract captions from a YouTube video:

python scraping-youtube.py <YouTube Video URL><br>
Process and analyze the scraped captions using video-subtitles.py or interact with it using the chatgpt.py script.
