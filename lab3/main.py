def parse(file):
    with open(file) as f:
        all_lines = f.readlines()
        all_lines = [line.strip().split(' ') for line in all_lines]

        graph = all_lines[2::]
        clients = all_lines[1]
        other_vertexes = [item for sublist in all_lines[2::] for item in sublist[0:2]]
        other_vertexes = set(other_vertexes)

        for i in clients:
            if i in other_vertexes:
                other_vertexes.remove(i)
    return graph, clients, other_vertexes


def dijkstra_algorythm(start_vertex, graph, unvisited):
    distances = {}
    visited = []
    current_vertex = start_vertex
    while unvisited:
        for i in graph:
            if current_vertex in i:
                dist = i.copy()
                dist.remove(current_vertex)
                if dist[0] in unvisited:
                    if dist[0] not in list(distances.keys()):
                        if current_vertex != start_vertex:
                            distances[dist[0]] = int(dist[1]) + distances[current_vertex]
                        else:
                            distances[dist[0]] = int(dist[1])
                    else:
                        if distances[dist[0]] > int(dist[1]) + distances[current_vertex]:
                            distances[dist[0]] = int(dist[1]) + distances[current_vertex]

        unvisited.remove(current_vertex)
        visited.append(current_vertex)
        distances = {key: val for key, val in sorted(distances.items(), key=lambda elem: elem[1])}
        for i in list(distances.keys()):
            if i in unvisited:
                current_vertex = i
                break
    return distances


def find_min_max_ping(file):
    graph, clients, other_vertexes = parse(file)
    max_pings = []
    for i in other_vertexes:
        result = dijkstra_algorythm(i, graph, list(other_vertexes)+clients)
        clients_ping = []
        for client in clients:
            clients_ping.append(result[client])
        max_pings.append(max(clients_ping))

    with open('gamsrv.out', 'w') as f:
        f.write(str(min(max_pings)))


if __name__ == '__main__':
    find_min_max_ping('gamsrv.in')
