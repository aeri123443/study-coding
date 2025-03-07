/**
 * p.161 11. 짝지어 제거하기
 * 소요시간: 16m 28s
 */

function solution(s){
    if (s.length%2 === 1) {return 0}

    let stack = [];
    for (c of s){
        if (stack.length===0) {stack.push(c); continue;}

        // pop과 같은건지 확인
        const last = stack.pop();
        if (last !== c) { stack.push(last, c);}
        // console.log(last, c, stack);
    }
    // 스택 비어있으면 1, 아니면 0 반환
    return stack.length===0 ? 1 : 0;
}

console.log(solution("baabaa")); // 1
console.log(solution("cdcd")); // 0
console.log(solution("abbcca")); // 1
console.log(solution("aaa")); //0
console.log(solution("abbcac")); // 0
