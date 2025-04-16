/**
 * 외우기
 */
let arr = []
let obj = {}
let str = ''

// 배열 중간 추가/삭제 (시작점, 삭제수, 데이터)
arr = [1,2,3,4,5];
let removed = arr.splice(2, 0, 9)
// console.log(removed, arr); // [], [1, 2, 9, 3, 4, 5]

arr = [1,2,3,4,5];
removed = arr.splice(2, 2)
// console.log(removed, arr); // [3, 4], [1, 2, 5]

// 슬라이스
arr = [1,2,3,4,5];
// console.log(arr.slice(1,3)); // [2,3]
// console.log(arr.slice(1)); // [2,3,4,5]

// 오름차순 정렬
arr = [1,3,5,4,2];
arr.sort( (a,b) => a-b );
// console.log(arr); // [1,2,3,4,5]

// 필터
arr = [1,2,3,4,5];
const filteredArr = arr.filter( (a, i) => a>3 );
// console.log(filteredArr); // [5, 5, 5]

// 순서 뒤집기
arr = [1,2,3,4,5];
arr.reverse();
// console.log(arr); // [5, 4, 3, 2, 1]

// 객체를 리스트로
// [key, value] 배열이 들어간 2차원 배열 반환
obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4};
let objToList = Object.entries(obj);
let objToListBykey = Object.keys(obj);
let objToListByVal = Object.values(obj);
// console.log(JSON.stringify(objToList)); // [["a",1],["b",2],["c",3],["d",4]]
// console.log(JSON.stringify(objToListBykey)); // ["a","b","c","d","e"]
// console.log(JSON.stringify(objToListByVal)); // [1,2,3,4]

// 문자열 정렬
str = 'baedc'
let sortedStr = [...str].sort();
// console.log(sortedStr); // ['a', 'b', 'c', 'd', 'e']

// 아스키코드
let charToCode = "a".charCodeAt();
let strToCode = "abc".charCodeAt(1);
let codeToChar = String.fromCharCode(65);
let codeToStr = String.fromCharCode(65, 66, 67);
// console.log(charToCode); // 97
// console.log(strToCode); // 98
// console.log(codeToChar); // A
// console.log(codeToStr); // ABC

// 반올림
const roundFloat = Math.round(9.47 * 10)/10;
// 올림
const ceilFloat = Math.ceil(9.47 / 10)*10;
// 버림
const floorFloat = Math.floor(9.47 * 10)/10;
console.log(roundFloat); // 9.5
console.log(ceilFloat); // 10
console.log(floorFloat); // 9.4

// 큐
// 연결리스트
// 순열조합(재귀)