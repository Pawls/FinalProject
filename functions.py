from Weighted_Graph import *
#G = Weighted_Graph('test_graph.txt')
#G.draw_graph()
#print(G.edge_set())
#print(G.vertex_set())
#print(G.edge_dict())
#H = ({0,1,3}, [(0,1),(1,3)])
#G.draw_subgraph(H)

#COST of graph e with respect to graph G
def C(e, G):
    return G.edge_dict()[e]


def incident_edges(T,G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e:
                edges.append(e)
    return [e for e in edges if e not in T[1]]


def valid_incident_edges(T, G):
    edges = incident_edges(T,G)
    valid_edges = []
    for e in edges:
        if e[0] not in T[0] or e[1] not in T[0]:
            valid_edges.append(e)
    return valid_edges
#   return [e for e in incident_edges(T,G) if ....]
    
def min_valid_edge(T,G):
    edges = valid_incident_edges(T,G)
    min_e = edges[0]
    for e in edges:
        if C(min_e, G) > C(e, G):
            min_e = e
    return min_e

def update(T, G):
    e = min_valid_edge(T,G)
    T[1].append(e)
    for v in e:
        T[0].add(v)
    return T     

def min_incident_edge(T, G):
    edges = valid_incident_edges(T,G)
    min_edge = edges[0]
    min_weight = C(edges[0],G)
    for e in edges:
        this_weight = C(e,G)
        if this_weight < min_weight:
            min_edge = e
            min_weight = this_weight
    return min_edge
