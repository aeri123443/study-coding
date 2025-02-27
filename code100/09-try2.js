/**
 * p.151 09. 10진수를 2진수로 변환하기
 */

function solution(decimal) {

    let stack = [];

    while( decimal>0) {
        // 2를 나눈 나머지 담기
        stack.push( decimal%2 );
        // 2를 나눈 몫 저장
        decimal = Math.floor( decimal/2 );
    }

    return stack.reverse().join('');
}

// TEST 코드 입니다. 주석을 풀고 실행시켜보세요
console.log(solution(10)); // 반환값 :  1010
console.log(solution(27)); // 반환값 :  11011
console.log(solution(12345)); // 반환값 : 11000000111001
