import random
import re
class Game1A2B:
    _ans = '0000'
    guessedTimes = 0 #猜的次數
    _ansHistory = []
    _canBeGuessedTimes = 10 #可以猜的次數
    isOver = False
    def __init__(self):
        self.reset()
    def reset(self):
        '''重置答案和猜的次數'''
        self._ans = self._generateAns()
        self.guessedTimes = 0
        self._ansHistory.clear()
        self.guessedTimes = 0
        self.isOver=False
    def _generateAns(self):
        '''產生答案'''
        ans = 0
        stop = 1
        while stop:
            stop = 0
            ans = random.random()*10000
            ans = str(int(ans)).zfill(4)
            for i in range(4):
                for j in range(i+1,4):
                    if ans[i] == ans[j]:
                       stop+=1
        return ans

    def _is4numInput(self,guessAns):
        '''檢查輸入的答案是否為四位數字'''
        if re.search(r"^\d{4}$",guessAns):
            return True
        else:
            return False
    
    def _checkA(self,guessAns):
        ''' 檢查A的個數 並回傳a的個數'''
        a=0
        for i in range(4):
            if guessAns[i] == self._ans[i]:
                a+=1
        return a
    def _checkB(self,guessAns):
        ''' 檢查B的個數 並回傳b的個數'''
        b=0 
        for i in range(4):
            for j in range(4):
                if guessAns[i] == self._ans[j]:
                    b+=1
        return b
    def _judgeABWL(self,a,b):
        ''' 判斷幾A幾B或輸贏'''
        if self.guessedTimes >= self._canBeGuessedTimes:
            self.isOver = True
            return '猜的次數用盡囉! 答案是:'+ self._ans
        elif a == 4 and b == 0 :
            self.isOver = True
            return '答對囉!! 答案是:' + str(self._ans)
        elif a == 4 and b!= 0:
            return '有bugRRRR 快跑RRRR'
        else:
            return '第'+str(self.guessedTimes)+'猜的結果:'+str(a)+'A'+str(b)+'B'

        
         
        
    def checkAns(self,guessAns):
        '''檢查答案 回傳?A?B或輸贏'''
        a = 0
        b = 0
        msg = ''
        history=[]
        if guessAns=='h':
            return self._ansHistory
        elif self._is4numInput(guessAns):
            self.guessedTimes += 1
            a = self._checkA(guessAns)
            b = self._checkB(guessAns) - a # b包含a 所以要扣掉
            msg = self._judgeABWL(a,b)
        else:
            msg = '輸入錯誤 請重新輸入'
        history.append(guessAns)
        history.append(msg)
        self._ansHistory.append(history)
        return msg
