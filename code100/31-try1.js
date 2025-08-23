/**
 * p.334 31. 양과 늑대
 * 102m 42s 갈아엎음!! 재귀 말고 bfs로
 */

function solution(info, edges) {

    let ptc = {}; // 부모 -> 자식 객체 
    let ctp = {}; // 자식 -> 부모 객체 
    for( const x of edges ){
        if( ptc[x[0]] ){ ptc[x[0]] = [ ...ptc[x[0]], x[1] ]}
        else{ ptc[ x[0] ] = [x[1]]; }

        if( ctp[x[1]] ){ ctp[x[1]] = [ ...ctp[x[1]], x[0] ]}
        else{ ctp[ x[1] ] = [x[0]]; }
    }
    console.log(JSON.stringify(ptc))
    console.log(JSON.stringify(ctp))

    // 양 최대치
    let maxSheep = 0;
    for( const x of info ){
        if( x===0 ){ maxSheep++; }
    }
    // console.log(maxSheep)

    // 뺑뺑이

    let sheepCnt = 0;

    // recentPath: 최근 3개 경로 추적(무한루프 방지)
    // start: 현재 노드
    // data: [양 수, 늑대 수, set(획득 번호)]
    function explore(recentPath, start, data){
        const newVisited = data[2];
        console.log(start, data, [...newVisited]);
        console.log(" recentPath: ", recentPath)
        // 양 최대치 달성 시 양 최대치 반환
        if( recentPath.length>0 && data[0]>=maxSheep ){ ;return maxSheep }
        // 양 <= 늑대가 되면 양 개수 반환
        else if( recentPath.length>0 &&  data[0] <= data[1] ){
            // sheepCnt 크면 업데이트 
            if( data[0] > sheepCnt){
                sheepCnt = data[0];
            }
        } else { // 양 > 늑대일 경우
            // 기존 추가된 노드가 아니면
            if( !newVisited.has(start) ){
                // 양 또는 늑대 추가
                newVisited.add(start)
                data[info[start]]++;
            }

            // 자식으로 이동
            if(ptc[start]){
                console.log("  ptc data:", [data[0], data[1], newVisited], [...newVisited])
                for( x of ptc[start] ){ 
                    if(recentPath.length<3){
                        recentPath.push(x);
                        explore(recentPath, x, [data[0], data[1], newVisited]);
                    } else {
                        if( !(recentPath[0]===recentPath[2] && recentPath[1]===x) ){
                            recentPath.shift();
                            recentPath.push(x);
                            explore(recentPath, x, [data[0], data[1], newVisited]);
                        }
                    }


                    // if(recentPath.length<3 || !(recentPath[0]===recentPath[2] && recentPath[1]===x) ){
                    //     explore(start, x, [data[0], data[1], newVisited]);
                    // }
                }
            }
            // 부모로 이동
            if(ctp[start]){
                console.log("  ctp data:", [data[0], data[1], newVisited], [...newVisited])
                for( x of ctp[start] ){
                    if(recentPath.length<3){
                        recentPath.push(x);
                        explore(recentPath, x, [data[0], data[1], newVisited]);
                    } else {
                        if( !(recentPath[0]===recentPath[2] && recentPath[1]===x) ){
                            recentPath.shift();
                            recentPath.push(x);
                            explore(recentPath, x, [data[0], data[1], newVisited]);
                        }
                    }

                }
            }
        
        }
    }

    let visited = new Set();
    let answer = explore([], 0, [0, 0, visited]);

    return answer;
}

// 5
console.log(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]));
// console.log(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,3],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]));
// 5
// console.log(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]));

