from fileinput import filename
import subprocess
import argparse
import pathlib
import os
from random import choice
from glob import glob
# subprocess.run(["ffmpeg", "-ss", "00:01:00", "-to", "00:02:00",  "-i", "Microtomography_team.mp4", "-c", "copy", "output.mp4"]) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('dataset', 
                        metavar='D', 
                        type=str, 
                        help='Path to sequences')
    parser.add_argument('--start',
                        metavar="s",
                        # required=False,
                        default="00:10:00.00",  
                        type=str,
                        help='start of the video, in format HH:MM:SS.m')
    parser.add_argument('--finish', 
                        metavar="f",
                        # required=False,
                        default="00:10:00.300",
                        type=str,
                        help='end of the video, in format HH:MM:SS.m')
    parser.add_argument('output', type=str, help="output folder")
    args = parser.parse_args()

    path = args.dataset
    for dir in os.scandir(path):
        if not dir.name.startswith('.') and dir.is_dir():
            # print("len", len(glob(os.path.join(dir.path, choice(os.listdir(dir.path)), "smartphone_video_frames", "*.mp4"))), glob(os.path.join(dir.path, choice(os.listdir(dir.path)), "smartphone_video_frames", "*.mp4")))
            vid_path = glob(os.path.join(dir.path, choice(os.listdir(dir.path)), "smartphone_video_frames", "*.mp4"))
            # print("len", len(vid_path), vid_path[0])
            file_name = dir.name +"_" +os.path.basename(vid_path)
            write_path = os.path.join(args.output, file_name)
            subprocess.run(["ffmpeg", "-ss", args.start, "-to", args.finish,  "-i", vid_path, "-c", "copy", write_path])