/**
 * p.251 21. 할인 행사
 * 타 풀이 참고해보기: fillter, slice 사용
 */

function solution(want, number, discount) {
    let answer = 0;

    for (let i=0; i<discount.length-9; i++){
        // 10개 슬라이스
        const slice = discount.slice(i, i+10);

        let flag = true;
        for (let j=0; j<want.length; j++){
            const keyword = want[j];
            // 필터 후 want와 비교
            if ( ( slice.filter( (item) => item===keyword).length ) !== number[j]) {
                flag = false;
                break;
            }
        }
        if(flag) {answer++}
    }

    return answer;
}

console.log(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) // 3
console.log(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])) // 0

