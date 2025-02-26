/**
 * p.125 06. 실패율
 * 소요시간: 34m 42s
 */

function solution(N, stages) {
    var answer = [];
    var failList = [];
    // N회 반복
    for(let i=0; i<N; i++){
        // i+1 스테이지
        // 도전 인원
        const member = stages.length;
        // i번 반복째에 i+1의 개수 구함 (실패횟수)
        // 다음 회차에서 그만큼 배열 제하기
        stages = stages.filter( (stage) => stage !== (i+1) );
        
        // 실패율 계산 (키밸류?)     
        const fail = (member - stages.length) / member;
        failList.push({stage: i+1, fail:fail});
    }

    // 정렬
    // console.log(failList[0])
    // for (let x of failList){ console.log(x) }
    failList.sort( (a,b) => (b.fail - a.fail));
    // for (let x of failList){ console.log(x) }

    // stage만 추출
    for (let x of failList){ 
        answer.push(x.stage);
    }

    return answer;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])); // [3,4,2,1,5]
console.log(solution(4, [4,4,4,4,4])); // [4,1,2,3]
console.log(solution(4, [1,1,1,1])); // [1, 2, 3, 4]
console.log(solution(4, [1,2,2,3,5])); // [2, 3, 1, 4]
console.log(solution(4, [1,2,2,3,3])); // [3, 2, 1, 4]
