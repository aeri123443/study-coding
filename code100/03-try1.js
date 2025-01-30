/**
 * p.115 03. 두 개 뽑아서 더하기
 * 소요시간: 10m 31s
 */

function solution(numbers) {
    
    // (a,b)에 대하여 a+b를 수행하고 새 리스트에 담음
    
    var answer = [];
    
    for (let i=0; i<numbers.length; i++){
        for (let k=i+1; k<numbers.length; k++){
            answer.push(numbers[i] + numbers[k]);
        }
        
    }
    // console.log(answer);
    answer = [...new Set(answer)];
    answer.sort( (a,b) => a-b );
    
    return answer;
}

console.log(solution([2, 1, 3, 4, 1])); // 반환값 : [2, 3, 4, 5, 6, 7]
console.log(solution([5, 0, 2, 7])); // 반환값 : [2, 5, 7, 9, 12]
