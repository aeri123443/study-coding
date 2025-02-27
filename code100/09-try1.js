/**
 * p.151 09. 10진수를 2진수로 변환하기
 * 소요시간: 21m 58s
 * 자연수 조건 확인하고 다시 풀어볼 것. 
 */

function solution(decimal) {
    let stack=[];
    let temp=decimal;
    if(decimal===0){return 0};
    while (temp>=1){
        if (temp===1){stack.push(`${1}`); break;}
        else {
            // console.log(temp, temp%2);
            stack.push( `${temp%2}` );
            temp = Math.floor(temp/2);
        }
    }
    // console.log(stack)
    let answer = '';
    for (let i=stack.length-1; i>=0; i--){
        answer += stack[i];
    }

    return answer;
    // 2씩 나눠서 나머지 담기
    // 스택 거꾸로 반환
}

// TEST 코드 입니다. 주석을 풀고 실행시켜보세요
console.log(solution(10)); // 반환값 :  1010
console.log(solution(27)); // 반환값 :  11011
console.log(solution(12345)); // 반환값 : 11000000111001
