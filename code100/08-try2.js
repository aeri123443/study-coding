/**
 * p.146 08. 괄호 짝 맞추기
 */

function solution(s) {

    let stack = [];

    for (c of s){
        
        if (c==='('){
            // ( 가 나오면 스택에 넣음
            stack.push(c);
        } else if (stack.length>0){
            // )가 나오면 + 스택이 들어있으면 스택pop
            stack.pop();
        } else { 
            // )가 나왔는데 스택이 비어있음 == 잘못된 괄호임 스택pop
            return false;
        }
        
    }

    return stack.length===0;
}
  
console.log(solution("(())()")); // true
console.log(solution("((())()")); // false
