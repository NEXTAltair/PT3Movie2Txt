# PT3Movie2Txt
## 録画ファイルとかをwhisperでドライブレターごと一気に文字起こしするやつ
録画ファイルをwavにするやつ
wavをtxtにするやつ
## ChatGPTとGoogleと初心者向け記事を書いてくれた人のおかげ
大量の録画ファイルを一気に処理してる最中なんで妙なバグがあるかもしれないが今のところ動く

# 導入の注意点
pip3 install git+https://github.com/openai/whisper.git
でインストールすると何故かtorchがcudaに対応していない

## コレで対応させられる(ハズ)
pip uninstall torch
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117

## ToDo
print("tsからmp4へ変換")とか表示の位置がなにかおかしい気がする