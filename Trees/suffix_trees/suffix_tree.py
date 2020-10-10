class Node:
    def __init__(self):
        self.suffix = -1


class Edge:
    def __init__(self, first, last, src, dest):
        self.first = first
        self.last = last
        self.src_node = src
        self.dest_node = dest

    def length(self):
        return self.last - self.first


class Suffix:
    def __init__(self, first, last, src_node):
        self.first = first
        self.last = last
        self.src_node = src_node

    def length(self):
        return self.last - self.first

    def is_explicit(self):
        return self.first > self.last

    def is_implicit(self):
        return not self.is_explicit


class SuffixTree:
    def __init__(self, string, case_sensitive=True):
        self.string = string
        self.case_sensitive = case_sensitive
        self.N = len(string) - 1
        self.nodes = [Node()]
        self.edges = {}
        self.active = Suffix(0, -1, 0)

        if not self.case_sensitive:
            self.string = self.string.lower()

        for i in range(len(string)):
            self.add_prefix(i)

    def __repr__(self):
        """
        Lists edges in the suffix tree
        """
        curr_index = self.N
        s = "\tStart \tEnd \tSuffix \tFirst \tLast \tString\n"
        values = list(self.edges.values())
        values.sort(key=lambda x: x.src_node)
        for edge in values:
            if edge.src_node == -1:
                continue
            s += "\t%s \t%s \t%s \t%s \t%s \t" % (
                edge.src_node,
                edge.dest_node,
                self.nodes[edge.dest_node].suffix,
                edge.first,
                edge.last,
            )

            top = min(curr_index, edge.last)
            s += self.string[edge.first : top + 1] + "\n"
        return s

    def insert_edge(self, edge):
        self.edges[(edge.src_node, self.string[edge.first])] = edge

    def remove_edge(self, edge):
        return self.edges.pop((edge.src_node, self.string[edge.first]))

    def canonize_suffix(self, suffix):

        if not (suffix.is_explicit()):
            e = self.edges[suffix.src_node, self.string[suffix.first]]
            if e.length() <= suffix.length():
                suffix.first += e.length() + 1
                suffix.src_node = e.dest_node
                self.canonize_suffix(suffix)

    def split_edge(self, edge, suffix):
        self.nodes.append(Node())
        e = Edge(
            edge.first,
            edge.first + suffix.length(),
            suffix.src_node,
            len(self.nodes) - 1,
        )
        self.remove_edge(edge)
        self.insert_edge(e)
        self.nodes[e.dest_node].suffix_node = suffix.src_node
        edge.first += suffix.length() + 1
        edge.src_node = e.dest_node
        self.insert_edge(edge)
        return e.dest_node

    def add_prefix(self, last):
        """
        The main additive method
        """

        last_parent_node = -1

        while True:
            parent_node = self.active.src_node
            if self.active.is_explicit():
                if (self.active.src_node, self.string[last]) in self.edges:
                    # present already
                    break
            else:
                e = self.edges[self.active.src_node, self.string[self.active.first]]
                if self.string[e.first + self.active.length() + 1] == self.string[last]:
                    break
                parent_node = self.split_edge(e, self.active)

            self.nodes.append(Node())
            e = Edge(last, self.N, parent_node, len(self.nodes) - 1)
            self.insert_edge(e)

            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_node = parent_node

            last_parent_node = parent_node

            if self.active.src_node == 0:
                self.active.first += 1
            else:
                self.active.src_node = self.nodes[self.active.src_node].suffix

            self.canonize_suffix(self.active)

        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix = parent_node

        self.active.last += 1
        self.canonize_suffix(self.active)

    def substring_search(self, substring):

        if not substring:
            return -1
        if not self.case_sensitive:
            substring = substring.lower()

        curr_node = 0

        t = 0
        while t < len(substring):
            edge = self.edges.get((curr_node, substring[i]))
            if not edge:
                return -1

            length_ = min(edge.length + 1, len(substring) - 1)

            if (
                substring[i : i + length_]
                is not self.string[edge.first : edge.first + length_]
            ):
                return -1

            i += edge.length() + 1
            curr_node = edge.dest_node
        return edge.first - len(substring) + ln

    def is_superstring(self, substring):
        return self.substring_search(substring) != -1


if __name__ == "__main__":
    print(SuffixTree("xabccbax"))
