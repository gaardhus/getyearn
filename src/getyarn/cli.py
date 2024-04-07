# TODO:
# - Add clipping time range option

from __future__ import annotations

import argparse
import os

from moviepy.editor import concatenate_videoclips

from .getyarn import get_yarn


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Get and merge video clips from https://getyarn.io/"
    )
    parser.add_argument("url", nargs="*", help="Yarn URLs")
    parser.add_argument("output", type=str, help="Output file")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="~/Videos/clips/",
        help="Output directory",
    )
    parser.add_argument(
        "--next-clips",
        type=int,
        default=0,
        help="Number of next clips to download and merge",
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["chain", "compose"],
        default="chain",
        help="Method to merge clips",
    )  # NOTE: Should the method be automatically determined based multiple URLs vs next-clips?
    return parser.parse_args()


def main():
    args = parse_args()

    clips = []

    for url in args.url:
        main_clip, next_clip = get_yarn(url)
        clips.append(main_clip)

        for _ in range(args.next_clips):
            sub_clip, next_clip = get_yarn(next_clip)
            clips.append(sub_clip)

    merged_clip = concatenate_videoclips(clips, method=args.method)

    out_file = os.path.expanduser(os.path.join(args.output_dir, args.output))
    merged_clip.write_videofile(out_file)


if __name__ == "__main__":
    main()
