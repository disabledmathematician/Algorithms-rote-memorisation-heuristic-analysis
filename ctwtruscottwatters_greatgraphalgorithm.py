"""
 (Can the true walk through a financial optimisation tree become a spanning tree out of all other hypothetical walks?)
 Charles Thomas Wallace Truscott Watters. 127 Broken Head Rd, Suffolk Park, NSW 2481
 
"""
import networkx as nx
import matplotlib.pyplot as plt

def Plot():
    n = 8
    count = 2
    while count < 6:
        plt.figure(count, dpi=120, figsize=[12, 12])
        L = [x for x in range(1, (3 ** count) + 3 + 2)]
        print(L)
        i, j = 1, 2
        k = 3
        x = 0
        G = nx.Graph()
        print(len(L))
        while (x < (len(L) // 3) - 1):
            G.add_edge(L[x], L[x + i])
            G.add_edge(L[x], L[x + j])
            G.add_edge(L[x], L[x + k])
            print(L[x], L[x + i], L[x + j], L[x + k])
            i += 2
            j += 2
            k += 2
            x += 1
        plt.title("Charles Truscott Watters.".format(count))
        pos = nx.spring_layout(G, seed=5)
        nx.draw_networkx_nodes(G, pos, node_color='blue', node_size=120)
        nx.draw_networkx_edges(G, pos, width=0.5)
        nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5, edge_color='grey', style='dashed')
        plt.savefig("Trinary-Charles-{}.png".format(count))
        count += 1

def CharlesTruscott():
    Plot()
    
CharlesTruscott()

