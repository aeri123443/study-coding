/**
 * p.334 31. 양과 늑대
 * 60m 00s 
 * 아이디어: 최적 경로니까 bfs + 다시 부모로 올라가는 방식은 너무 비효율적 -> bfs 원리를 응용 -> 갈 수 있는 경로를 visited로
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
        return this.front===this.rear;
    }
}
function solution(info, edges) {

    // 트리 생성
    const tree = {};
    for(const x of edges){
        if(!tree[ x[0] ]) {tree[ x[0] ]=[]}
        tree[ x[0] ].push(x[1]);
    }
    // console.log(JSON.stringify(tree));

    // 큐 생성
    const q = new Queue();
    q.push( [0, 1, 0, new Set()] ); 

    let maxSheep = 1;
    while(!q.isEmpty()){
        // 현재 위치, 양 수, 늑대 수, 방문 가능 노드
        const [current, sheepCnt, WolfCnt, visited] = q.pop();
        // console.log(current, sheepCnt, WolfCnt, [...visited]);
        maxSheep = Math.max(maxSheep, sheepCnt);

        if(tree[current]){
            // console.log(" ", current, "'s child ", tree[current])
            // 자식 노드를 visited에 넣음
            for(const child of tree[current]){
                visited.add(child);
            }
        }

        // 방문 가능한 노드 탐색
        for(const next of visited){

            // 다음 노드가 양이면
            if(info[next]===0){
                const newVisited = new Set(visited);
                newVisited.delete(next);
                q.push( [next,sheepCnt+1, WolfCnt, newVisited] );
            }
            // 다음 노드가 늑대면
            else{
                if(sheepCnt > WolfCnt+1){
                    const newVisited = new Set(visited);
                    newVisited.delete(next);
                    q.push( [next,sheepCnt, WolfCnt+1, newVisited] ); 
                }
            }
        }
    }

    return maxSheep;
}

// 5
// console.log(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]));
// console.log(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,3],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]));
// 5
// console.log(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]));

