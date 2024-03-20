from __future__ import annotations

import tempfile

import requests
from bs4 import BeautifulSoup as bs
from moviepy.editor import VideoFileClip

# TODO: Replace moviepy with ffmpeg

DOMAIN = "https://getyarn.io"
TMP_DIR = tempfile.gettempdir()


def get_yarn(url) -> tuple[VideoFileClip, str]:
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

    next_clip = DOMAIN + soup.find("a", title="Next Clip").get("href")
    if not next_clip:
        msg = "No next clip found"
        raise ValueError(msg)

    return mp4, next_clip


def get_video_source(url) -> VideoFileClip:
    response = requests.get(url)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(suffix=".mp4", dir=TMP_DIR, delete=False) as f:
        f.write(response.content)
        return VideoFileClip(f.name)
