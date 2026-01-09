# 🎬 AI Ambient Video Automator

A professional Python-based automation tool designed to create high-quality, long-duration (1 hour+) ambient videos for YouTube. Perfect for "Study with Me," Cyberpunk, and Nature soundscape channels.

## 🚀 Overview
This tool automates the tedious process of manual video editing for ambient channels. It takes short AI-generated clips (from Luma, Kling, or Leonardo) and transforms them into seamless, long-form content with layered audio.

## ✨ Key Features
* **OOP Architecture**: Built with clean, maintainable Python classes.
* **Multi-Track Audio Mixing**: Dynamically blends an unlimited number of audio sources (e.g., rain + fire + lo-fi music) using FFmpeg's `amix` filter.
* **Seamless Ping-Pong Loop**: Automatically generates a forward-reverse loop to eliminate visible cuts in short clips.
* **Resource Efficient**: Uses stream copying (`-c:v copy`) whenever possible to ensure fast rendering without quality loss.
* **Robust Logging**: Includes a professional logging system for debugging and tracking progress.

## 🛠 Prerequisites
* **Python 3.10+**
* **FFmpeg**: Must be installed and accessible via System PATH.

## 📦 Installation & Usage
1.  Clone the repository:
    ```bash
    git clone [https://github.com/syntax-error-dev/VideoConverter.git](https://github.com/syntax-error-dev/VideoConverter.git)
    ```
2.  Configure your `ffmpeg_path` in `main.py`.
3.  Place your source video and audio files in the project directory.
4.  Run the script:
    ```bash
    python src/main.py
    ```

## 🗺 Roadmap
- [ ] Auto-scan directory for media files.
- [ ] Add 4K Upscaling integration.
- [ ] Develop a simple GUI for non-technical users.
- [ ] Support for YouTube API uploads.

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.