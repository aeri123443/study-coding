/**
 * 교재 정답 참고
 * of, entries 사용해보기
 */

function solution(answers) {
    var answer = [];

    // 패턴
    let patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];

    // 정답과 비교
    let scores = [0, 0, 0]
    for( const [i, ans] of answers.entries()) { // answers 길이만큼 반복
        for( const [k, pattern] of patterns.entries()){ // 학생 수만큼 반복
            if (ans === pattern[i%pattern.length]){
                scores[k] += 1;
            }
        }
    }
    // return scores;

    // 최대값
    const maxScore = Math.max(...scores);
    // 누구?
    for( const [i, score] of scores.entries() ){
        if( maxScore===score){
            answer.push(i+1);
        }
    }

    return answer;
}

console.log(solution([1,2,3,4,5]));
console.log(solution([1,3,2,4,2]));
console.log(solution([1, 1, 1, 1, 1, 2, 2, 2, 2]));

// 1, 2, 3, 4, 5, 1, 2, 3, 4, 5
// 1, 1, 1, 1, 1, 2, 2, 2, 2 반복!!!

// 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5
// 1, 1, 1, 1, 1, 2, 2, 2, 2

// 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
// 1, 1, 1, 1, 1, 2, 2, 2, 2

// [2, 3, 3] => [2,3]
