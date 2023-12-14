	 
import logging
import sys
 
# Setting up logging to monitor performance and errors
logging.basicConfig(level=logging.INFO)
 
def find_shortest_path(graph, start, end):
    """
    Find the Shortest Path
 
    This function finds the shortest path between two nodes in a graph.
    The graph is represented as an adjacency matrix.
 
    Args:
    graph (list of list): Adjacency matrix representing the graph.
    start (int): Starting node.
    end (int): Ending node.
 
    Returns:
    list: Shortest path between the start and end nodes.
 
    Examples:
    >>> graph = [
    ...     [0, 4, 0, 0, 0, 0, 0, 8, 0],
    ...     [4, 0, 8, 0, 0, 0, 0, 11, 0],
    ...     [0, 8, 0, 7, 0, 4, 0, 0, 2],
    ...     [0, 0, 7, 0, 9, 14, 0, 0, 0],
    ...     [0, 0, 0, 9, 0, 10, 0, 0, 0],
    ...     [0, 0, 4, 14, 10, 0, 2, 0, 0],
    ...     [0, 0, 0, 0, 0, 2, 0, 1, 6],
    ...     [8, 11, 0, 0, 0, 0, 1, 0, 7],
    ...     [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ... ]
    >>> start = 0
    >>> end = 4
    >>> find_shortest_path(graph, start, end)
    [0, 7, 6, 5, 4]
 
    >>> start = 3
    >>> end = 8
    >>> shortest_path = find_shortest_path(graph, start, end)
    >>> print(f"The shortest path from node {start} to node {end} is: {shortest_path}")
    The shortest path from node 3 to node 8 is: [3, 2, 8]
    """
    try:
        logging.info("Finding the shortest path...")
        # Number of nodes in the graph
        num_nodes = len(graph)
 
        # Initialize distance array with infinity values
        distance = [sys.maxsize] * num_nodes
 
        # Distance of start node from itself is 0
        distance[start] = 0
 
        # Initialize visited array
        visited = [False] * num_nodes
 
        # Initialize parent array to store the shortest path
        parent = [-1] * num_nodes
 
        # Find the shortest path
        for _ in range(num_nodes):
            # Find the node with the minimum distance
            min_distance = sys.maxsize
            min_index = -1
            for i in range(num_nodes):
                if not visited[i] and distance[i] < min_distance:
                    min_distance = distance[i]
                    min_index = i
 
            # Mark the node as visited
            visited[min_index] = True
 
            # Update the distance of the adjacent nodes
            for i in range(num_nodes):
                if (
                    not visited[i]
                    and graph[min_index][i] != 0
                    and distance[min_index] + graph[min_index][i] < distance[i]
                ):
                    distance[i] = distance[min_index] + graph[min_index][i]
                    parent[i] = min_index
 
        # Construct the shortest path
        shortest_path = []
        current_node = end
        while current_node != -1:
            shortest_path.append(current_node)
            current_node = parent[current_node]
        shortest_path.reverse()
 
        return shortest_path
 
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
 
if __name__ == "__main__":
    # Example usage
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    start = 0
    end = 4
    shortest_path = find_shortest_path(graph, start, end)
    if shortest_path:
        print(f"The shortest path from node {start} to node {end} is: {shortest_path}")
    else:
        print("Failed to find the shortest path.")