/**
 * p.180 14. 표 편집
 * 익일 복습 필요 / 시간 재서 다시 풀기
 */

function solution(n, k, cmd) {
    let up = [...new Array(n+2)].map( (_,i) => (i-1) );
    let down = [...new Array(n+2)].map( (_,i) => (i+1) );
    let dels = [];

    let p = k+1;

    for( let i=0; i<cmd.length; i++) {
        switch(cmd[i][0]){
            case "C":
                dels.push(p);
                up[ down[p] ] = up[p];
                down[ up[p] ] = down[p];
                if( down[p]>n ) { p = up[p] }
                else { p = down[p]; }
                break;
            case "Z":
                let tmp = dels.pop();
                up[ down[tmp] ] = tmp;
                down[ up[tmp] ] = tmp;
                break;
            case "U":
                const uNum = cmd[i].split(' ')[1];
                for( let k=0; k<uNum; k++){
                    p = up[p];
                }
                break;
            case "D":
                const dNum = cmd[i].split(' ')[1];
                for( let k=0; k<dNum; k++){
                    p = down[p];
                }
                break;
            
        }
        // console.log('');
        // console.log(cmd[i]);
        // console.log(p);
        // console.log('u', up);
        // console.log('d',down);
        // console.log('del',dels);
        
    }

    let answer = new Array(n).fill('O');
    for(let i=0; i<dels.length; i++){
        answer[ dels[i]-1 ] = 'X'
    }

    return answer.join('');
}


console.log(solution(6, 2, ["C", "C", "Z", "C", "U 1", "C", "C", "Z", "Z", "U 1", "C", "D 2", "C"]));
console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]));
console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]));
