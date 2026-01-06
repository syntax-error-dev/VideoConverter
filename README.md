# AI Video Automator 🎬 🤖

A Python-based automation tool for creating seamless high-quality ambient videos for YouTube (Cyberpunk, Lofi, Nature).

## Features
- **Seamless Looping:** Creates ping-pong loops for short AI-generated clips.
- **Audio Mixing:** Blends multiple audio tracks (rain, fire, music) using FFmpeg's `amix`.
- **Final Assembly:** Automatically cycles video to match any duration (up to 1 hour+).

## Requirements
- Python 3.10+
- [FFmpeg](https://ffmpeg.org/) installed and added to PATH.

## Usage
1. Place your AI-generated 5s clip in the folder.
2. Run `python src/main.py`.
3. Get your 1-hour ready-to-upload YouTube video.