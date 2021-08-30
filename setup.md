# Virual Environmet
The environment I am using is **dcop**

### Create
    conda create --name dcop python=3.7 (Just press y for any prompts)
    conda activate dcop
    pip install .
    pip install -e .[test] (To install pyDCOP in development mode with test dependencies)
    pip install -e .[doc] (To install the documentation)
    sudo dnf install glpk-utils

### Use
    conda activate dcop
    pydcop solve --algo dpop graph_coloring.yaml

# Python Version

Although the website says that Python>=3.6 works, I got some error which said 3.6 is not supported. 

Versions above Python 3.8 dont support ```import clock from time```. Removing that import is not possible the import must be inside some library. If you search for clock inside the entire repository, you wont find anything. So the current version that is being used id python 3.7

# Changes in the code 
The code imports pulp.solvers in three files viz ilp_compref_fg.py, ilp_compre.py,ioit.py using 

```from pulp.solvers import GLPK_CMD```. 

But this format has changed and it now has to be replaced with 

```import pulp``` 

```GLPK_CMD = pulp.getSolver('GLPK_CMD')```

# New additions
graph_coloring.yaml has been added to test if the setup is working well or not. 