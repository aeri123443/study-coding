/**
 * p.210 16. 기능 개발
 * 22m 10s
 */
 
function solution(progresses, speeds) {
   
    // 프로그레스 별 남은 일자
    let left = [];
    for (let i=0; i<progresses.length; i++){
        const l = (100 - progresses[i]) / speeds[i];
        left.push( Math.ceil(l) );
    }

    // 배포
    let answer = [];
    let standard = left[0]; //기준값 초기화
    let day = 0;
    for (let i=0; i<left.length; i++){
        if(standard < left[i]) {
            answer.push(day);
            standard = left[i];
            day = 0;
        }
        day++;
        if(i===left.length-1){answer.push(day)}
    }

    return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5])); //[2, 1]
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])); //[1, 3, 2]
