/**
 * p.210 16. 기능 개발
 * 다른 사람 풀이 적용하기
 */
 
function solution(progresses, speeds) {
   
    let days = progresses.map( (progress, index) => Math.ceil( (100-progress)/speeds[index] ));

    let maxDay = days[0];
    let answer = [0];

    for (let i=0, j=0; i<progresses.length; i++){
        if (maxDay >= days[i]){
            answer[j]++;
        } else {
            maxDay = days[i]
            answer[++j] = 1;
        }
    }

    return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5])); //[2, 1]
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])); //[1, 3, 2]
