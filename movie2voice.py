import os
import ffmpeg
# 変換するファイルパス
folder = "./TestFile"

# 変換したいファイル (e.g. mp3, flac, etc.)
ext = ".ts"

for filename in os.listdir(folder):
    if filename.endswith(ext):
        input_file = os.path.join(folder, filename)
        output_file = os.path.join(folder, os.path.splitext(filename)[0]+".wav")
        # use ffmpeg-python to convert the file
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream)