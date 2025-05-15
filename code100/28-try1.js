/**
 * p.316 28. 예상 대진표
 * 19m 04s
 */

function solution(n,a,b){
    let answer = 0;

    while ( true ) {
        answer++;

        a = Math.ceil(a/2);
        b = Math.ceil(b/2);

        if (a===b){break};
    }

    return answer;
}

console.log(solution(8,4,7)) // 3
console.log(solution(4,2,3)) // 2
console.log(solution(8,7,4)) // 3
console.log(solution(8,3,4)) // 1
console.log(solution(8,1,3)) // 2
