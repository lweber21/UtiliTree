# UtiliTree
A lightweight toolkit for clonal trees

# Installation 

Clone the repo:
```bash
git clone git@github.com:lweber21/UtiliTree.git
```

Install the package:
```bash
cd UtiliTree
pip install .
```

Test installation:
```bash
enumerate -h
```


# Input

CSV with the first column holding the name or labels of the cluster and the second having CCFs:
See ccfs.txt for an example
```
label,ccf
1,1.0
2,0.5
3,0.2
4,0.1
```

# Usage

```bash
enumerate sample.txt -o trees.txt
```


# Output
A file containing all edge lists (parent,child) of all possible trees .
See trees.txt for an example.
```
#candidate tree 0
1,2
1,3
1,4
#candidate tree 1
1,2
1,4
2,3
#candidate tree 2
1,2
1,3
2,4
#candidate tree 3
1,2
2,3
2,4
#candidate tree 4
1,2
1,3
3,4
#candidate tree 5
1,2
2,3
3,4
```