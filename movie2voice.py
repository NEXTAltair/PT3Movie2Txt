#音声だけを取り出す
import os
import ffmpeg

# 変換元のフォルダ
src_folder = "TestFile"

# 変換先のフォルダ
dst_folder = "wav"

# 変換したいファイルの拡張子
ext = ('.m4v', '.ts', '.mp3', '.mp4')

# 変換元のフォルダ内のファイルを検索
for file in os.scandir(src_folder):
    if file.is_file() and file.name.endswith(ext):
        input_file = file.path
        output_file = os.path.join(dst_folder, os.path.splitext(file.name)[0]+".wav")
        # ffmpegを使用して音声のみを抽出し、変換
        ffmpeg.input(input_file).output(output_file, acodec='pcm_s16le', vcodec='none').run()