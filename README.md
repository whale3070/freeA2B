# freeA2B
[whale3070.github.io/tags/I-hate-VIP/](https://whale3070.github.io/tags/I-hate-VIP/)

视频处理： 1. 免费将avi转换mp4格式 

2.
使用whisper`自动给mp4视频添加字幕`。相关模块请自行安装，不要问我，我已经不记得安装了哪些模块了。
使用方法python3 mp4_srt.py xx.mp4

xx.mp4是没有字幕的版本。脚本运行后会生成srt字幕文件和已添加字幕的mp4视频。

使用方法
python3 multi_mp4_srt.py "windows文件夹的绝对路径，例如C:\Users\whale\Videos"

3. 
文档处理：免费将PDF转换PNG格式 
```
      文档处理需要模块和依赖，需要下载windows版本的poppler：https://blog.alivate.com.au/poppler-windows/
      以及安装模块：pip install pdf2image -i https://pypi.tuna.tsinghua.edu.cn/simple
      最后将https://blog.alivate.com.au/wp-content/uploads/2018/10/poppler-0.68.0_x86.7z 解压缩，将 C:\Users\whale\Desktop\poppler-0.68.0_x86\bin 这个绝对路径添加到windows环境变量
      不需要重启电脑，运行python脚本，即可进行转换
```

4. 
图片处理：免费将图片加上水印
