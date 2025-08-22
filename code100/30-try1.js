/**
 * p.326 30. 미로 탈출
 * 89m 11s 갈아엎음!!
 */

function solution(maps) {
    let cursor = ["X", 0, 0, 0]; // L여부, x, y, 이동 횟수
    const xMax = maps.length;
    const yMax = maps[0].length;
    const map={} //"XY", "V O/X;"
    // let s = "";
    let e = "";
    let l = "";

    // 맵 생성
    for( let i=0; i<xMax; i++){
        for( let j=0; j<yMax;j++){
            if( maps[i][j]==="S" ) {
                cursor = ["X", i, j, 0]; // L여부, x, y, 이동 횟수
            }
            if( maps[i][j]==="E" ) {e=`${i}${j}`}
            if( maps[i][j]==="L" ) {l=`${i}${j}`}
            map[`${i}${j}`] = "X" 
        }
    }

    // 이동 시작
    function explore(node){

        // 벽을 넘기지 않는 좌표일 때
        if(node[1]>=0 && node[2]>=0 && node[1]<xMax && node[2]<yMax) {
            
            /// cursor = ["X", i, j, 0]; // L여부, x, y, 이동 횟수
            // 방문한 경로가 아니라면
            if(map[`${node[1]}${node[2]}`]=="X"){
                console.log(`${node[1]}${node[2]}`);
                // End 지점일 경우
                if ( `${node[1]}${node[2]}` === e ) {
                    // L 방문 확인
                    if( node[0]==="O"){return node[3]}
                    
                }

                // Labor 지점일 경우
                if ( `${node[1]}${node[2]}` === l ) {
                    console.log("L");
                    // L 방문 등록
                    if( node[0]=="X"){
                        console.log(node);
                        node[0] = "O";
                        for(let i in map){map[i]="X"}
                        return node;
                    }

                }

                node[3] += 1;
                map[`${node[1]}${node[2]}`]="O";
                // (1,1)
                /// cursor = ["X", i, j, 0]; // L여부, x, y, 이동 횟수
                
                
                node[1]++;
                explore(node);
                
                // x 1 감소
                // (0,1)
                node[1] -= 2;
                explore(node);

                // y 1 증가
                // (1,2)
                node[1]++;
                node[2]++;
                explore(node);

                // y 1 감소
                // (1,0)
                node[2]-=2;
                explore(node);

            }

        }
    }
    // 레버 탐색
    let cusorLabor = explore(cursor);
    console.log(cusorLabor);
    // cusorLabor[0] = "O";
    // 맵 방문 여부 초기화
    // for(let i in map){map[i]="X"}
    // end 탐색
    const answer = explore(cusorLabor);
    return answer;
}

// console.log(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) // 16
// console.log(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) // -1

console.log(solution(["XXXXXX","XEOOOO","XXXSOO","XXXXOO","XXXXOL", "XXXXXX", "XXXXXX"])) // 11
// console.log(solution(["XXXXXX","XEOOOO","XXXSOO","XXXXOX","XXXXXL", "XXXXXX", "XXXXXX"])) // -1
// console.log(solution(["XXXXXX","XEOOOX","XXXSOX","XXXXOX","XXXXOL", "XXXXXX", "XXXXXX"])) // 11
// console.log(solution(["XXXXXX","XEOOOO","XXOSXO","XXOOXO","XXOOOL", "XXXXXX", "XXXXXX"])) // 11
