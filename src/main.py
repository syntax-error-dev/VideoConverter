import subprocess
import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class AmbientVideoCreator:
    def __init__(self, ffmpeg_path=r'D:\Progr\ffmpeg\bin\ffmpeg.exe'):
        self.ffmpeg_path = ffmpeg_path
        if not os.path.exists(self.ffmpeg_path):
            logging.error(f"FFmpeg не найден по пути: {self.ffmpeg_path}")
            messagebox.showerror("Ошибка", f"FFmpeg не найден!\nПроверьте путь: {self.ffmpeg_path}")
            raise FileNotFoundError("FFmpeg executable not found.")

    def select_assets(self):
        """Интерактивный выбор файлов через системное окно."""
        root = tk.Tk()
        root.withdraw()

        logging.info("Ожидание выбора файлов пользователем...")

        video_v = filedialog.askopenfilename(
            title="1. Выберите видео-исходник (5-10 сек)",
            filetypes=[("Video files", "*.mp4 *.mov *.mkv")]
        )
        if not video_v: return None, None

        audio_a = filedialog.askopenfilenames(
            title="2. Выберите аудио-файлы (все, что нужно смешать)",
            filetypes=[("Audio files", "*.mp3 *.wav *.aac")]
        )

        return video_v, list(audio_a)

    def mix_audio(self, audio_files, output_audio="temp_mixed_bg.mp3"):
        """Смешивает любое кол-во аудио в одну дорожку."""
        if not audio_files:
            return None

        logging.info(f"Начинаю микширование {len(audio_files)} дорожек...")
        inputs = []
        for f in audio_files:
            inputs.extend(['-i', f])

        # Фильтр amix: смешивает потоки, duration=longest делает длину по самому длинному треку
        filter_complex = f"amix=inputs={len(audio_files)}:duration=longest"

        cmd = [
                  self.ffmpeg_path, '-y'
              ] + inputs + [
                  '-filter_complex', filter_complex,
                  '-c:a', 'libmp3lame', '-q:a', '2', output_audio
              ]

        subprocess.run(cmd, check=True, capture_output=True)
        return output_audio

    def build_final(self, video_in, audio_in, output_name, duration_min=60):
        """Собирает финальный часовой ролик с зацикливанием."""
        time_str = f"{duration_min // 60:02d}:{duration_min % 60:02d}:00"
        logging.info(f"Сборка финального видео: {output_name} ({duration_min} мин)")

        cmd = [
            self.ffmpeg_path, '-y',
            '-stream_loop', '-1', '-i', video_in,
            '-stream_loop', '-1', '-i', audio_in,
            '-t', time_str,
            '-map', '0:v', '-map', '1:a',
            '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
            output_name
        ]

        try:
            subprocess.run(cmd, check=True)
            logging.info("Рендеринг успешно завершен!")
            messagebox.showinfo("Готово", f"Видео сохранено как:\n{output_name}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Ошибка при сборке: {e}")


if __name__ == "__main__":
    creator = AmbientVideoCreator()

    try:
        # 1. Выбираем файлы
        video_src, audio_sources = creator.select_assets()

        if video_src and audio_sources:
            # 2. Смешиваем аудио
            final_audio = creator.mix_audio(audio_sources)

            # 3. Собираем финал (для теста поставил 60 мин, можно менять)
            creator.build_final(video_src, final_audio, "FINAL_YOUTUBE_VIDEO.mp4", duration_min=60)
        else:
            logging.warning("Файлы не выбраны. Выход.")

    except Exception as e:
        logging.critical(f"Произошла непредвиденная ошибка: {e}")