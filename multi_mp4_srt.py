import sys
import subprocess
import os
from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

# 输入视频名称，生成对应名称的 mp3 文件
def video_to_mp3(video_path):
    # 获取输入视频的文件名（不包括扩展名）
    base_name = os.path.splitext(os.path.basename(video_path))[0]

    # 设置输出的 MP3 文件名为输入视频的文件名 + ".mp3"
    audio_path = base_name + '.mp3'

    # 从视频中提取音频并保存为 MP3
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    # 返回生成的 MP3 文件路径
    return audio_path

def mp3_to_srt(audio_path):
    # 使用 Whisper 将 MP3 转换为 SRT 字幕
    subprocess.run(["whisper", audio_path, "--output_format", "srt"])

def add_subtitles_to_video(video_path, subtitles_path, output_path):
    # 加载视频
    video = VideoFileClip(video_path)

    # 生成字幕
    subtitles = SubtitlesClip(subtitles_path)

    # 将字幕设置在视频底部
    subtitles = subtitles.set_position(('center','bottom')).set_duration(video.duration)

    # 组合视频和字幕
    final_video = CompositeVideoClip([video, subtitles])

    # 导出视频
    final_video.write_videofile(output_path, codec='libx264', fps=video.fps)

def generate_subtitles(video_path):
    # 获取输入视频的文件名（不包括扩展名）
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    srt_path = base_name + '.srt'
    output_video_path = base_name + '_srt.mp4'

    # 检查是否存在字幕文件
    if not os.path.isfile(srt_path):
        # 生成字幕文件
        audio_path = video_to_mp3(video_path)
        mp3_to_srt(audio_path)
        os.remove(audio_path)  # 清理临时音频文件

    # 添加字幕到视频
    add_subtitles_to_video(video_path, srt_path, output_video_path)

def process_all_mp4_files_in_directory(directory):
    # 获取目录下所有的 mp4 文件
    mp4_files = [f for f in os.listdir(directory) if f.endswith(".mp4")]

    for mp4_file in mp4_files:
        video_path = os.path.join(directory, mp4_file)
        generate_subtitles(video_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mp42srt.py <video_path_or_directory>")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isdir(path):
        # 如果输入是一个目录，则处理目录下的所有 mp4 文件
        process_all_mp4_files_in_directory(path)
    elif os.path.isfile(path) and path.endswith(".mp4"):
        # 如果输入是一个单个 mp4 文件，则处理该文件
        generate_subtitles(path)
    else:
        print("Invalid input. Please provide either a single mp4 file or a directory containing mp4 files.")
