# 🎬 AI Ambient Video Automator

A professional Python-based automation tool designed to create high-quality, long-form ambient videos (1 hour+) for YouTube. Perfect for creators of "Study with Me," Cyberpunk, and Nature soundscape content.

## 🚀 Overview
This project automates the tedious manual workflow of looping short AI-generated clips (from Kling, Luma, or Leonardo) and layering complex audio environments. It transforms a 5-second video "seed" into a fully-functional 4K ambient experience with just a few clicks.

## ✨ Key Features
* **Interactive File Selection:** Built-in GUI using `tkinter` allows you to select source videos and multiple audio tracks without touching the code.
* **Dynamic Multi-Track Mixing:** Automatically blends any number of audio sources (e.g., fire crackling + rain + lo-fi music) with balanced volume levels using FFmpeg's `amix` filter.
* **Smart Looping Logic:** Seamlessly repeats video and audio streams to match your target duration (default is 60 minutes).
* **Zero Quality Loss:** Utilizes stream copying (`-c:v copy`) to ensure the original AI-generated visual quality is preserved while keeping rendering times ultra-fast.
* **Error Handling & Logging:** Robust Python backend with professional logging and user-friendly error messages.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Engine:** [FFmpeg](https://ffmpeg.org/) (The industry standard for video processing)
* **GUI:** Tkinter (Standard Python interface)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/syntax-error-dev/VideoConverter.git](https://github.com/syntax-error-dev/VideoConverter.git)
Install FFmpeg: Make sure FFmpeg is installed and added to your System PATH.

Configure Path: Open main.py and update the ffmpeg_path variable to point to your ffmpeg.exe location (e.g., D:\Progr\ffmpeg\bin\ffmpeg.exe).

🖥 How to Use
Run the script:

Bash

python main.py
Select Video: An explorer window will pop up. Select your short AI-generated video.

Select Audio: Select one or multiple audio files (hold Ctrl to select several).

Relax: The script will mix the audio and generate your 1-hour final video automatically.