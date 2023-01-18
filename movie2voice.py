#音声だけを取り出す
#tsはmp4にエンコしてから変換
#tsを直にwavにすると変換はできているがエラーを吐いて処理が止まる
#ゴミ箱にあるファイルを参照してエラーで止まる
#temp_fileが重複してると上書きするか聞かれるのですスキップ
import os
import ffmpeg

# 変換元のフォルダ
src_folder = "TestFile"

# 変換先のフォルダ
dst_folder = "wav"

# 変換したいファイルの拡張子
ext = ('.m4v', '.ts', '.mp3', '.mp4')

# 変換元のフォルダ内のファイルを検索
for root, dirs, files in os.walk(src_folder):
    #ゴミ箱にあるファイルをスキップする処理
    if '$RECYCLE.BIN' in root:
        continue
    for file in files:
        if file.endswith(ext):
            input_file = os.path.join(root, file)
            # ffmpegを使用して音声のみを抽出しwavへ変換するファイルの作成
            output_file = os.path.join(dst_folder, os.path.splitext(file)[0]+".wav")
            #tsは先にmp4へ変換処理
            if file.endswith('.ts'):
                temp_file = os.path.join(root, os.path.splitext(file)[0]+".mp4")
                # 同名の.mp4が存在する場合はスキップ
                if os.path.exists(output_file):
                    print(output_file + "は変換済み")
                    continue
                ffmpeg.input(input_file).output(temp_file).run()
                input_file = temp_file
            # 同名の.wavが存在する場合はスキップ
            if os.path.exists(output_file):
                print(output_file + "は変換済み")
                continue
            #output_fileの中身に音声だけをエンコードして書き込み
            ffmpeg.input(input_file).output(output_file, acodec='pcm_s16le', vcodec='none').run()