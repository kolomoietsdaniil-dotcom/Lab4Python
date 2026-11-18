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

while True:
    print("\n ГОЛОВНЕ МЕНЮ ")
    print("1 Завдання")
    print("2 Завдання ")
    print("0. Вийти з програми")
    
    choice = input("Оберіть пункт меню: ")
    
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2, 3 або 0.")