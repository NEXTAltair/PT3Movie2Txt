# PT3Movie2Txt
## 録画ファイルとかをwhisperでドライブレターごと一気に文字起こしするやつ
録画ファイルをwavにするやつ
wavをtxtにするやつ
## ChatGPTとGoogleと初心者向け記事を書いてくれた人のおかげ
大量の録画ファイルを一気に処理してる最中なんで妙なバグがあるかもしれないが今のところ動く

# 導入の注意点
python 3.11では動かない  

`python -m venv venv`  
`python.exe -m pip install --upgrade pip`  
## whisperのreadmeに従ってインストールすると何故かtorchがcudaに対応していない
何故かではなくもともとwhisperはCPUで動かすのが前提っぽい?  
コレで対応させられる(ハズ)  

`pip install git+https://github.com/openai/whisper.git`  
`pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git`  
`pip uninstall torch`  
`pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117`  

## tsから字幕を抜き出すモジュール
`pip install git+https://github.com/reazon-research/reazonspeech`

https://github.com/iGlitch/Caption2Ass
許諾的に最終的にGPTに食わせようって考えてるから使えない

## .tsファイルのエンコード処理のために必要  
`pip install ffmpeg`  
# ToDo  
`print("tsからmp4へ変換")`とか表示の位置がなにかおかしい気がする  
tsからmp4にエンコード途中で止めると破損したmp4が残ってエラーで止まるのは別に手動で消せばいいか
依存関係に色々入りすぎてるのはそのうち消す
2023-02-02 生のtsファイル持ってるならから字幕データを摘出するほうが速いかと