/**
 * 배열
 */
let arr = [1, 4, 5, 5, -3, 2];

// 맨 끝에 추가
arr.push(6); // [1, 4, 5, 5, -3, 2, 6]
// 배열을 추가
arr = arr.concat([4,5]); // [1, 4, 5, 5, -3, 2, 6, 4, 5]
// 스프레드 연산자 사용
arr = [...arr, ...[5, 6]]; // [1, 4, 5, 5, -3, 2, 6, 4, 5, 5, 6]
// 맨 앞에 추가
arr.unshift(0); // [0, 1, 4, 5, 5, -3, 2, 6, 4, 5, 5, 6]
// 중간에 추가 (시작점, 삭제수, 데이터)
arr.splice(2, 0, 9); // [0, 1, 9, 4, 5, 5, -3, 2, 6, 4, 5, 5, 6]
// console.log(arr); // [0, 1, 9, 4, 5, 5, -3, 2, 6, 4, 5, 5, 6]

// 맨끝 삭제
arr.pop(); // [0, 1, 9, 4, 5, 5, -3, 2, 6, 4, 5, 5]
// 맨앞 삭제
arr.shift(); // [1, 9, 4, 5, 5, -3, 2, 6, 4, 5, 5]
// 중간 삭제
arr.splice(2, 2); // [1, 9, 5, -3, 2, 6, 4, 5, 5]
// console.log(arr); // [1, 9, 5, -3, 2, 6, 4, 5, 5]

// 슬라이스
const sliceArr = arr.slice(2,5)
// console.log(sliceArr) // [5, -3, 2]

// 오름차순 정렬
// arr.sort( (a,b) => a-b );
arr.sort( (a,b) => a-b );
// console.log(arr); // [-3, 1, 2, 4, 5, 5, 5, 6, 9]

// 중복값 제거
const sortArr = [...new Set(arr)];
// console.log(sortArr); // [-3, 1, 2, 4, 5, 6, 9]

// 필터
const filteredArr = arr.filter( (a, i) => a===5 );
// console.log(filteredArr); // [5, 5, 5]

// 순서 뒤집기(거꾸로)
// console.log(arr);
arr.reverse();
// console.log(arr); // [9, 6, 5, 5, 5, 4, 2, 1, -3]

// 문자열로 합치기 (기본값 .,')
const joinArr = arr.join('');
// console.log(joinArr);

// 배열의 길이만큼 반복 [key, value]
// in, of도 사용 가능
for( const [i, ar] of arr.entries()) {
    // console.log(i, ar) // 0 -3  | 1 1 | 2 2 | ... | 7 6 | 8 9
}

// 배열 순회
let mapArr1 = [...new Array(6)].map( (_,i) => i );
let mapArr2 = mapArr1.map( (v) => v );
// console.log(mapArr1); // [0, 1, 2, 3, 4, 5]
// console.log(mapArr2); // [0, 1, 2, 3, 4, 5]

/**
 * 객체
 */
let obj = {'a': 0.125, 'b': 0.42857142857142855, 'c': 0.5, 'd': 0.5};

// 추가
obj['e'] = 0;
// console.log(obj); // {a: 0.125, b: 0.42857142857142855, c: 0.5, d: 0.5, e: 0}

// 객체를 리스트로
// [key, value] 배열이 들어간 2차원 배열 반환
let objToList = Object.entries(obj);
let objToListBykey = Object.keys(obj);
let objToListByVal = Object.values(obj);
// console.log(JSON.stringify(objToList)); // [["a",0.125],["b",0.42857142857142855],["c",0.5],["d",0.5],["e",0]]
// console.log(JSON.stringify(objToListBykey)); // ["a","b","c","d","e"]
// console.log(JSON.stringify(objToListByVal)); // [0.125,0.42857142857142855,0.5,0.5,0]

/**
 * 문자열
 */

// 문자열 분리
let splitStr1 = "ab c d".split('');
let splitStr2 = "ab c d".split(' ');
// console.log(splitStr1);
// console.log(splitStr2);

// 문자열 정렬
let sortedStr = [...'abcd'].sort();
let sortedStrRev = [...'abcd'].sort().reverse();
// console.log(sortedStr)
// console.log(sortedStrRev)

// 아스키 코드
let charToCode = "a".charCodeAt();
let strToCode = "abc".charCodeAt(1);
let codeToChar = String.fromCharCode(65);
let codeToStr = String.fromCharCode(65, 66, 67);
// console.log(charToCode);
// console.log(strToCode);
// console.log(codeToChar);
// console.log(codeToStr);

/**
 * 수학
 */

// 최대 최소
const maxScore1 = Math.max(...arr); //배열은 펼쳐서 넣어야 함
const maxScore2 = Math.max(1, 2, 3);
// console.log(maxScore1); // 9
// console.log(maxScore2); // 3

// 반올림
const roundFloat = Math.round(9.47 * 10)/10;
// 올림
const ceilFloat = Math.ceil(9.47 / 10)*10;
// 버림
const floorFloat = Math.floor(9.47 * 10)/10;
// console.log(ceilFloat);
// console.log(roundFloat);
// console.log(floorFloat);
