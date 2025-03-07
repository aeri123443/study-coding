/**
 * p.164 12. 주식 가격
 * 소요시간: 32m 37s
 */

function solution(prices) {
    let answer = [];

    // i항이 i+k항보다 커지는 순간에 k 리턴
    // i는 전체길이의 -2만큼만 반복
    for (let i=0; i<prices.length-2; i++){
        // console.log('i=',i)
        for  (let k=i+1; k<prices.length; k++){
            // console.log('k=',k);
            if (prices[i]>prices[k]){ answer.push(k-i); break;}
            if (k===prices.length-1){ answer.push(k-i); break;}
        }
    }
    // 마지막 두 원소는 무조건 1, 0으로 끝남 (계산 X)

    return [...answer, 1, 0];
}

console.log(solution([1, 2, 3, 2, 3])); // [4, 3, 1, 1, 0]
console.log(solution([1, 1, 1, 1, 2])); // [4, 3, 2, 1, 0]
console.log(solution([1, 1, 1, 1, 1])); // [4, 3, 2, 1, 0]
console.log(solution([1, 2, 3, 4, 5])); // [4, 3, 2, 1, 0]
console.log(solution([1, 1, 2, 1, 1])); // [4, 3, 1, 1, 0]
console.log(solution([5, 5, 3, 4, 4, 5])); // [2, 1, 3, 2, 1, 0]
console.log(solution([5, 4, 3])); // [1, 1, 0]
console.log(solution([4, 4])); // [1, 0]
