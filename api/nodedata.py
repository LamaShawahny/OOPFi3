class nodedata: #this class is represent the nodes of the graph with a basic methods
    def __init__(self,key,pos):
        self.key = key #the key of the node
        self.tag = 0 #the weight of the node
        self.info = "" #the info of rhe node
        self.pos = pos #the loctation of the node
        self.weight = 0 #the weight of the node
        self.neighbors = {}#this hashmap represent the edges between our node and itst neighbors
        self.outedeges = [] #we use this list in the method connect to save the destination of the edge and we use this list in the method remove node in DiGraph class

    def getweight(self):#this method return the node weight
        return self.weight

    def getinfo(self):#this method return the node info
        return self.info

    def getkey(self):#this method return the key value
        return self.key

    def getMyList(self): #return the list that contains the edeges that our node key is the dest
        return self.outedeges

    def gettag(self): # this method return the node tag
        return self.tag

    def getloc(self): # this method return the  location
        return self.pos

    def setloc(self,loc):# this method set the location
        self.pos=loc

    def setkey(self,key):# this method set the key value
        self.key=key

    def settag(self,tag):#this method set the node tag
        self.tag=tag

    def setinfo(self,info):#this method return the node tag
        self.info=info

    def setweight(self,weight):#this method set the node weight
        self.weight=weight

    def getmyhash(self):#return a hashmap that contains the edges between our node and is't neighbors
        return self.neighbors

    def getmyedeges(self):# return the edges that our node is the src in them
        return self.neighbors.values()
