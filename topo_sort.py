# @Time    : 2019/3/20 22:09
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from dijkstra import DirectedGraph
from single_linked_list import SingleLinkedList


def topo_sort_by_kahn(dg: DirectedGraph):
    adj = dg.adj
    vertex_nums = len(adj)
    in_degree = [0] * vertex_nums
    for v in adj:
        node = v.head
        while node:
            if node.val is None: break
            in_degree[node.val[0]] += 1
            node = node._next
    queue = []
    for i in range(vertex_nums):
        if in_degree[i] == 0:
            queue.append(i)
    while len(queue) != 0:
        v = queue.pop(0)
        print(v)
        node = adj[v].head
        while node:
            if node.val is None: break
            id_ = node.val[0]
            in_degree[id_] -= 1
            if in_degree[id_] == 0:
                queue.append(id_)
            node = node._next


def topo_sort_by_dfs(dg: DirectedGraph):
    adj = dg.adj
    vertex_nums = len(adj)
    visited = [False] * vertex_nums
    reverse_adj = [SingleLinkedList() for _ in range(vertex_nums)]

    # 构造逆邻接表
    for i in range(vertex_nums):
        v = adj[i].head
        while v:
            if v.val is None: break
            id_ = v.val[0]
            reverse_adj[id_].append((i, 1))
            v = v._next

    def dfs(i):
        v = reverse_adj[i].head
        while v:
            if v.val is None or visited[v.val[0]]: break
            id_ = v.val[0]
            visited[id_] = True
            dfs(id_)
            v = v._next
        print(i)

    # 遍历
    for i in range(vertex_nums):
        if visited[i]: continue
        visited[i] = True
        dfs(i)


if __name__ == "__main__":
    dt = {'内裤': 0, '裤子': 1, '腰带': 2, '袜子': 3, '鞋子': 4, '衬衣': 5, '领带': 6, '外套': 7}
    edges = [(0, 1, 1), (0, 4, 1), (1, 4, 1), (1, 2, 1), (3, 4, 1), (5, 7, 1), (5, 6, 1)]
    dg = DirectedGraph(8)
    for e in edges:
        dg.add_edge(*e)
    # topo_sort_by_kahn(dg)
    topo_sort_by_dfs(dg)
