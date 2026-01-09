import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class AmbientVideoCreator:
    def __init__(self, ffmpeg_path=r'C:\ffmpeg\bin\ffmpeg.exe'):
        self.ffmpeg_path = ffmpeg_path
        if not os.path.exists(self.ffmpeg_path):
            raise FileNotFoundError(f"FFmpeg не найден по пути: {self.ffmpeg_path}")

    def mix_audio(self, audio_files, output_audio="temp_mixed_bg.mp3"):
        if not audio_files:
            raise ValueError("Список аудиофайлов пуст!")

        logging.info(f"Смешиваю {len(audio_files)} аудиофайла(ов)...")

        inputs = []
        for f in audio_files:
            if not os.path.exists(f):
                logging.warning(f"Файл {f} не найден, пропускаю.")
                continue
            inputs.extend(['-i', f])

        filter_complex = f"amix=inputs={len(inputs) // 2}:duration=longest"

        cmd = [self.ffmpeg_path, '-y'] + inputs + [
            '-filter_complex', filter_complex,
            '-c:a', 'libmp3lame', '-q:a', '2', output_audio
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            return output_audio
        except subprocess.CalledProcessError as e:
            logging.error(f"Ошибка FFmpeg при микшировании: {e.stderr.decode()}")
            raise

    def create_ping_pong_video(self, input_video, output_video="temp_ping_pong.mp4"):
        logging.info("Создаю ping-pong цикл для видео...")
        return output_video

    def build_final(self, video_loop, audio_mix, output_name, duration_min=60):
        time_str = f"{duration_min // 60:02d}:{duration_min % 60:02d}:00"
        logging.info(f"Сборка финального видео на {duration_min} минут...")

        cmd = [
            self.ffmpeg_path, '-y',
            '-stream_loop', '-1', '-i', video_loop,
            '-stream_loop', '-1', '-i', audio_mix,
            '-t', time_str,
            '-map', '0:v', '-map', '1:a',
            '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
            output_name
        ]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    creator = AmbientVideoCreator()

    try:
        audio_sources = ["rain.mp3", "forest.mp3", "music.mp3", "crickets.mp3"]

        mixed_audio = creator.mix_audio(audio_sources)
        logging.info("Все готово!")
    except Exception as e:
        logging.error(f"Критическая ошибка: {e}")