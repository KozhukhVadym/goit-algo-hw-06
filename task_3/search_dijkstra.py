import heapq

def dijkstra(edges, start_vertex):
    # Створюємо словник для представлення графа у вигляді списків суміжності з вагами
    graph = {}
    for edge in edges:
        u, v, weight = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    # Ініціалізація відстаней та черги пріоритетів
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

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

# Виконання алгоритму Дейкстри з початкової вершини "Вінниця"
distances = dijkstra(graph, "Київ")
for vertex, distance in distances.items():
    print(f"Відстань від Київ до {vertex}: {distance}")
