# from graph import ADTGraph


# class Knapsack():
#     def __init__(self, items=[]):
#         '''initialize this knapsack with a directed graph
#         the start vertex of the graph being a frozenset with all possible items
#         input is an array of tuples (tuples are items)
#         ex: items = [(1,2),(4,2),(2,6),(3,2)]
#         tuples are given as (weight, value)
#         Once knapsack is created we can call optimal_knapsack(max_weight)
#         to find the best items that fit.
#         '''

#         self.items = frozenset(items)
#         self.graph = ADTGraph()
#         self.graph.digraph = True
#         self.add_vert_to_graph(self.items)

#     def add_vert_to_graph(self, vert):
#         '''We are using the graph class but we also need to store the weight and value
#         This is a custom function that is '''
#         self.graph.add_vertex(vert)
#         weight = sum([item[0] for item in vert])
#         value = sum([item[1] for item in vert])
#         self.graph.get_vertex(vert).data = (weight, value)

#     def get_weight(self, vert):
#         return self.graph.get_vertex(vert).data[0]

#     def get_value(self, vert):
#         return self.graph.get_vertex(vert).data[1]

#     def level_down_set(self, frozenset_items):
#         all_combinations = []
#         set_items = set(frozenset_items.copy())
#         for item in frozenset_items:
#             set_items.remove(item)
#             set_without_item = frozenset(set_items)
#             all_combinations.append(set_without_item)
#             set_items.add(item)
#         return all_combinations

#     def lowest_graph_level(self):
#         '''traverses the graph in BFS order from a start'''
#         for vertex in self.graph:
#             if len(self.graph.get_vertex(vertex).neighbors) == 0:
#                 yield vertex

#     def optimal_knapsack(self, max_weight):
#         done = False
#         while not done:
#             done = True
#             for combo in self.lowest_graph_level():
#                 if self.get_weight(combo) > max_weight:
#                     done = False
#                     level_down = self.level_down_set(combo)
#                     for level_down_combo in level_down:
#                         self.add_vert_to_graph(level_down_combo)
#                         self.graph.add_edge(combo, level_down_combo)

#         best_combo = None
#         for combo in self.lowest_graph_level():
#             if best_combo is None:
#                 best_combo = combo
#             else:
#                 if self.get_value(combo) > self.get_value(best_combo):
#                     best_combo = combo
#         best_value = sum([item[1] for item in best_combo])
#         return best_value, list(best_combo)

def recursive_knapsack(items, capacity):
    if len(items) == 0 or capacity == 0:
        return 0
    item = items[0]
    if item[0] > capacity:
        return recursive_knapsack(items[1:], capacity)
    value_without = recursive_knapsack(items[1:], capacity)
    value_with = recursive_knapsack(
        items[1:], capacity - item[0]) + item[1]
    return max(value_with, value_without)


def fast_knapsack(items, capacity, items_so_far=None):
    if items_so_far is None:
        items_so_far = items.copy()
    if len(items) == 0 or capacity == 0:
        return 0, items_so_far
    item = items[0]
    items_so_far_without = items_so_far.copy()
    items_so_far_without.remove(item)
    if item[0] > capacity:
        return fast_knapsack(items[1:], capacity, items_so_far_without)
    value_without = fast_knapsack(
        items[1:], capacity, items_so_far_without)
    value_with = fast_knapsack(
        items[1:], capacity - item[0], items_so_far.copy())
    value_with = (value_with[0] + item[1], value_with[1])
    if value_with[0] > value_without[0]:
        return value_with
    else:
        return value_without


if __name__ == '__main__':
    good_call = fast_knapsack([(10, 2), (4, 2), (2, 6), (3, 2), (10, 500)], 15)
    print(good_call)
