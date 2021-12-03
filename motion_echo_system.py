from unity_bot import UnityBot
import random

# ユーザの入力をそのまま返す対話システム．
class EchoSystem:
    def __init__(self):
        pass
 
    def initial_message(self, input):
        return {'utt': 'こんにちは。対話を始めましょう。', 'end':False}
 
    def reply(self, input):
        motionNum = random.randrange(3)
        if(motionNum == 0):
         return {"utt": input['utt'], "end": False, "motion": "smile"}
        elif(motionNum == 1):
         return {"utt": input['utt'], "end": False, "motion": "bow"}
        else:
         return {"utt": input['utt'], "end": False, "motion": "wavehands"}
         
if __name__ == '__main__':
    system = EchoSystem()
    bot = UnityBot(system)
    bot.run()
    
