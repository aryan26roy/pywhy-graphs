from enum import Enum, EnumMeta


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class EdgeType(Enum, metaclass=MetaEnum):
    """Enumeration of different causal edge endpoints.

    Categories
    ----------
    directed : str
        Signifies arrowhead ("->") edges.
    circle : str
        Signifies a circle ("*-o") endpoint. That is an uncertain edge,
        which is either circle with directed edge (``o->``),
        circle with undirected edge (``o-``), or
        circle with circle edge (``o-o``).
    undirected : str
        Signifies an undirected ("-") edge. That is an undirected edge (``-``),
        or circle with circle edge (``-o``).

    Notes
    -----
    The possible edges between two nodes thus are:

    ->, <-, <->, o->, <-o, o-o

    In general, among all possible causal graphs, arrowheads depict
    non-descendant relationships. In DAGs, arrowheads depict direct
    causal relationships (i.e. parents/children). In ADMGs, arrowheads
    can come from directed edges, or bidirected edges
    """

    ALL = "all"
    DIRECTED = "directed"
    BIDIRECTED = "bidirected"
    CIRCLE = "circle"
    UNDIRECTED = "undirected"


class EndPoint(Enum, metaclass=MetaEnum):
    """Enumeration of different causal edge endpoints.

    Categories
    ----------
    arrow : str
        Signifies arrowhead (">") endpoint. That is a normal
        directed edge (``->``), bidirected arrow (``<->``),
        or circle with directed edge (``o->``).
    circle : str
        Signifies a circle ("o") endpoint. That is an uncertain edge,
        which is either circle with directed edge (``o->``),
        circle with undirected edge (``o-``), or
        circle with circle edge (``o-o``).
    tail : str
        Signifies a tail ("-") endpoint. That is either
        a directed edge (``->``), or an undirected edge (``-``), or
        circle with circle edge (``-o``).

    Notes
    -----
    The possible edges between two nodes thus are:

    ->, <-, <->, o->, <-o, o-o

    In general, among all possible causal graphs, arrowheads depict
    non-descendant relationships. In DAGs, arrowheads depict direct
    causal relationships (i.e. parents/children). In ADMGs, arrowheads
    can come from directed edges, or bidirected edges
    """

    arrow = "arrow"
    circle = "circle"
    tail = "tail"
