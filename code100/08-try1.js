/**
 * p.146 08. 괄호 짝 맞추기
 * 소요시간: 11m 13s
 * 스택으로도 풀어볼 것. 
 */

function solution(str) {
    // while로 Flag가 true일때까지 반복
    let s = [...str];
    let flag = false;
    while (!flag){
        flag = true;
        for (let i=0; i<s.length; i++){
            if (s[i]=='(' && s[i+1]==')'){           
                // ( 찾기
                // 바로 다음 )가 오면 두개 제거, flag false
                s.splice(i, 1);
                s.splice(i, 1);
                flag = false;
            }
        }
    }

    return s.length===0;
}
  
console.log(solution("(())()")); // true
console.log(solution("((())()")); // false
