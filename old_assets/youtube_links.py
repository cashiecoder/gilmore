import subprocess

def extract_links(link):
    python_code = f"""
import youtube_dl

options = {{
    "quiet":    True,
    "simulate": True,
    "forceurl": True,
}}

with youtube_dl.YoutubeDL(options) as ytdl:
    info = ytdl.extract_info("{link}")
print(info.get('url', ''))  # Print video URL
print(info.get('url', ''))  # Print audio URL
"""

    # Run the Python code in a subprocess
    process = subprocess.Popen(['python', '-c', python_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output
    output, error = process.communicate()

    # Process the output
    link_data = output.splitlines() if output else []
    links = {"video": link_data[0] if link_data else "", "audio": link_data[1] if len(link_data) > 1 else ""}
    return links

yt = extract_links("https://www.youtube.com/watch?v=sMApF4h3fJw")
print("Video Link:", yt["video"])
print("Audio Link:", yt["audio"])
