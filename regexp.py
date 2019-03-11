# @Time    : 2019/3/11 14:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
"""
假设正表达式中只包含“*”和“?”这两种通配符，并且对这两个通配符的语义稍微做些改变，
其中，“*”匹配任意多个（大于等于 0 个）任意字符，“?”匹配零个或者一个任意字符
"""

matched = False


def match(texts: str, pattern: str, t: int, p: int):
    """
    :param texts: 待匹配的文本串
    :param pattern: 模式串
    :param t: 待匹配文本的当前匹配索引
    :param p: 模式串当前索引
    :return: 返回匹配到文本的具体位置
    """
    global matched
    if matched: return
    if p == len(pattern):
        if t == len(texts):
            matched = True
        return
    if pattern[p] == '*':
        for i in range(len(texts) - t + 1):
            match(texts, pattern, t + i, p + 1)
    elif pattern[p] == '?':
        match(texts, pattern, t, p + 1)
        match(texts, pattern, t + 1, p + 1)
    else:
        if t < len(texts) and texts[t] == pattern[p]:
            match(texts, pattern, t + 1, p + 1)


if __name__ == "__main__":
    pattern = 'df*f'
    s = 'dfsdl'
    match(s, pattern, 0, 0)
    print(matched)
