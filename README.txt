【事前設定】
<Unity側>
　masterブランチにあるUnity.zipを解答しmainと同じファイルに移動させてください．
　Unity/AIX_Dialogue_Data/setting.json に，以下の通りに書き込んでください．

###

  "IP" : "(Pythonファイルを実行するサーバーのIPアドレス)"
  "PORT" : (Pythonファイルを実行するサーバーのアドレスのポート番号)
  "url" : "(IBM Cloudから作成したWatsonのAPIのアクセス用のURL)"
  "apikey" : "(IBM Cloudから作成したWatsonのAPI Key)" 
}
###

　デフォルトでは，IPアドレスはローカル，ポート番号は適当なもの，urlやapikeyは私のアカウントのものが書いてあります．一応そのまま実行することが可能です，ただし，無料版のIBM　Watsonは非アクティブが30日間続くとサービスが終了してしまうので，もし終了してしまった場合は
https://note.com/yiwase/n/n4d7eb15de9c8
などのページを参考にIBM Cloudアカウントを作成し，urlやapikeyを自身のものに書き換えてください．
(このREADMEが読まれている頃にはすでにサービスが終了しているかも)

<Python側>
　unity_bot.pyや実行するPythonファイルと同じ階層にsetting.txtを配置してください．内容はUnity側の設定と同様一行目にIPアドレス，二行目にポート番号です．必ず，Unity側で設定したものと同じものを書き込んでください．
　また，unity_bot.pyは「Pythonでつくる対話システム」内のTelegram_bot.pyなどを参考に作成していますので，同じように利用することができます．Pythonで対話システムを作成する際は，"telegram_bot" を "unity_bot" に，"TelegramBot" を "UnityBot" に置き換えて利用してください．

【使い方】
1)UnityBotをインポートしたPythonファイルを実行してください．(このときにサーバーが立つのでUnityアプリケーションより先に実行してください)
2)AIX_Dialogue.exeを起動してください．
3)「こんにちは．対話を始めましょう」から対話が始まります．
4)「音声認識停止」ボタンを押すとディクテーション機能が一時停止し，「音声認識開始」ボタンを押すとディクテーション機能が再開します．
　
・発話時にモーションをつけたい場合，{"utt":input['utt'], "end":False, "motion":"smile}のように辞書型の返り値にmotionを追加してください．
　サンプルとして"motion_echo_system.py"を同梱しておきます．
・音声認識が反応しないなどの不具合があった場合，一度「音声認識開始」ボタンをおしてみてください．



不明な点や不具合などがございましたら以下の連絡先まで連絡お願いします．

国立大学法人 電気通信大学 情報学専攻　稲葉研究室
2230003 秋山一馬
TEL: 090-2327-0493
MAIL: a2230003@edu.cc.uec.ac.jp
