/**
 * p.334 31. 양과 늑대
 * 53m 16s
 */

class Queue{
    items = [];
    front = 0;
    rear = 0;

    push(item){
        this.items.push(item);
        this.rear++;
    }

    pop(){
        return this.items[this.front++];
    }

    isEmpty(){
        return this.front === this.rear;
    }
}

function makeBT(map){
    const tree = {};
    for(const x of map){
        if(!tree[x[0]]){tree[x[0]]=[x[1]]}
        else{tree[x[0]].push(x[1])}
    }
    return tree;
}

function solution(info, edges){
    // 양 최댓값일때 종료?
    let maxSheep = 0;
    // 트리 생성
    const tree = makeBT(edges);
    // console.log(JSON.stringify(tree));

    const q = new Queue;

    // [current(현재 노드), sheep cnt, wolf cnt, visited(방문가능노드)]
    q.push([0, 1, 0, new Set()]);

    while(!q.isEmpty()){
        const [name, sNum, wNum, visited] = q.pop();
        const newVisited = new Set(visited);
        maxSheep = Math.max(maxSheep, sNum);
        // console.log(name, sNum, wNum, [...visited])

        newVisited.delete(name);
        // 자식 노드 추가
        for(const child of tree[name] ?? []){
            newVisited.add(child);
        }
        // console.log()
        for(v of newVisited){
            // 양이면
            if(info[v]===0){
                q.push( [v, sNum+1, wNum, newVisited] )
            } else { // 늑대면 크기 비교
                if(sNum > wNum+1){
                    q.push( [v, sNum, wNum+1, newVisited] )
                }
            }
        }
    }

    return maxSheep;
}

// 5
console.log(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
// 5
console.log(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
