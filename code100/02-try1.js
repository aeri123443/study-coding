/**
 * p.112 02. 배열 제어하기
 * 소요시간: 4m 32s
 */

function solution(arr){
    // 중복값 제거
    let sortArr = [...new Set(arr)];
    // 정렬
    return sortArr.sort( (a,b) => b-a );
    
}

console.log(solution([4, 2, 2, 1, 3, 4])); // 반환값 : [4, 3, 2, 1]
console.log(solution([2, 1, 1, 3, 2, 5, 4])); // 반환값 : [5, 4, 3, 2, 1]
