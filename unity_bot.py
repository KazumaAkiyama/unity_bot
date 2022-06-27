# ソケットを使うためにsocketモジュールをimportする。
import socket, threading

class UnityBot:
    def __init__(self, system):
        self.system = system
        # ソケットを生成する。
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ソケットレベルとデータタイプを設定する。
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        f = open('setting.txt', 'r')
        datalist = f.readlines()
        IP = datalist[0].rstrip('\n')
        PORT = int(datalist[1])
        f.close()
        # サーバーは複数ipを使っているPCの場合はIPを設定して、そうではない場合はNoneや''で設定する。
        # ポートはPC内で空いているポートを使う。cmdにnetstat -an | find "LISTEN"で確認できる。
        self.server_socket.bind((IP, PORT))
        # server設定が完了すればlistenを開始する。
        self.server_socket.listen()


    def start(self, input_utt):
        # 辞書型 inputにユーザIDを設定
        input = {'utt': None, 'sessionId': "myid"}
 
        # システムからの最初の発話をinitial_messageから取得し，送信
        return self.system.initial_message(input)

    def message(self, input_utt):
        # 辞書型 inputにユーザからの発話とユーザIDを設定
        input = {'utt': input_utt, 'sessionId': "myid"}
 
        # replyメソッドによりinputから発話を生成
        system_output = self.system.reply(input)
 
        # 発話を送信
        return system_output

    def run(self):
        binder = self.binder
        try:
          # サーバーは複数クライアントから接続するので無限ループを使う。
          while True:
            # clientから接続すればacceptが発生する。
            # clientソケットとaddr(アドレス)をタプルで受け取る。
            client_socket, addr = self.server_socket.accept()
            # スレッドを利用してclient接続を作って、またaccept関数に行ってclientを待機する。
            th = threading.Thread(target=binder, args = (client_socket,addr))
            # スレッド開始
            th.start()
        except:
          # コンソール出力
          print("server")
        finally:
          # エラーが発生すればサーバーソケットを閉める。
          self.server_socket.close()

    # binder関数はサーバーからacceptしたら生成されるsocketインスタンスを通ってclientからデータを受信するとecho形で再送信するメソッドだ。
    def binder(self, client_socket, addr):
      # コネクションになれば接続アドレスを出力する。
      print('Connected by', addr)
      try:
        # 接続状況でクライアントからデータ受信を待つ。
        # もし、接続が切れちゃうとexceptが発生する。
        while True:
          # socketのrecv関数は連結されたソケットからデータを受信を待つ関数だ。最初に4byteを待機する。
          data = client_socket.recv(4)
          # 最初4byteは転送するデータのサイズだ。そのサイズはlittleエンディアンでbyteからintタイプに変換する。
          # C#のBitConverterはbigエンディアンで処理する。
          length = int.from_bytes(data, "big")
          # データを受信する。上の受け取ったサイズほど
          data = client_socket.recv(length)
          # 受信されたデータをstr形式でdecodeする。
          input_utt = data.decode()
          # 受信されたメッセージをコンソールに出力する。
          print('Received from', addr, input_utt)
    
          #受信されたメッセージから発話内容を決定する
          if "/start" in input_utt:
            sys_out = self.start(input_utt)
          else:
            sys_out = self.message(input_utt)
          sys_out_utt = sys_out["utt"]
          #motionの指定があれば文末に付け足す
          if "motion" in sys_out:
            sys_out_utt = sys_out_utt + ',' + sys_out["motion"]
          # バイナリ(byte)タイプに変換する。
          data = sys_out_utt.encode()
          # バイナリのデータサイズを計算する。
          length = len(data)
          # データサイズをlittleエンディアンタイプのbyteに変換して転送する。(※これがバグかbigを入れてもlittleエンディアンで転送する。)
          client_socket.sendall(length.to_bytes(4, byteorder='big'))
          # データをクライアントに転送する。
          client_socket.sendall(data)
      except:
        # 接続が切れちゃうとexceptが発生する。
        print("except : " , addr)
      finally:
        # 接続が切れたらsocketリソースを返却する。
        client_socket.close()