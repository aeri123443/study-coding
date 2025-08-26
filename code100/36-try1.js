/**
 * p.381 36. 전화번호 목록
 * 정렬 시도는 좋았으나... 정렬하면 인접한 두 개만 포함하면 된다는 사실까지 떠올리기!!
 */

/**
 * 글자수 정렬 후 반복문
 */
// function solution(phone_book) {
//     // 글자수 오름차순 배치
//     let phoneList = [...phone_book]
//     phoneList.sort( (a,b)=> a.length - b.length);
//     // console.log(JSON.stringify(phoneList))

//     // 자기 인덱스 뒷부분부터 비교
//     for(let i=0; i<phoneList.length; i++ ){
//         const len = phoneList[i].length;
//         for(let j=i+1; j<phoneList.length; j++){
//             if(len === phoneList[j].length){continue}
//             if(phoneList[i]===phoneList[j].slice(0,len)){return false}
//             // console.log(phoneList[j].slice(0,len));
//         }
//     }
//     return true;
// }
/**
 * 글자 정렬 후 반복문
 */
function solution(phone_book) {
    // 글자 오름차순 배치
    let phoneList = [...phone_book]
    phoneList.sort();
    // console.log(JSON.stringify(phoneList))

    // 자기 인덱스 뒷부분부터 비교
    for(let i=0; i<phoneList.length; i++ ){
        const lenI = phoneList[i].length;
        for(let j=i+1; j<phoneList.length; j++){
            const lenJ = phoneList[j].length;
            if(lenI<lenJ){
                if(phoneList[i]===phoneList[j].slice(0,lenI)){return false}
            } else{
                if(phoneList[j]===phoneList[i].slice(0,lenJ)){return false}
            }
        }
    }
    return true;
}



false
console.log(solution(["119", "97674223", "1195524421"]));
// // true
console.log(solution(["123","456","789"]));
// false
console.log(solution(["12","123","1235","567","88"]));
