/**
 * p.151 09. 10진수를 2진수로 변환하기
 * 타 풀이 참고하기: 객체 매핑 활용하기, slice 회전하기 
 */

function solution(s) {
    let answer = 0;
    const mapping = { ']':'[', '}':'{', ')':'('};
    
    for (let i=0; i<s.length; i++){
        // 회전
        const rocate = s.slice(i)+s.slice(0,i);

        let stack = [];
        let flag = true;
        for (c of rocate){
            // [ { ( 는 스택에 쌓음
            if ( c==='[' || c==='{' || c==='(' ) { stack.push(c) }
            // ) } ] 에서는 최근 스택에서 매핑되는게 있는지 확인
            else {
                const last = stack.pop();
                if (last !== mapping[c]) {flag=false; break;} // 없으면 false 반환
            }
        }

        if (stack.length===0 && flag) {answer++}

    }

    return answer;
}

console.log(solution("[](){}")); // 3
console.log(solution("}]()[{")); // 2
console.log(solution("[)(]")); // 0
console.log(solution("}}}")); // 0
console.log(solution("")); // 0
console.log(solution("()(])[")); // 0
