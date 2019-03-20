# @Time    : 2019/3/20 14:41
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from single_linked_list import SingleLinkedList
from heap import SmallTopHeap
from collections import namedtuple
import sys


class DirectedGraph:

    def __init__(self, n: int):
        """
        :param n: 顶点数
        """
        self.adj = [SingleLinkedList() for _ in range(n)]

    def add_edge(self, s: int, e: int, w: float):
        """
        :param s: 起始顶点编号
        :param e: 终止顶点编号
        :param w: 权重
        :return:
        """
        self.adj[s].append((e, w))


def dijkstra(s: int, e: int, dg: DirectedGraph):
    """
    :param s: 起始顶点
    :param e: 终止顶点
    :return:
    """
    visited = [False] * len(dg.adj)
    predecessors = [None] * len(dg.adj)
    vertex = namedtuple('vertex', ['id', 'dist'])
    vertexes = []
    for i in range(len(dg.adj)):
        vertexes.append(vertex(i, sys.maxsize))
    vertexes[s] = vertexes[s]._replace(dist=0)
    sth = SmallTopHeap()
    sth.insert([vertexes[s].id, vertexes[s].dist])
    visited[s] = True
    while not sth.is_empty():
        v = sth.poll()
        if v[0] == e: break
        next_vertex = dg.adj[v[0]].head
        while next_vertex != None:
            id_, w = next_vertex.val
            temp_dist = v[1] + w
            if temp_dist < vertexes[id_].dist:
                vertexes[id_] = vertexes[id_]._replace(dist=temp_dist)
                predecessors[id_] = v[0]
                if visited[id_]:
                    sth.update([id_, temp_dist])
                else:
                    sth.insert([id_, temp_dist])
                    visited[id_] = True
            next_vertex = next_vertex._next
    path = [e]
    p_id = e
    while p_id != s:
        p_id = predecessors[p_id]
        path.insert(0, p_id)
    return vertexes[e].dist, path


if __name__ == "__main__":
    dg = DirectedGraph(6)
    edges = [(0, 1, 10), (0, 4, 15), (1, 2, 15), (1, 3, 2),
             (4, 5, 10), (3, 2, 1), (3, 5, 12), (2, 5, 5)]
    for edge in edges:
        dg.add_edge(*edge)
    print(dijkstra(0, 5, dg))
