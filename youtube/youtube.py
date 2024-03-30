import scrapetube
from simple_term_menu import TerminalMenu
from pytube import YouTube

def format(s, max_line_length=50):
    words = s.split()  # Split the string into words
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + word) <= max_line_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())  # Append the current line to the list of lines
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())  # Append the last line if it's not empty

    return '\n'.join(lines)

def get_video_id(video_dict, title_text):
    for video in video_dict:
        if video["title"]["runs"][0]["text"] == title_text:
            return video["videoId"]
    return None  # If the title text is not found in any video entry

video_util = scrapetube.get_channel("UCMiJRAwDNSNzuYeN2uWa0pA", limit=100)
video_md, video_names = [], []

for video_data in video_util:
    video_md.append(video_data)

video_md = video_md[:10]

for video in video_md:
    video_names.append(video["title"]["runs"][0]["text"])

terminal_menu = TerminalMenu(video_names, clear_screen=False, cycle_cursor=False, menu_cursor=None)
menu_entry_index = terminal_menu.show()
video_id = get_video_id(video_md, video_names[menu_entry_index])
yt = YouTube(f'https://youtube.com/watch?v={video_id}')
stream = yt.streams.first()
description = yt.description
newline_index = description.find('\n')
print(description[:newline_index])
stream.download(filename="video.mp4")