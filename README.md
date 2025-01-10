# PathFinder
### Introduction

Pathfinding algorithms are essential in computer science for finding the shortest or optimal path between two points in a graph. This project implements **Dijkstra's Algorithm**, **Breadth-First Search (BFS)**, and **Depth-First Search (DFS)** using Python and Flask, offering a web-based visualization for better understanding.

---

### Problem Domain

The task is to identify the optimal path between a starting point and an endpoint in a 2D grid with obstacles. Challenges include:

- Efficient exploration of the grid.
- Handling large grids with obstacles while maintaining performance.
- Providing an interactive visualization for algorithm behavior.

---

### Solution Domain

1. **Dijkstra's Algorithm**:
   - Guarantees the shortest path in weighted graphs.

2. **Breadth-First Search (BFS)**:
   - Ensures the shortest path in unweighted grids.

3. **Depth-First Search (DFS)**:
   - Explores paths deeply but doesn’t guarantee the shortest path.

---

### Technology Used

- **Language**: Python
- **Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript for grid rendering and interactivity

---

### Data Structures Used

1. **Graph**: Grid represented as nodes and edges between adjacent cells.
2. **Priority Queue**: Used in Dijkstra’s Algorithm.
3. **Queue**: Implements BFS for level-by-level exploration.
4. **Stack**: Used in DFS for deep path exploration.

---

### Methodology

#### Dijkstra's Algorithm
1. Set all distances to infinity; start node to 0.
2. Use a priority queue to select nodes with the smallest distance.
3. Update distances of neighbors and repeat until the endpoint is reached.

#### Breadth-First Search (BFS)
1. Enqueue the start node and mark it as visited.
2. Explore neighbors and enqueue them until the endpoint is found.

#### Depth-First Search (DFS)
1. Push the start node onto a stack and mark it as visited.
2. Explore neighbors deeply until reaching the endpoint.

---

### Implementation Highlights

- **Flask Backend**: Processes grid, start, and endpoint inputs and returns computed paths.
- **Frontend Visualization**: Shows explored nodes and final paths dynamically, using distinct colors for each algorithm.

---

### Conclusion

This project showcases the strengths of Dijkstra’s Algorithm, BFS, and DFS in pathfinding:

- **Dijkstra's Algorithm**: Ideal for weighted graphs.
- **BFS**: Efficient for unweighted graphs.
- **DFS**: Useful for traversal but not shortest paths.


 ### Output
 ![Group 1](https://github.com/user-attachments/assets/efe18244-f8b1-4634-9ae9-a22d0eb7fc34)
