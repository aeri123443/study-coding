/**
 * p.180 14. 표 편집
 * 지속적인 정확도테스트 실패로 try2에서 방식 변경
 * 추가, cmd[i][0]의 방식은 num이 10일경우 1로 인식되는 문제 발생
 */

function solution(n, k, cmd) {
    
    let table = [];
    for (let i=0; i<n; i++){
        table.push(i);
    }
    let p = k;
    let stack = [];

    for (let i=0; i<cmd.length; i++){
        switch(cmd[i][0]){
            case 'U':
                p -= Math.floor( cmd[i][2] );
                break;

            case 'D':
                p += Math.floor( cmd[i][2] );
                break;

            case 'C':
                if(p === table.length-1){
                    stack.push( table.pop() );
                    p -= 1;
                    break;
                }
                stack.push( table[p] );
                table.splice(p, 1);
                
                break;

            case 'Z':
                let tmp = stack.pop();
                for(let k=0; k<table.length; k++){
                    if(table[table.length-1]<tmp){
                        table.push(tmp);
                        break;
                    }
                    if(table[k]>tmp){
                        table.splice(k,0,tmp);
                        if(tmp <= p) {p += 1}
                        break;
                    }
                }
                break;
        }

        console.log('');
        console.log(i, p);
        console.log(table);
        console.log(stack);
    }

    let answer = new Array(n).fill('O');
    for(let i=0; i<stack.length; i++){
        answer[ stack[i] ]='X';
    }

    
    return answer.join('');
}
console.log(solution(6, 0, ["C", "D 3", "Z", "U 1", "C", "U 2", "Z", "C", "Z", "C", "C", "Z"]));
// console.log(solution(8, 2, ["D 1", "C", "Z", "D 3", "C", "Z"]));
// console.log(solution(8, 2, ["D 1", "C", "Z", "D 3", "C", "U 4", "C", "C", "U 2"]));
// console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]));
// console.log(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]));
