const graph = {
    A: ["B", "C"],
    B: ["D", "E"],
    C: ["F"],
    D: [],
    E: ["F"],
    F: []
}

// BFS | Breadth-First Search
function bfs(graph, start){
    const queue = [];
    const visited = new Set();
    const order = [];

    queue.push(start);
    visited.add(start);

    while(queue.length > 0){
        const node = queue.shift();
        order.push(node);

        for( const neighbor of graph[node]){
            if(!visited.has(neighbor)){
                queue.push(neighbor)
                visited.add(neighbor)
            }
        }

    }

    return order;
}

console.log("BFS: ", bfs(graph, "A"));

function dfs(graph, start){
    const visited = new Set();
    const order = [];

    function explore(node){
        visited.add(node);
        order.push(node);

        for(const neighbor of graph[node]){
            if(!visited.has(neighbor)){
                explore(neighbor);
            }
        }
    }

    explore(start);
    return order;
}

console.log("DFS: ", dfs(graph, "A"))