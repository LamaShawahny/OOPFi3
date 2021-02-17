class edgedata:

    def __init__(self, src, dest , weight, info, tag):
        self.src=src
        self.weight =weight
        self.dest =dest
        self.info= " "
        self.tag=tag

    def getsrc(self):
        return self.src

    def getdest(self):
        return self.dest

    def getweight(self):
        return self.weight

    def getinfo(self):
        return self.info

    def getTag(self):
        return self.tag

    def setsrc(self, src):
        self.src = src

    def setdest(self, dest):
        self.dest = dest

    def setweight(self, weight):
        self.weight = weight

    def setinfo(self,s):
        self.info = s

    def setTag(self,t):
        self.tag = t