/**
 * p.151 09. 10진수를 2진수로 변환하기
 * 92.9점 틀린거 수정
 */

function isCorrect(s){
    let stack = [];
        for(x of s) {
            if ( (x==='[') || (x==='{') || (x==='(') ) { stack.push(x); }
            else if (x===']' && stack[stack.length-1]==='['){stack.pop(); }
            else if (x==='}' && stack[stack.length-1]==='{'){stack.pop(); }
            else if (x===')' && stack[stack.length-1]==='('){stack.pop(); }
            else return false;
        }
    return stack.length===0;
}

function solution(s) {
    var answer = 0;
    s = [...s];
   
    for (let k=0; k<s.length; k++){
        // 괄호가 제대로 되었는지 확인
        if ( isCorrect(s) ) {answer+=1};
        // 회전
        const tmp = s.shift();
        s.push(tmp);
    }

    return answer;
}

console.log(solution("[](){}")); // 3
console.log(solution("}]()[{")); // 2
console.log(solution("[)(]")); // 0
console.log(solution("}}}")); // 0
console.log(solution("")); // 0
console.log(solution("()(])[")); // 0
