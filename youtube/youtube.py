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

def videos(channel, channels, main):
    video_util = scrapetube.get_channel(channel_username=channel, limit=50)
    video_md, video_names = [], []

    for video_data in video_util:
        video_md.append(video_data)

    video_md = video_md[:10]

    for video in video_md:
        video_names.append(video["title"]["runs"][0]["text"])
    video_names.append("")
    video_names.append("Back")
    terminal_menu = TerminalMenu(video_names, clear_screen=False, cycle_cursor=False, menu_cursor=None, skip_empty_entries=True)
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            video_id = get_video_id(video_md, video_names[menu_entry_index])
            if video_id == "Back":
                raise KeyboardInterrupt
            yt = YouTube(f'https://youtube.com/watch?v={video_id}')
            stream = yt.streams.first()
            description = yt.description
            newline_index = description.find('\n')
            print(format(description[:newline_index]))
            stream.download(filename="video.mp4",)
    except KeyboardInterrupt:
            channels()
    except Exception as e:
        print(e)

    menu_entry_index = terminal_menu.show()
    video_id = get_video_id(video_md, video_names[menu_entry_index])
    yt = YouTube(f'https://youtube.com/watch?v={video_id}')
    stream = yt.streams.first()
    description = yt.description
    newline_index = description.find('\n')
    print(format(description[:newline_index]))
    stream.download(filename="video.mp4",)
