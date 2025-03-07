/**
 * p.172 13. 크레인 인형 뽑기 게임
 * 소요시간: 58m 00s
 */

function solution(board, moves) {
    let answer = 0;
    const b = board[0].length;

    let stack=[];

    for (let i=0; i<moves.length; i++){ 
        const m = moves[i]-1; // move 하나씩
        console.log('m =', m);
        
        for (let k=0; k<board.length; k++){ // 첫 차원 돌아다님
            // [_, m] 순환, 0이 아닐 때
            if (board[k][m]!==0){

                // [i, m]을 0으로 바꿈
                const tmp = board[k][m];
                board[k][m] = 0;
                // console.log('tmp =', tmp);
                // console.log('last =',stack[stack.length-1]);

                if (stack.length>0 && (stack[stack.length-1]===tmp)){
                    stack.pop();
                    answer+=2;
                } else {
                    stack.push(tmp);
                }

                console.log(stack);
                break;
            }            
        }        
    }
    return answer;
}

console.log(solution(
    [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
    [1,5,3,5,1,2,1,4]
)); // 4

console.log(solution(
    [[0,0,0,0,5],[0,0,0,0,3],[0,2,0,0,1],[4,2,0,4,2],[3,5,0,3,1]], 
    [1,5,3,5,1,2,1,4]
)); // 2

console.log(solution(
    [[0,0,0,0,0,5],[0,0,2,0,3,3],[0,2,5,0,1,5],[4,2,4,4,2,1],[3,5,1,3,1,4],[3,2,4,1,5,2]],
    [6,1,1,2,3,5,4,5]
)); // 6
