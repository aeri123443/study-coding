/**
 * p.180 14. 표 편집
 * 복습
 * 49m 8s
 */

function solution(n, k, cmds) {
    let up = [...new Array(n+2)].map( (_,i) => i-1);
    let down = [...new Array(n+2)].map( (_,i) => i+1);
    let dels = [];
    let p = k+1;

    for(let cmd of cmds) {
        switch(cmd[0]){
            case 'C':
                dels.push(p);
                down[ up[p] ] = down[p];
                up[ down[p] ] = up[p];
                p = (down[p]===n+1) ? up[p] : down[p];
                // p = down[p];
                break;

            case 'Z':
                const tmp = dels.pop();
                down[ up[tmp] ] = tmp;
                up[ down[tmp] ] = tmp;
                break;
            
            case 'U':
                const uNum = cmd.split(' ')[1];
                for( let j=0; j<uNum; j++){
                    p = up[p];
                }
                break;

            case 'D':
                const dNum = cmd.split(' ')[1];
                for( let j=0; j<dNum; j++){
                    p = down[p];
                }
                break;
                

        }

        // console.log('')
        // console.log(cmd)
        // console.log(up)
        // console.log(down)
        // console.log(dels)
        // console.log('p', p)
    }

    let answer = new Array(n).fill('O');
    for (let del of dels){
        answer[del-1]='X';
    }

    return answer.join('');
}

console.log(solution(6, 2, ["C", "C", "Z", "D 1", "C", "C", "U 2", "C", "Z"]));
console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]));
console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]));
