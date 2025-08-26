/**
 * p.381 36. 전화번호 목록
 * 3m 27s
 * startsWith이라는 함수가 잇음! 
 */

function solution(phone_book){
    // 글자 정렬
    phone_book.sort();
    // 전후 텍스트 비교
    for(let i=0; i<phone_book.length-1; i++){
        if( phone_book[i] === phone_book[i+1].slice(0,phone_book[i].length)){return false}
    }
    return true
}

// false
console.log(solution(["119", "97674223", "1195524421"]));
// // true
console.log(solution(["123","456","789"]));
// false
console.log(solution(["12","123","1235","567","88"]));
