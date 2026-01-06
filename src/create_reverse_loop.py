import os
import subprocess


def create_reverse_loop(input_video, output_video):
    reverse_video = "temp_reverse.mp4"

    try:
        reverse_cmd = [
            r'D:\Progr\Libs\ffmpeg\bin\ffmpeg.exe', '-y',
            '-i', input_video,
            '-vf', 'reverse',
            '-af', 'areverse',
            reverse_video
        ]
        subprocess.run(reverse_cmd, check=True)

        with open("concat_list.txt", "w") as f:
            f.write(f"file '{input_video}'\n")
            f.write(f"file '{reverse_video}'\n")

        concat_cmd = [
            r'D:\Progr\Libs\ffmpeg\bin\ffmpeg.exe', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', 'concat_list.txt',
            '-c', 'copy',
            output_video
        ]
        subprocess.run(concat_cmd, check=True)

    finally:
        if os.path.exists(reverse_video):
            os.remove(reverse_video)
        if os.path.exists("concat_list.txt"):
            os.remove("concat_list.txt")


input_file = "hailuo-2_3_Cyberpunk_room_window_view_on_a_rainy_futuristic_city_neon_lights_high_detail_4k-0.mp4"
output_file = "seamless_loop_cyberpunk.mp4"

create_reverse_loop(input_file, output_file)