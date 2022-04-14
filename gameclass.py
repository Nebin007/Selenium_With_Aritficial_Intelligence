class aigamebot:
    def __init__(self):
        self.numstring = []
        self.score = [] #[max,min]
    
    def __str__(self):
        return '[Comp: '+str(self.score[0])+', '+str(self.numstring)+', Player: '+str(self.score[1])

    def setvals(self,lst,humscore,aiscore):
        self.numstring.clear()
        self.score.clear()
        self.numstring.extend(lst)
        ascore = aiscore.split(":")
        hscore = humscore.split(":")
        self.score.extend([int(ascore[1]),int(hscore[1])])

    def chkwin(self):
        if len(self.numstring) == 1:
            return True
        else:
            return False
            
    def whowon(self,player):
        plin = player - 1
        if len(self.numstring) == 1:
            if self.score[plin] == max(self.score):
                return True
            else:
                return False
        else:
            return False
    
    def drawcheck(self):
        if len(self.numstring) == 1:
            if self.score[0] == self.score[1]:
                return True
            else:
                return False
        else:
            return False

    def comp_act(self):
        bestscore = -10
        bestnum = 0
        for num in self.numstring:
            self.numstring.remove(num)
            self.score[0] = self.score[0] - num
            score = self.minimax(0,False)
            self.numstring.append(num)
            self.score[0] = self.score[0] + num
            if(score > bestscore):
                bestscore = score
                bestnum = num
        print("Computer Choose ",bestnum)
        return bestnum
    
    def minimax(self, depth, isMaxi):
        if self.whowon(1):
            return 1
        elif self.whowon(2):
            return -1
        elif self.drawcheck():
            return 0
        
        if(isMaxi):
            bestscore = -10
            for num in self.numstring:
                self.numstring.remove(num)
                self.score[0] = self.score[0] - num
                score = self.minimax(depth + 1,False)
                self.numstring.append(num)
                self.score[0] = self.score[0] + num
                if(score > bestscore):
                    bestscore = score
            return bestscore
        else:
            bestscore = 10
            for num in self.numstring:
                self.numstring.remove(num)
                self.score[1] = self.score[1] - num
                score = self.minimax(depth + 1,True)
                self.numstring.append(num)
                self.score[1] = self.score[1] + num
                if(score > bestscore):
                    bestscore = score
            return bestscore

