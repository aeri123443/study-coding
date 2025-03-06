/**
 * p.161 10. 짝지어 제거하기
 * 소요시간: 32m 37s
 * try 2를 조금 더 깔끔하게
 */

function solution(prices) {
    const len = prices.length;
    let answer = new Array(len).fill(0);
    let stack = [];

    for (let i=0; i<len; i++){
        while ( stack.length>0 && ( prices[stack[stack.length-1]] > prices[i] )){
            const p = stack.pop();
            answer[p] = i - p;
        }
        stack.push(i);
    }

    while( stack.length>0 ){
        const p = stack.pop();
        answer[p] = len - 1 - p;
    }
    
    return answer;
}

console.log(solution([1, 2, 3, 2, 3])); // [4, 3, 1, 1, 0]
console.log(solution([1, 1, 1, 1, 2])); // [4, 3, 2, 1, 0]
console.log(solution([1, 1, 1, 1, 1])); // [4, 3, 2, 1, 0]
console.log(solution([1, 2, 3, 4, 5])); // [4, 3, 2, 1, 0]
console.log(solution([1, 1, 2, 1, 1])); // [4, 3, 1, 1, 0]
console.log(solution([5, 5, 3, 4, 4, 5])); // [2, 1, 3, 2, 1, 0]
console.log(solution([4, 6, 9, 5, 3, 2, 7])); // [4, 2, 1, 1, 1, 0]
console.log(solution([5, 4, 3])); // [1, 1, 0]
console.log(solution([4, 4])); // [1, 0]
