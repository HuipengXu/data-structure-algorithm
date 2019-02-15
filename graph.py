# @Time    : 2019/2/14 21:56
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from single_linked_list import SingleLinkedList


class Graph:
    """
    基于邻接表的无向图
    """

    def __init__(self, n: int):
        self.vertex_nums = n
        self.adjacency_list = [SingleLinkedList() for _ in range(n)]

    def add_edge(self, start: int, end: int):
        self.adjacency_list[start].append(end)
        self.adjacency_list[end].append(start)

    def breadth_first_search(self, start: int, end: int):
        """广度优先搜索"""
        if max(start, end) >= self.vertex_nums: return None
        if start == end: return [start]
        queue = [start]
        visited = [0] * self.vertex_nums
        visited[start] = 1
        prev = [None] * self.vertex_nums
        while visited[end] == 0:
            current = queue.pop(0)
            node = self.adjacency_list[current].head
            while node:
                if visited[node.val] == 1:
                    node = node._next
                    continue
                visited[node.val] = 1
                queue.append(node.val)
                prev[node.val] = current
                node = node._next
        p = prev[end]
        path = [end]
        while p != start:
            path.append(p)
            p = prev[p]
        path.append(p)
        return path[::-1]

    def depth_first_search0(self, start: int, end: int):
        """深度优先搜索，递归实现"""
        if max(start, end) >= self.vertex_nums: return None
        if start == end: return [start]
        visited = [0] * self.vertex_nums
        prev = [None] * self.vertex_nums

        def recur_dfs(start: int, end: int):
            if start == end:
                return
            visited[start] = 1
            next_node = self.adjacency_list[start].head
            # 避免拿到已经访问过的顶点
            while next_node and visited[next_node.val] == 1:
                next_node = next_node._next
            # 回溯
            if next_node is None:
                recur_dfs(prev[start], end)
            else:
                prev[next_node.val] = start
                recur_dfs(next_node.val, end)

        recur_dfs(start, end)
        p = prev[end]
        path = [end]
        while p != start:
            path.append(p)
            p = prev[p]
        path.append(p)
        return path[::-1]

    def depth_first_search1(self, start: int, end: int):
        """
        深度优先搜索，递归实现
        参考：https://time.geekbang.org/column/article/70891
        """
        if max(start, end) >= self.vertex_nums: return None
        if start == end: return [start]

        visited = [0] * self.vertex_nums
        prev = [None] * self.vertex_nums
        found = False

        def recur_dfs(start: int, end: int):
            nonlocal found
            if start == end:
                found = True
                return
            visited[start] = 1
            node = self.adjacency_list[start].head
            while node:
                if visited[node.val] != 1:
                    prev[node.val] = start
                    recur_dfs(node.val, end)
                if found: return
                node = node._next

        recur_dfs(start, end)
        p = prev[end]
        path = [end]
        while p != start:
            path.append(p)
            p = prev[p]
        path.append(p)
        return path[::-1]

    def depth_first_search2(self, start: int, end: int):
        """深度优先搜索，基于栈的循环实现"""
        if max(start, end) >= self.vertex_nums: return None
        if start == end: return [start]

        visited = [0] * self.vertex_nums
        visited[start] = 1
        prev = [None] * self.vertex_nums
        stack = [start]

        while visited[end] == 0:
            current = stack.pop()
            visited[current] = 1
            if visited[end] == 1: break
            node = self.adjacency_list[current].head
            while node:
                if visited[node.val] == 0:
                    prev[node.val] = current
                    stack.append(node.val)
                node = node._next

        p = prev[end]
        path = [end]
        while p != start:
            path.append(p)
            p = prev[p]
        path.append(p)
        return path[::-1]

    def n_degree_friends0(self, center: int, n: int):
        """
        寻找 n 度好友，基于广度优先搜索
        _count 记录当前度的好友个数
        count 用于记录当前度好友个数的消耗情况，同时用来判断度数的增加
        """
        if n == 0: return [center]
        if center >= self.vertex_nums: return None
        degree = _count = 0
        count = 1
        queue = [center]
        visited = [0] * self.vertex_nums
        visited[center] = 1
        while queue:
            vertex = queue.pop(0)
            count -= 1
            node = self.adjacency_list[vertex].head
            while node:
                v = node.val
                if visited[v] == 0:
                    _count += 1
                    queue.append(v)
                    visited[v] = 1
                node = node._next
            if count == 0:
                degree += 1
                count, _count = _count, 0
            if degree == n: return queue
        return None

    def n_degree_friends1(self, center: int, n: int):
        """
        寻找 n 度好友，基于广度优先搜索
        在广度优先的基础上添加一个数组记录与起始顶点的距离
        """
        visited = [0] * self.vertex_nums
        visited[center] = 1
        distance = [0] * self.vertex_nums
        queue = [center]
        while queue:
            vertex = queue.pop(0)
            node = self.adjacency_list[vertex].head
            while node:
                if visited[node.val] == 0:
                    v = node.val
                    distance[v] = distance[vertex] + 1
                    if n + 1 in distance:
                        break
                    visited[v] = 1
                    queue.append(v)
                node = node._next
        return [i for i, d in enumerate(distance) if d == n]


if __name__ == "__main__":
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    path0 = g.depth_first_search0(0, 7)
    path1 = g.depth_first_search1(0, 7)
    path2 = g.depth_first_search2(0, 7)
    path3 = g.breadth_first_search(0, 7)
    print(path0)
    print(path1)
    print(path2)
    print(path3)
    df0 = g.n_degree_friends0(4, 1)
    df1 = g.n_degree_friends1(4, 1)
    print(df0)
    print(df1)
