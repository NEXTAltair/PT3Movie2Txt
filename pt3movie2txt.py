#wavをwhisperでTXTにするやつ
import os
import glob
import whisper

#モデルロード最新版 #GPT3いわくaudio_path前にしないと処理が遅くならしい
model = whisper.load_model("large-v2")

# 変換元のフォルダ
wav_folder = "wav"

# 変換先のフォルダ
output_folder = "wtxt"

#変換元ファイル
audio_path = glob.glob(os.path.join(wav_folder, "*.wav"))

#model.transcribeはリストでファイルをは受け付けないのでforが必要
for audio_file in audio_path:
    # 出力処理ファイルの準備
    output_file = os.path.join(output_folder, os.path.basename(audio_file).replace(".wav", ".txt"))
    #文字起こしでverbose=True時間ごとの進捗をターミナルに表示
    result = model.transcribe(audio=audio_file, verbose=True, language="ja")
    #, encoding='utf-8'と, ensure_ascii=False忘れると文字コードしか出ない
    with open(output_file, "w", encoding='utf-8') as f:    
        f.write(result["text"])
        #txtに保存された内容をコンソールに表示
        print(result["text"])