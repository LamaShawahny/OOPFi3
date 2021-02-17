from nodedata import nodedata
from edgedata import edgedata

class DiGraph:
    from typing import List
    def __init__(self):
        self.Graph={} #a dictionary that represent our graph
        self.mc=0 #the number of the edges in the graph
        self.edgesize=0
        self.nodenum=0

    def getnode(self,key:int): #return the node with the key value
        if key in self.Graph.keys():
            return self.Graph[key]
        return None

    def v_size(self) -> int:#return the number of the nodes in the graph
        return  self.nodenum

    def e_size(self) -> int:#return the number of the edegs in the graph
        return self.edgesize

    def get_all_v(self) -> dict:#this method return the nodes of the graph
        return self.Graph.values()

    def all_out_edges_of_node(self, id1: int) -> dict:# this method return the edegs of the node_id
        node=self.Graph[id1].getmyhash().values()
        if node is None:
            return None
        return node

    def all_in_edges_of_node(self, id1: int) -> dict: # this method return list that contains the edeges that id1 is the dest
        if self.Graph.get(id1).getoutedge() is None:
            return None
        return self.Graph.get(id1).getoutedge()


    def get_mc(self) -> int:# return the mc
        return self.mc

    def getege(self,src: int , dest: int) -> edgedata: # return the edge between the src and the dest
        des = self.Graph.get(dest)
        source = self.Graph.get(src)
        return source.getmyhash().get(des)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool: # this method takes two nodes and connect them (make them neighbors)
        if id1==id2: #connecting a node to himself do not do anything so this if check if nodes are the same
            return False
        src = self.Graph.get(id1)
        dest =self.Graph.get(id2)
        if src is None or dest is None: #if one of the nodes are not exist we dont do any thing
            return False
        e = edgedata(id1, id2, weight, "", 0)
        if self.getege(id1, id2) is None:#if the nodes is not neighbors we add to the edge number one
            self.edgesize=self.edgesize+1 # and edge between the nodes and add the nuber of the nodes
            src.getmyhash()[dest]=e
            dest.getMyList().append(src)
            return True
        src.getmyhash()[dest]=e
        dest.getMyList().append(src)
        self.mc=self.mc+1 #add one to the mc
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool: #this method add new node to the graph
        node = self.getnode(node_id)
        if node is not None:
            return False
        else:
            self.Graph[node_id] = nodedata(node_id,pos)
            self.mc = self.mc + 1  # we add one to the mc
            self.nodenum=self.nodenum+1
            return True

    def remove_node(self, node_id: int) -> bool: #// this method remove the node with key key
        sum=0
        if node_id in self.Graph.keys():
            mynode = self.Graph[node_id]
            if mynode.getmyhash().keys() is not None: #if the node hase edges
                for g in mynode.getmyhash().keys():
                    self.remove_edge(node_id,g.getkey()) # removes nodes from neighbors
                    sum = sum + 1
                if mynode.getMyList() is not None: # remove the nodes in the edges that our node is the dest in them
                    for g in mynode.getMyList():
                        self.remove_edge(g.getkey(),node_id)
                        sum=sum+1

            self.edgesize=self.edgesize-sum # // removes edges
            self.mc=self.mc+1  #add one to the mc
            self.nodenum=self.nodenum-1
            self.Graph.pop(node_id)


            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool: # this method remove the edge between two nodes
        src = self.Graph.get(node_id1)
        dest = self.Graph.get(node_id2)
        if dest is None or src is None: # if one of the two nodes ar'nt exist we don't do any thing
            return False
        if src.getmyhash().get(dest)is None: #if the nodes is not connected we don't do any thing
            return False
        src.getmyhash().pop(dest)
        self.edgesize=self.edgesize-1
        self.mc=self.mc+1
        return True
















