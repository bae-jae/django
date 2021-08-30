

class Mbti:
    MBTI = ["ENTP", "INTP", "ENTJ", "INTJ", "ENFP", "INFP", "ENFJ", "INFJ", "ESTJ", "ISTJ", "ESFJ", "ISFJ", "ESTP", "ISTP", "ESTP", "ISFP"]
    comb = []
    MBTIDict = {}
    
    def __init__(self):
        self.calc('')
        Mbti.MBTIDict = dict(zip(Mbti.comb, Mbti.MBTI))
        
        print(Mbti.MBTIDict)

    def calc(self, making):
        if len(making) == 4:
            Mbti.comb.append(making)
            return
    
        self.calc(making + "0")
        self.calc(making + "1")
        
        
        
Mbti();

print(Mbti.MBTIDict.keys())
    
    