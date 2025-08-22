/**
 * p.326 30. 미로 탈출
 * 재귀 -> BFS 2차 시도
 * 75m 4s
 * visited를 Set 대신 2차원 boolean으로 만들었으면 더 효율적이었을 것
 * const visited = Array.from({ length: xMax }, () => Array(yMax).fill(false));
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

function solution(maps) {
    let visited = new Set();
    const xMax = maps.length;
    const yMax = maps[0].length;
    let s = "";    
    let e = "";    
    let l = "";    

    // 맵 탐색
    for( let i=0; i<xMax; i++){
        for( let j=0; j<yMax; j++){
            if(maps[i][j]==="S"){s=`${i},${j}`}
            if(maps[i][j]==="E"){e=`${i},${j}`}
            if(maps[i][j]==="L"){l=`${i},${j}`}
        }
    }
    // console.log(`l:${l}  s:${s}  e:${e}`);
    
    function bfs(start, cnt, labor){
        // console.log(start, cnt, labor)
        const q = new Queue;
        // [x, y, cnt, Labor]       
        q.push([...start, cnt, labor])

        while(!q.isEmpty()){
            const node = q.pop();
            // console.log(node)
            const x = Number(node[0]);
            const y = Number(node[1]);
            
            if(!visited.has(`${x},${y}`) && x>=0 && x<xMax && y>=0 && y<yMax && maps[x][y]!=="X"){
                const cursor = `${x},${y}`;
                // console.log("cursor: ", cursor)
                visited.add(cursor);

                if(l===cursor){
                    if(node[3]==="X"){
                        node[3] = "O";
                        // console.log("FIND L")
                        return [x, y, node[2], "O"];
                    }
                }
                if(e===cursor){
                    if(node[3]==="O"){
                        return node[2];
                    }
                }
                q.push([x+1, y, node[2]+1, node[3]]);
                q.push([x-1, y, node[2]+1, node[3]]);
                q.push([x, y+1, node[2]+1, node[3]]);
                q.push([x, y-1, node[2]+1, node[3]]);
            }
            // const cString = `${i}${j}`;

        }
    }
    // L 까지
    const toL=bfs(s.split(','), 0, "X");
    // console.log("toL: ", toL)
    if(!toL){return -1;}
    // E 까지
    visited = new Set();
    const toE=bfs([toL[0],toL[1]], toL[2], toL[3]);
    if(!toE){return -1;}
    return toE;
}

console.log(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) // 16
// console.log(solution(["SXOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) // -1
// console.log(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) // -1

// console.log(solution(["XXXXXX","XEOOOO","XXXSOO","XXXXOO","XXXXOL", "XXXXXX", "XXXXXX"])) // 11
// console.log(solution(["XXXXXX","XEOOOO","XXXSOO","XXXXOX","XXXXXL", "XXXXXX", "XXXXXX"])) // -1
// console.log(solution(["XXXXXX","XEOOOX","XXXSOX","XXXXOX","XXXXOL", "XXXXXX", "XXXXXX"])) // 11
// console.log(solution(["XXXXXX","XEOOOO","XXOSXO","XXOOXO","XXOOOL", "XXXXXX", "XXXXXX"])) // 11
// console.log(solution(["XXXXXX","XEXOOX","XXXSOX","XXXXOX","XXXXOL", "XXXXXX", "XXXXXX"])) // -1
