#Hash table para el graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"] = {}
graph["b"]["a"] = 7
graph["b"]["d"] = 8
graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"] = {}
graph["d"]["fin"] = 1
graph["fin"] = {}

print(graph["start"].keys())
print(graph["a"].keys())
print(graph["b"].keys())
print(graph["c"].keys())
print(graph["d"].keys())



#hash table para costos
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

#hash table para parents
parents = {}
parents["a"] = "start"
parents["a"] = "b"
parents["b"] = "start"
parents["c"] = "a"
parents["d"] = "a"
parents["d"] = "b"
parents["d"] = "c"
parents["fin"] = None

processed = []
path = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    print(lowest_cost_node)
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    print(graph[node])
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
