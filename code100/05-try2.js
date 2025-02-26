/**
 * 문제를 확실하게 분석할 것!!
 */

function solution(arr1, arr2) {
    var answer = [];

    const r1 = arr1.length;
    const c1 = arr2[0].length;
    const n1 = arr2.length;

    // 빈 배열 생성
    for(let i=0; i<r1; i++){
        answer.push( new Array(c1).fill(0) );
    }
    
    // 삽입
    for(let i=0; i<r1; i++){
        for(let k=0; k<c1; k++){
            for(let n=0; n<n1; n++){
                answer[i][k] += (arr1[i][n] * arr2[n][k]);
            }
        }
    }
    return answer;
}

console.log(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]));
console.log(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]));
console.log(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]]));
console.log(solution([[2, 3, 2], [4, 2, 4]], [[5, 4], [2, 4], [3, 1]]));
