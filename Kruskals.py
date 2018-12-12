# -*- coding: utf-8 -*-

from weighted_Graph import Weighted_Graph
from functions import *
from Weighted_Graph import *
G = Weighted_Graph('test_graph.txt')

def Kruskal_Alg(self): 
  
        Min =[] 
  
        i = 0 
        e = 0  
            #Sort all the edges in non-decreasing               
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
             
        while e < self.V -1 :   
            # Pick the smallest edge and increment  
            min_incident_edge(T,G)
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            if x != y: 
                e = e + 1     
                Min.append([u,v,w]) 
                self.union(parent, rank, x, y)             
         
            H = Min
            print(G.draw_subgraph(H))  
            
            
            
            
            
