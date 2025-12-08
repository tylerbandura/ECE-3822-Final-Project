'''
file path: /home/tul34363/ece_3822LABWORK/ECE-3822-Final-Project/DataStructures/BFS.py

descripton: this file contains a BFS using queue.py and graph.py.
            this BFS will be used in the query section. I will do
            this so that the code looks better and more OOP

            this will be use in query 6 to find the shorest path between two actors

author: Tony Mejia
'''

# import code from toher files
from DataStructures.Queue import Queue_circular
from DataStructures.Graph import Graph

# BFS class that specializes in fisnding the shortest path so i can use it in query 6
class BFS:
    # constructor
    def __init__(self, graph: Graph):
        # initialize graph
        self.graph = graph

    # fuction to find the shortest path between two nodes
    def shortest_path(self, start, end):
        # if start or end node not in graph, return None
        # this is because we want to make sure the nodes exist
        if not self.graph.has_node(start) or not self.graph.has_node(end):
            return None
        
        queue = Queue_circular()
        queue.push(start)

        visited = {start: None} # dictionary to keep track of visited nodes and their parents

        # while there are nodes in the queue
        while queue.count() > 0:
            current = queue.pop() # get the current node

            # if we reached the end node, break
            if current == end:
                break

            '''heart of BFS, explore neighbors'''
            # for each neighbor of the current node
            # neighbor being the node connected to the current node
            for neighbor in self.graph.get_neighbors(current):
                # if neighbor not visited, add it to the queue and mark it as visited
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.push(neighbor)
            # end of heart of BFS

            # if we reached the end node, break
            if end not in visited:
                return None
            
            # restart from end to start to get the path
            path = [] # list to store the path
            node = end # start from the end node

            # while node is not None, add it to the path
            # this is because we want to go back to the start node so 
            # we use the visisted dictionary to get the parent of each node
            while node is not None:
                path.append(node)
                node = visited[node]
            path.reverse()
            return path
        
# end of BFS clas

# end of file