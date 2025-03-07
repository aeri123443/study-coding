/**
 * p.161 11. 짝지어 제거하기
 * pop 대신 length 활용해보기
 */

function solution(s){
    if (s.length%2 === 1) {return 0}

    let stack = [];
    for (c of s){
        // pop과 같은건지 확인
        const len = stack.length;
        if ( (len>0) && (stack[len-1]===c) ) {stack.pop()}
        else {stack.push(c)}
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
