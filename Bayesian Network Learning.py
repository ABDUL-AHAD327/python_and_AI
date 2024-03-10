def parse_dataset(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip().split('\n')
    vertex_data = {}
    for line in content:
        vertex_part, rest = line.split('{', 1)
        vertex = int(vertex_part.strip(','))
        parents, cost = rest.rsplit('}', 1)
        cost = float(cost.strip(','))
        parents = parents.split(',') if parents else []
        parents = [int(p) for p in parents if p]
        if vertex not in vertex_data:
            vertex_data[vertex] = []
        vertex_data[vertex].append((set(parents), cost))
    return vertex_data

def greedy_vertex_ordering(vertex_data):
    remaining_vertices = set(vertex_data.keys())
    ordering = []
    total_cost = 0.0
    while remaining_vertices:
        best_next_vertex = None
        best_cost_increase = float('inf')
        for vertex in remaining_vertices:
            valid_parent_sets = [cost for parents, cost in vertex_data[vertex] if parents.issubset(ordering)]
            if valid_parent_sets:
                min_cost = min(valid_parent_sets)
                cost_increase = min_cost
                if cost_increase < best_cost_increase:
                    best_cost_increase = cost_increase
                    best_next_vertex = vertex
        if best_next_vertex is not None:
            ordering.append(best_next_vertex)
            total_cost += best_cost_increase
            remaining_vertices.remove(best_next_vertex)
        else:
            break
    return ordering, total_cost

dataset_file_paths = ['/mnt/data/data0.txt', '/mnt/data/data1.txt', '/mnt/data/data2.txt', '/mnt/data/data3.txt']
results = {}
for file_path in dataset_file_paths:
    dataset = parse_dataset(file_path)
    ordering, total_cost = greedy_vertex_ordering(dataset)
    results[file_path] = (ordering,total_cost)