/**
 * p.161 10. 짝지어 제거하기
 * 소요시간: 32m 37s
 */

function solution(prices) {
    const len = prices.length;
    let answer = new Array(len).fill(0);
    let stack = [];

    for (let i=0; i<len; i++){
        // console.log('i =', i)
        if( stack.length>0 && ( prices[stack[stack.length-1]] > prices[i] ) ){
            answer[stack[stack.length-1]] = 1;
            stack.pop();
            while (stack.length>=0){
                if (stack.length === 0) {stack.push(i); break;}
                if (prices[stack[stack.length-1]] > prices[i]) {
                    answer[stack[stack.length-1]] = i - stack[stack.length-1];
                    stack.pop();
                } else {
                    stack.push(i);
                    break;
                }
            }
        } else {
            stack.push(i);
        }
        // console.log(stack);
        // console.log(answer);
        
    }

    if (stack.length === 0) { return answer }
    else { 
        const last = stack[stack.length-1] // 마지막 인덱스 번호
        for ( index of stack ) {
            answer[index] = last - index;
        }
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
