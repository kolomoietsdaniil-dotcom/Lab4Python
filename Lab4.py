from collections import deque

def create_sorter(sort_keys):
    return lambda item: tuple ( -item[key] if direction=="desc" else item[key] for key, direction in sort_keys)


def task1():
    players = [
    {'name': 'Bob', 'score': 90, 'games_played': 120},
    {'name': 'Alice', 'score': 90, 'games_played': 100},
]
    complex_sorter = create_sorter([('score', 'desc'), ('games_played', 'asc')])
    print(sorted(players, key=complex_sorter))

def sliding_window(iterable,n):
    window = deque()
    for i in iterable: 
        window.append(i)
        if len(window) == n:
            yield tuple(window)
            window.popleft()

def task2():
    data = [1, 2, 3, 4, 5, 6]
    windows = sliding_window(data, 3)
    print(list(windows)) 

