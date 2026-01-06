import subprocess

def build_final_video(video_input, audio_input, output_name, duration_minutes=60):
    hours = duration_minutes // 60
    minutes = duration_minutes % 60
    time_str = f"{hours:02d}:{minutes:02d}:00"

    print(f"Начинаю сборку видео длительностью {time_str}...")

    cmd = [
        r'D:\Progr\Libs\ffmpeg\bin\ffmpeg.exe', '-y',
        '-stream_loop', '-1', '-i', video_input,
        '-stream_loop', '-1', '-i', audio_input,
        '-t', time_str,
        '-vf', 'scale=1920:1080:flags=lanczos',
        # or 'scale=3840:2160:flags=lanczos' for 4K
        '-map', '0:v', '-map', '1:a',
        '-c:v', 'libx264',
        '-preset', 'slow',
        '-crf', '18',
        '-c:a', 'aac',
        '-b:a', '192k',
        output_name
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"--- Успех! Видео готово: {output_name} ---")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при сборке: {e}")


# Твои файлы:
input_v = "seamless_loop_cyberpunk.mp4"
input_a = "background_mix.mp3"
output = "CYBERPUNK_NIGHT_1HOUR.mp4"

build_final_video(input_v, input_a, output, duration_minutes=60)