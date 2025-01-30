/**
 * 프로그래머스 모범답안 참고
 * 학생 수가 정해져있고, 적으니 해당부분은 반복문을 사용하지 않음
 * 정답에서 일치하는 것만 필터링한 후 그 수를 세는 식으로 스코어를 계산
 */

function solution(answers) {
    var answer = [];

    // 패턴
    const a1=[1, 2, 3, 4, 5];
    const a2=[2, 1, 2, 3, 2, 4, 2, 5];
    const a3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
           // 1, 1, 1, 1, 1, 2, 2, 2, 2

    // 비교
    const a1c = answers.filter( (a, i) => a===a1[i%a1.length] ).length;
    const a2c = answers.filter( (a, i) => a===a2[i%a2.length] ).length;
    const a3c = answers.filter( (a, i) => a===a3[i%a3.length] ).length;
    // return [a1c, a2c, a3c];

    // 최대값
    const maxScore = Math.max(a1c, a2c, a3c);

    // 누구?
    if (maxScore===a1c){answer.push(1)}
    if (maxScore===a2c){answer.push(2)}
    if (maxScore===a3c){answer.push(3)}

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
