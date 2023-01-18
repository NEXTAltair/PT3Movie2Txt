#wavをwhisperでtxtにするやつ
import os
import glob
import whisper
import json

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
    # 同名の.txtが存在する場合はスキップ
    if os.path.exists(output_file):
        print(output_file + "は変換済み")
        continue
    #文字起こし
    result = model.transcribe(audio=audio_file, verbose=True, language="ja")
    #resultはdict(辞書)型なのでjsonモジュールのjson.dumpでstr(文字列)型に変換
    transcribed_text = json.dumps(result)
    #, encoding='utf-8'忘れると文字コードしか出ない
    with open(output_file, "w", encoding='utf-8') as f:
        #result内ではsegmentsで分割されてるのでその中からidとtextを取り出して一行ずつtxtに保存
        for segment in result["segments"]:
            f.write(f"id:{segment['id']} {segment['text']}\n")