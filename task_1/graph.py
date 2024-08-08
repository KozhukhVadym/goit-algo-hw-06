import networkx as nx
import matplotlib.pyplot as plt

# Створимо зважений граф
G = nx.Graph()

# Додаємо вершини (райцентри)
towns = ["Київ", "Біла Церква", "Бориспіль", "Бородянка", "Бровари", "Буча", "Васильків", 
         "Вишгород", "Макарів", "Кагарлик", "Миронівка", 
         "Рокитне", "Тараща", "Тетіїв", "Яготин"]

G.add_nodes_from(towns)

# Додаємо ребра з вагами (відстанями в км, приблизні значення)
edges = [
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
    ("Тетіїв", "Біла Церква", 57),
]

G.add_weighted_edges_from(edges)

# Візуалізуємо граф
pos = nx.spring_layout(G)  # обчислення положення вузлів
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()