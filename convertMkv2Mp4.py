import ffmpeg
#pip install ffmpeg-python
def convert_mkv_to_mp4(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file, vcodec='copy', acodec='copy').run()
        print(f"Successfully converted {input_file} to {output_file}")
    except ffmpeg.Error as e:
        print(f"Error converting file: {e}")

# 让用户输入视频的名称
input_file = input("请输入要转换的MKV视频文件名（包括扩展名，例如：video.mkv）: ")
output_file = input("请输入输出的MP4视频文件名（包括扩展名，例如：video.mp4）: ")

convert_mkv_to_mp4(input_file, output_file)
