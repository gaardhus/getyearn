from __future__ import annotations

import argparse

from moviepy.editor import concatenate_videoclips

from .getyarn import get_yarn


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Get and merge video clips from https://getyarn.io/")
    parser.add_argument("url", help="Yarn URL")
    parser.add_argument("output", type=str, help="Output file")
    parser.add_argument(
        "--next-clips", type=int, default=0, help="Number of next clips to download and merge"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    main_clip, next_clip = get_yarn(args.url)

    clips = [main_clip]

    for _ in range(args.next_clips):
        sub_clip, next_clip = get_yarn(next_clip)
        clips.append(sub_clip)

    merged_clip = concatenate_videoclips(clips)

    merged_clip.write_videofile(args.output)


if __name__ == "__main__":
    main()
