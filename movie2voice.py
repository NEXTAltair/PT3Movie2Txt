#音声だけWAVで取り出す
#tsを直にwavにすると変換はできているがエラーを吐いて処理が止まる
#tsはmp4にエンコしてから変換
#ゴミ箱にあるファイルを参照してエラーで止まる
#temp_fileが重複してると上書きするか聞かれるのですスキップ
import os
import ffmpeg

# 変換元のフォルダ
src_folder = "L:"

# 変換先のフォルダ
dst_folder = "wav"

# 変換したいファイルの拡張子
ext = ('.m4v', '.ts', '.mp3', '.mp4')

# 変換元のフォルダ内のファイルをサブフォルダ含めて検索
for root, dirs, files in os.walk(src_folder):
    #ゴミ箱にあるファイルをスキップする処理
    if '$RECYCLE.BIN' in root:
        #continueはスキップして処理を続ける｡ breakだと処理が終わる
        continue
    for file in files:
        if file.endswith(ext):
            input_file = os.path.join(root, file)
            # ffmpegを使用して音声のみを抽出しwavへ変換するファイルの作成
            output_file = os.path.join(dst_folder, os.path.splitext(file)[0]+".wav")
            #tsは先にmp4へ変換処理
            if file.endswith('.ts'):
                temp_file = os.path.join(root, os.path.splitext(file)[0]+".mp4")
                # 同名のmp4が存在する場合はスキップ
                if os.path.exists(output_file):
                    print(output_file + "はmp4へ変換済み")
                    continue
                print("tsからmp4へ変換")
                #コマンドライン引数の場合は ｢-vcodec h264_nvenc｣ だが､モジュールから呼び出して引数渡す場合
                #｢, オプション = '引数'｣ 例:｢, vcodec='h264_nvenc'｣
                # h264_nvenc はRTXを使ったハードウェアエンコードで速いらしい
                ffmpeg.input(input_file).output(temp_file, vcodec='h264_nvenc').run()
                input_file = temp_file
            # 同名のwavが存在する場合はスキップ
            if os.path.exists(output_file):
                print(output_file + "はwavへ変換済み")
                continue
            print("mp4からwavへ変換")
            #output_fileの中身に音声だけをwavエンコードして書き込み
            ffmpeg.input(input_file).output(output_file, vcodec='none').run()