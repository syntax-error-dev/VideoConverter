import subprocess


def mix_audio_tracks(input_files, output_file):

    inputs = []
    for file in input_files:
        inputs.extend(['-i', file])

    filter_complex = f'amix=inputs={len(input_files)}:duration=longest'

    cmd = [
              r'D:\Progr\Libs\ffmpeg\bin\ffmpeg.exe', '-y'
          ] + inputs + [
              '-filter_complex', filter_complex,
              '-c:a', 'libmp3lame',
              '-q:a', '2',
              output_file
          ]

    subprocess.run(cmd, check=True)
    print(f"Аудио смешано! Файл: {output_file}")


my_tracks = ['50054__vibe_crc__rain_session_thunder_2006.wav', '651714__sounddesignforyou__rain-hitting-window-1.wav', '744001__rmshh__cyberpunk-rain-ambience-wind-and-raindrops-stem.wav']
mix_audio_tracks(my_tracks, 'background_mix.mp3')