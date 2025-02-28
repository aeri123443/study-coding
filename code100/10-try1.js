/**
 * p.151 09. 10진수를 2진수로 변환하기
 * 소요시간: 28m 24s
 * 92.9점 
 */

function isCorrect(s){
    // [ { (
    let check = [0, 0, 0];
    for (x of s){
        if (x==='[') {check[0]+=1}
        else if (x==='{') {check[1]+=1}
        else if (x==='(') {check[2]+=1}
        else if (x===']') { if(check[0]<1) return false; check[0]-=1}
        else if (x==='}') { if(check[1]<1) return false; check[1]-=1}
        else if (x===')') { if(check[2]<1) return false; check[2]-=1}
    }
    for (let i=0; i<3; i++){
        if(check[i]!==0)return false
    }

    return true
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
