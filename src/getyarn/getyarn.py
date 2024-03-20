from __future__ import annotations

import requests
from bs4 import BeautifulSoup as bs
from moviepy.editor import VideoFileClip, concatenate_videoclips


def get_yarn(url) -> tuple[bytes, str]:
    response = requests.get(url)
    soup = bs(response.content, "html.parser")
    source = soup.find("source").get("src")
    if not source:
        msg = "No source found"
        raise ValueError(msg)
    if not source.endswith(".mp4"):
        msg = "Source is not a video"
        raise ValueError(msg)
    mp4 = get_video_source(source)

    next_clip = soup.find("a", title="Next Clip").get("href")
    if not next_clip:
        msg = "No next clip found"
        raise ValueError(msg)

    print(next_clip)

    return mp4, next_clip


def get_video_source(url) -> bytes:
    response = requests.get(url)
    response.raise_for_status()
    return response.content


concatenate_videoclips([]).write_videofile("output.mp4")

if __name__ == "__main__":
    url = "https://getyarn.io/yarn-clip/4b6e7f8e-5e5e-4b3e-8f8e-7e4b5e5e3e8f"
    get_yarn(url)
