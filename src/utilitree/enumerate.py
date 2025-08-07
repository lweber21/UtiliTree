
import itertools 
import networkx as nx
import argparse 
import pandas as pd 

def check_dcfs(T, ccfs):

    for u in T:
        desc_dcf = sum( ccfs[u] for u in  sorted(T.successors(u)))
        if ccfs[u] < desc_dcf or desc_dcf > 1:
            return False 
    return True 

def enumerate_clone_trees(ccfs, sum_condition=True):
    '''
    Enumerate the set of mutation cluster trees that respect 
    the sum condition of the CCFs

    '''
    k = len(ccfs)
    G = nx.DiGraph()
    G.add_nodes_from([q for q in ccfs])
    for u,v in itertools.combinations(list(ccfs.keys()),2):
        if ccfs[u] >= ccfs[v]:
            G.add_edge(u,v, weight=1)
        elif ccfs[u] < ccfs[v]:
            G.add_edge(v,u, weight=1)

        
    trees = nx.algorithms.tree.branchings.ArborescenceIterator(G)

    if sum_condition:
        return [tree for tree in trees if check_dcfs(tree,ccfs)]
    else:
        return [tree for tree in trees]


def save_trees(fname, trees, sep=","):
        with open(fname, "w") as f:
            for i, tree in enumerate(trees):
                f.write(f"#candidate tree {i}\n")
                for parent, child in tree.edges:
                    f.write(f"{parent}{sep}{child}\n")





def main():
    parser = argparse.ArgumentParser(description="A tool to enumerate clonal trees for a small number k of clones.")
    parser.add_argument("file", type=str, help="input file of CCFs")
    parser.add_argument("--all", action="store_true", help="include trees that violate the sum condition")
    parser.add_argument("-o", "--out", type=str, help="output file")

    args = parser.parse_args()

    dat = pd.read_csv(args.file)
    if dat.shape[1] < 2:
        raise ValueError("there must be at least two columns, with first column being the label, second the CCF")
    dat.columns = ["label", "ccf"]
    ccfs = dict(zip(dat["label"], dat["ccf"]))
    trees = enumerate_clone_trees(ccfs, not args.all)

    if args.out:
        save_trees(args.out, trees)

