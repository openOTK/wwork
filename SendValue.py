# coding: utf-8

time = {
    "0%":0,
    "100%":320
}

color = {
    "0%":100,
    "20%":55,
    "50%":143,
    "80%":98,
    "100%":255
}

class SendValue():
    """パーセント指定で値が移り変わる"""
    def __init__(self, args1, args2):
        self.time = args1
        self.values = args2
        self.timeline = []
        self.sendCnt1 = []
        self.sendCnt2 = []
        self.sendCnt3 = []
        self.sendValues = []

    def strToint(self, args):
        u"""%を外して数値にして返す"""
        if(len(args) == 2):
            return int(args[0:1])
        elif(len(args) == 3):
            return int(args[0:2])
        elif(len(args) == 4):
            return int(args[0:3])

    def createTimeLine(self, args):
        u"""パーセントでの進み具合をリストで返す"""
        print(args)
        return list(range(args["0%"] * 10, args["100%"] * 10, (args["100%"] * 10)//100))

    def getValues(self):
        # タイムライン取得
        self.timeline = self.createTimeLine(self.time)
        #print("timeline:", timeline)
        
        # colorのパーセント割りを取得
        for i in self.values:
            self.sendCnt1.append(list([self.strToint(i), self.values[i]]))
        #print("sendCnt1:", sendCnt1)
        for j in range(len(self.sendCnt1)-1):
            self.sendCnt2.append(list(range(self.sendCnt1[j][0], self.sendCnt1[j+1][0], 1)))
        #print("sendCnt2:", sendCnt2)
        
        # タイムラインとcolorの数値変化を同期
        lineCnt = 0
        for k in range(len(self.sendCnt2)):
            for l in range(len(self.sendCnt2[k])):
                sendVal1 = self.sendCnt1[k+1][0] - self.sendCnt1[k][0]
                if(self.sendCnt1[k+1][1] >= self.sendCnt1[k][1]):
                    sendVal2 = self.sendCnt1[k+1][1] - self.sendCnt1[k][1]
                    self.sendCnt2[k][l] = list([self.timeline[lineCnt] // 10, int(round(self.sendCnt1[k][1] + ((sendVal2 / sendVal1) * l), 1))])
                    self.sendCnt3.append(list([self.timeline[lineCnt] // 10, int(round(self.sendCnt1[k][1] + ((sendVal2 / sendVal1) * l), 1))]))
                else:
                    sendVal2 = self.sendCnt1[k][1] - self.sendCnt1[k+1][1]
                    self.sendCnt2[k][l] = list([self.timeline[lineCnt] // 10, int(round(self.sendCnt1[k][1] - ((sendVal2 / sendVal1) * l), 1))])
                    self.sendCnt3.append(list([self.timeline[lineCnt] // 10, int(round(self.sendCnt1[k][1] - ((sendVal2 / sendVal1) * l), 1))]))
                lineCnt += 1
            
        #    print(str(sendCnt1[k][0])+"%","-----------------------------------------")
        #    print(sendCnt2[k])
        #print("100%","-----------------------------------------")
        
        #print(sendCnt3)
        
        # 結果
        nowValues = self.values["0%"]
        for m in range(self.time["100%"]):
            for n in range(len(self.sendCnt3)):
                if(m == self.sendCnt3[n][0]):
                    nowValues = self.sendCnt3[n][1]
            self.sendValues.append(nowValues)
            print("m:", m, ",color:", nowValues)
        return self.sendValues

def main():
    u""""""
    sv = SendValue(time, color)
    val = sv.getValues()
    print("len:",len(val),",val:",val)
    
if __name__ == "__main__":
    main()
    
