from collections import deque

def bfs_iterative(edges, start):
    # Створюємо словник для представлення графа у вигляді списків суміжності
    graph = {}
    for edge in edges:
        u, v, _ = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


def dfs_iterative(edges, start_vertex):
    # Створюємо словник для представлення графа у вигляді списків суміжності
    graph = {}
    for edge in edges:
        u, v, _ = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    stack = [start_vertex]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку у зворотному порядку, щоб дотримуватись порядку обходу
            stack.extend(reversed(graph[vertex]))
    
    return visited

# Граф у вигляді списку ребер з вагами
graph = [
    ("Київ", "Біла Церква", 87),
    ("Київ", "Бориспіль", 37),
    ("Київ", "Бровари", 24),
    ("Київ", "Васильків", 39),
    ("Київ", "Вишгород", 20),
    ("Київ", "Буча", 25),
    ("Біла Церква", "Кагарлик", 35),
    ("Біла Церква", "Рокитне", 35),
    ("Біла Церква", "Васильків", 23),
    ("Бориспіль", "Яготин", 68),
    ("Бориспіль", "Бровари", 22),
    ("Бородянка", "Макарів", 23),
    ("Бородянка", "Буча", 16),
    ("Бровари", "Вишгород", 27),
    ("Бровари", "Яготин", 84),
    ("Буча", "Макарів", 28),
    ("Васильків", "Рокитне", 39),
    ("Вишгород", "Буча", 29),
    ("Кагарлик", "Миронівка", 24),
    ("Миронівка", "Рокитне", 20),
    ("Миронівка", "Тараща", 30),
    ("Рокитне", "Тараща", 32),
    ("Тараща", "Тетіїв", 26),
    ("Тетіїв", "Яготин", 65),
    ("Тетіїв", "Біла Церква", 57)
]

print ('Виконання BFS з початкової вершини "Київ"')
bfs_iterative(graph, "Київ")
print ('\nВиконання DFS з початкової вершини "Київ"')
dfs_iterative(graph, "Київ")