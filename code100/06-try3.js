/**
 * 모범 답안 참고하기
 * 발상: 도전자 수를 더 간략하게? -> 도전자수= 그 스테이지 이상까지 간 사람의 수
 */

function solution(N, stages) {
  let result = []
  for ( i=1; i<=N; i++){
    // 실패자 수
    const fail = stages.filter(s => s===i).length;
    // 도전자 수
    const chal = stages.filter(s => s>=i).length;
    // 실패율 계산, 리스트 넣기    
    const failR = fail/chal;
    result.push([i, failR]);
  }

  // 정렬
  result.sort( (a,b) => b[1]-a[1]);
  let answer = result.map( (r => r[0]));
  // 스테이지만
  return answer;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])); // [3,4,2,1,5]
console.log(solution(4, [4,4,4,4,4])); // [4,1,2,3]
console.log(solution(4, [1,1,1,1])); // [1, 2, 3, 4]
console.log(solution(4, [1,2,2,3,5])); // [2, 3, 1, 4]
console.log(solution(4, [1,2,2,3,3])); // [3, 2, 1, 4]
