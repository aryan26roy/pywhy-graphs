"""
===========================
On PAGs and their validity
===========================

A PAG or a Partial Ancestral Graph is a type of mixed edge
graph that can represent, in a single graph, the causal relationship
between several nodes as defined by an equivalence class of MAGs.


PAGs model this relationship by displaying all common edge marks shared 
by all members in the equivalence class and displaying circles for those marks
that are not common.

More details on PAGs can be found at :footcite:`Zhang2008`.

"""

import pywhy_graphs
from pywhy_graphs.viz import draw
from pywhy_graphs import PAG

try:
    from dodiscover import FCI, make_context
    from dodiscover.ci import Oracle
    from dodiscover.constraint.utils import dummy_sample
except ImportError as e:
    raise ImportError("The 'dodiscover' package is required to convert a MAG to a PAG.")


# %%
# PAGs in pywhy-graphs
# ---------------------------
# Constructing a PAG in pywhy-graphs is an easy task since
# the library provides a separate class for this purpose.
# True to the definition of PAGs, the class can contain
# directed edges, bidirected edges, undirected edges and
# cicle edges. To illustrate this, we construct an example PAG
# as described in :footcite:`Zhang2008`, figure 4:

pag = PAG()
pag.add_edge("I", "S", pag.directed_edge_name)
pag.add_edge("G", "S", pag.directed_edge_name)
pag.add_edge("G", "L", pag.directed_edge_name)
pag.add_edge("S", "L", pag.directed_edge_name)
pag.add_edge("PSH", "S", pag.directed_edge_name)
pag.add_edge("S", "PSH", pag.circle_edge_name)
pag.add_edge("S", "G", pag.circle_edge_name)
pag.add_edge("S", "I", pag.circle_edge_name)


# Finally, the graph looks like this:
dot_graph = draw(pag)
dot_graph.render(outfile="new_pag.png", view=True)


# %%
# Validity of a PAG
# ---------------------------
# For a PAG to be valid, it must represent a valid 
# equivalent class of MAGs. This can be verified by
# turning the PAG into an MAG and then checking the 
# validity of the MAG
# To check if the constructed PAG is a valid one in
# pywhy-graphs, we can simply do:


# returns True
print(pywhy_graphs.valid_pag(pag))

# %%
# If we want to test whether this algorithm
# is working correctly or not, we can change
# a single mark in the graph such that the PAG
# does not represent the equivalent class of MAGs:

pag.remove_edge("S","I",pag.circle_edge_name)

# returns False
print(pywhy_graphs.valid_pag(pag))

# %%
# References
# ----------
# .. footbibliography::