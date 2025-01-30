/**
 * p.117 04. 모의고사
 * 소요시간: 21m 57s
 * 테스트 케이스 추가 작성하기!! 
 */

function solution(answers) {
    var answer = [];

    // 패턴
    let pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];

    // 정답과 비교 (문항 수 고려)
    var score = [0,0,0];
    for (let i=0; i<answers.length; i++){ // 문제 개수만큼
        for(let k=0; k<3; k++){ // 학생 1, 2, 3
            if (pattern[k][i]===answers[i]) {
                score[k] += 1;
            }
        }
    }

    // 정답 수 담기 [3]
    // return score;

    // 큰놈 인덱스+1
    let maxScore = Math.max(...score);
    for (let i=0; i<3; i++){
        if (score[i]===maxScore){
            answer.push(i+1);
        }
    }

    return answer;
}

console.log(solution([1,2,3,4,5]));
console.log(solution([1,3,2,4,2]));
