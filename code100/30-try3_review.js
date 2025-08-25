/**
 * p.326 30. 미로 탈출 - 복습
 * BFS는 큐에 방문경로를 넣지 않는다! 
 * 모든 경로를 탐색해야 하는 건 DFS 방식이고,
 * BFS는 처음 간 좌표가 곧 최단경로임.
 * 거리1, 거리2, 거리3인 순서대로 큐에 쌓이기 때문!
 */

// 큐 클래스
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

// 좌표 비교
function isSameXY(a, b){
    return a[0]===b[0] && a[1]===b[1];
}

function solution(maps){
    const xMax = maps.length;
    const yMax = maps[0].length;
    let s = [];
    let l = [];
    let e = [];

    // s l e 찾기
    for(let x=0; x<xMax; x++){
        for(let y=0; y<yMax; y++){
            if(maps[x][y]==="S"){s=[x,y]}
            else if(maps[x][y]==="L"){l=[x,y]}
            else if(maps[x][y]==="E"){e=[x,y]}
        }
    }
    // console.log(s, l, e);

    function explore(start, cnt, labor){
        const q = new Queue;
        let visited = Array.from({length:xMax}, ()=>new Array(yMax).fill(false))
        // 'x,y', cnt   
        q.push( [start, cnt] );

        while(!q.isEmpty()){
            const node = q.pop();
            let [x,y] = node[0];
            let newCnt = node[1];
            // console.log(node)

            // x, y 범위에 맞지 않거나 방문했으면 넘어가기
            if( !(x>=0 && y>=0 && x<xMax && y<yMax) || visited[x][y] || maps[x][y]==="X"){continue}
            
            // visited 적립
            visited[x][y] = true;
            // L/E 확인
            if( isSameXY([x,y], l) && !labor){
                return newCnt;
            } else if( isSameXY([x,y], e) && labor){
                return newCnt;
            }

            // x,y,cnt ++ --
            newCnt++;
            q.push([[x+1,y], newCnt])
            q.push([[x-1,y], newCnt])
            q.push([[x,y+1], newCnt])
            q.push([[x,y-1], newCnt])
        }

        return -1;
    }

    // S-L 탐색
    const cntSL = explore(s, 0, false);
    if(cntSL<0){ return -1 }
    // L-E 탐색
    const cntLE = explore(l, cntSL, true);
    if(cntLE<0){ return -1 }
    else {return cntLE}
}

// 16
console.log(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]));
// -1 S 막힘
console.log(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
// 9 직사각형
console.log(solution(["XXXXXX","XOLOOX","XOXXOX","XOXXEX","XOXXXX","XSXXXX","XXXXXX"]))
// 9 최단거리 찾기
console.log(solution(["OOOXXX","OOLOOX","OOXXOX","OOXXEX","OOXXXX","XSXXXX","XXXXXX"]))
// -1 S-L 경로 막힘 
console.log(solution(["OOXXXX","OXLOOX","OOXXOX","OOXXEX","OOXXXX","XSXXXX","XXXXXX"]))
// -1 L-E 경로 막힘
console.log(solution(["OOOXXX","OOLOOX","OOXXXX","OOXXEX","OOXXXX","XSXXXX","XXXXXX"]))
// -1 S-L, L-E 경로 막힘, S-E 경로 열림 (레버 확인)
console.log(solution(["OOXXXX","OXLOOX","OOXXXX","OOXXEX","OOXXOX","XSOOOX","XXXXXX"]))
// 9 중복 경로
console.log(solution(["XXXXXX","XOOLXX","XEXXXX","XOXXXX","XOXXXX","XSXXXX","XXXXXX"]))
