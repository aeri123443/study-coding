/**
 * 교재 답안 참고하기
 * 발상: 수식에 플레이어 수가 주로 들어가니, 챌린지 별 실패한 사람 수를 정리해두자. 도전자 수야 전체 인원 수에서 실패자 수를 빼면 된다!
 */
function solution(N, stages) {

  // 남은 사람 수
  let total = stages.length;
  // 챌린지 별 실패자 리스트
  let chals = new Array(N+2).fill(0);
  for (let x of stages) {
    chals[x] += 1;
  }
//   console.log(chals); 
  //  0  1  2  3  4  5  6
  // [0, 1, 3, 2, 1, 0, 1]

  let fails = {};
  // N회 반복
  for (let i=1; i<=N; i++){
    // 도전자가 0이면 실패율을 0으로
    if ( total <= 0 ) {
        fails[i] = 0;
        continue;
    }
    // 실패율 계산
    // fails에 넣기
    fails[i] = chals[i] / total;

    // total에서 실패자 제하기
    total -= chals[i];
  }
//   console.log(fails);

  // 정렬
  // 옵젝을 리스트로
  fails = Object.entries(fails).sort( (a,b) => b[1]-a[1]);

  // 스테이지만 추출
  answer = fails.map( (f) => Number(f[0]))
  
  return answer;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])); // [3,4,2,1,5]
console.log(solution(4, [4,4,4,4,4])); // [4,1,2,3]
console.log(solution(4, [1,1,1,1])); // [1, 2, 3, 4]
console.log(solution(4, [1,2,2,3,5])); // [2, 3, 1, 4]
console.log(solution(4, [1,2,2,3,3])); // [3, 2, 1, 4]
