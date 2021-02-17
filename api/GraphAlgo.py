import json
import sys
from typing import List
import GraphInterface
from nodedata import nodedata
from edgedata import edgedata
from DiGraph import DiGraph
class GraphAlgo:  # this class is represent a directed weighted graph with a basic methods complex methods
    def init(self,graph):
        self.MyGraph= graph
        self.nill=-1
        sizeofarr1=0
        for i in graph.get_all_v():
            x=i.getkey()
            if sizeofarr1<x :
                sizeofarr1=x
        self.sizeofarr=sizeofarr1
        self.prev=[]
        self.destination = []

    def get_graph(self) -> GraphInterface: #this method return the graph
        return self.MyGraph

    def shortest_path(self, id1: int, id2: int) -> (float, list):# this method return the a list that contains the shortest path and its dest
        myls=[]
        if self.MyGraph.getnode(id1) is None or self.MyGraph.getnode(id2) is None:
            return -1,None
        if id1 == id2: # if the two nodes are the same return 0 and list contain id1 node
            myls.append(self.MyGraph.getnode(id1))
            return 0,myls
        if self.MyGraph.getnode(id1) is None or self.MyGraph.getnode(id2) is None: #if one of the nodes ar'nt exist return -1
            return -1,None
        if self.findtheminpath(id1, id2) is None: # if there is no path return -1
            return -1,None
        myls=self.findtheminpath(id1,id2)
        np=[]
        for n1 in myls:
            if n1 is not None:
                np.append(n1)
        x=self.destination[id2]
        if x==sys.maxsize:
            x=-1
        return x,np


    def findtheminpath(self, id1: int, id2: int) -> list:#this algorithm I find the psodocode in the internet
    #this method find the shortest path between the src and the dest
        a=0
        Q={}
        listofnodes=[]
        arraydic=[]
        self.resetarr()
        for n in self.MyGraph.get_all_v():
            Q[n.getkey()]=n
        self.destination[id1]=0
        while len(Q)!=0 :
            index=self.getmin(Q)
            u=self.MyGraph.getnode(index)
            if u is None:
                break
            del Q[index]
            for e1 in self.MyGraph.all_out_edges_of_node(u.getkey()):
                if e1.getdest() in Q.keys():
                    a= self.destination[index]+e1.getweight()
                    if a< self.destination[e1.getdest()]:
                        self.destination[e1.getdest()]=a
                        self.prev[e1.getdest()]=u.getkey()
        u2=self.MyGraph.getnode(id2)
        j=0
        if self.prev[u2.getkey()] !=-1 or u2.getkey()==id1:
            while u2 is not None:
                arraydic.append(u2.getkey())
                j=j+1
                u2=self.MyGraph.getnode(self.prev[u2.getkey()])
        if j==1:
           return None
        j=j-1
        while j>0 :
            listofnodes.append(arraydic[j])
            j=j-1
        if len(listofnodes)>0:
            listofnodes.append(id2)
        return listofnodes


    def resetarr(self):#this method set the prev array values to -1 and the destination to sys.maxsize
        for x in range(0,self.sizeofarr+1):
            self.prev.insert(x,self.nill)
            self.destination.insert(x,sys.maxsize)
        return

    def getmin(self, Q):  # this method return the the index of the min node
        mini = 0
        min = sys.maxsize
        for i in Q.keys():
            if self.destination[i] < min and i in Q.keys() :
                mini = i
                min = self.destination[i]
        return mini

    def save_to_json(self, file_name: str) -> bool: # this method save the graph to file
        try:
            with open(file_name,"w") as file:
                json.dump(self.MyGraph,default=lambda m:m.as_dict,indent=4,fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def load_from_json(self, file_name: str) -> bool: # this method load a graph from file
        self.MyGraph=DiGraph()
        try:
            with open(file_name,"r") as file_name:
                gg= json.load(file_name)
                Node=gg.get("Nodes")
                for n in Node:
                    if len(n)>1:
                        self.MyGraph.add_node(node_id=n["id"], pos=n["pos"])
                    self.MyGraph.add_node(node_id=n["id"])
                Edge=gg.get("Edges")
                for e in Edge:
                    self.MyGraph.add_edge(id1=e["src"],id2=e["dest"],weight=e["w"])
            return True
        except IOError as e:
            print(e)
            return False

    def connected_component(self, id1: int) -> list: #this method return all the connected components of the id1
        visited = []
        for n1 in self.MyGraph.get_all_v():
            if self.shortest_path(id1, n1.getkey())!=-1:
                visited.append(n1.getkey())
        return visited

    def connected_components(self) -> List[list]: # this method return list of lists that contains all the graph nodes and its connected components
        ls=[]
        for n in self.MyGraph.get_all_v():
            lst= self.connected_component(n.getkey())
            ls.append(lst)
        return ls

    def helpm(self,Q)->bool:
        flag=True
        for i in Q.keys():
            if Q[i]!=-5000:
                flag=False
        return flag

    def plot_graph(self) -> None:
        return

