NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


def validate_is(item, TYPE):
    if TYPE is NODE:
        if len(item) != 3:
            raise ValueError(f'len(@node) must be 3, but item is "{item}".')
    if TYPE is EDGE:
        if len(item) != 4:
            raise ValueError(f'len(@edge) must be 4, but item is "{item}".')
    if TYPE is ATTR:
        if len(item) != 3:
            raise ValueError(f'len(@attr) must be 3, but item is "{item}".')


def validate_data(data):
    if not isinstance(data, list):
        raise TypeError(f'@data must be a list, but @data is "{data}".')


class Graph(object):
    def __init__(self, data=[]):
        validate_data(data)
        self._attrs = {}
        self._edges = []
        self._nodes = []
        for item in data:
            if len(item) == 0:
                raise TypeError(f'Did not understand item "{item}".')
            elif item[0] == NODE:
                validate_is(item, NODE)
                self._nodes.append(Node(item[1], item[2]))
            elif item[0] == EDGE:
                validate_is(item, EDGE)
                self._edges.append(Edge(item[1], item[2], item[3]))
            elif item[0] == ATTR:
                validate_is(item, ATTR)
                self._attrs[item[1]] = item[2]
            else:
                raise ValueError(f'Did not understand item "{item}".')

    @property
    def attrs(self):
        return self._attrs

    @property
    def edges(self):
        return self._edges

    @property
    def nodes(self):
        return self._nodes
