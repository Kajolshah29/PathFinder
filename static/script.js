const grid = [];
const rows = 20, cols = 20;
let start = null, end = null;
let algorithmPath = ''; // Keep track of the algorithm

const gridDiv = document.getElementById("grid");

// Initialize grid
for (let i = 0; i < rows; i++) {
    const row = [];
    for (let j = 0; j < cols; j++) {
        const cell = document.createElement("div");
        cell.classList.add("cell");
        cell.addEventListener("click", () => handleCellClick(cell, i, j));
        gridDiv.appendChild(cell);
        row.push(0); // 0: free, 1: obstacle
    }
    grid.push(row);
}

function handleCellClick(cell, i, j) {
    if (!start) {
        start = [i, j];
        cell.classList.add("start");
    } else if (!end) {
        end = [i, j];
        cell.classList.add("end");
    } else {
        grid[i][j] = 1;
        cell.classList.add("obstacle");
    }
}

async function startPathfinding(algorithm) {
    algorithmPath = algorithm; // Store selected algorithm
    const response = await fetch('/pathfind', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ grid, start, end, algorithm })
    });
    const data = await response.json();
    visualizePath(data.path);
}

function visualizePath(path) {
    // Clear any existing paths
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const cell = gridDiv.children[i * cols + j];
            cell.classList.remove('path-dijkstra', 'path-a-star');
        }
    }

    // Visualize the path based on the algorithm
    path.forEach(([i, j]) => {
        const cell = gridDiv.children[i * cols + j];
        if (algorithmPath === 'dijkstra') {
            cell.classList.add('path-dijkstra'); // Dark path for Dijkstra
        } else if (algorithmPath === 'a_star') {
            cell.classList.add('path-a-star'); // Light path for A*
        }
    });
}
