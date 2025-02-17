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
console.log(arr);

// 맨끝 삭제
arr.pop(); // [0, 1, 9, 4, 5, 5, -3, 2, 6, 4, 5, 5]
// 맨앞 삭제
arr.shift(); // [1, 9, 4, 5, 5, -3, 2, 6, 4, 5, 5]
// 중간 삭제
arr.splice(2, 2); // [1, 9, 5, -3, 2, 6, 4, 5, 5]
console.log(arr);

// 오름차순 정렬
// arr.sort( (a,b) => a-b );
arr.sort( (a,b) => a-b );
console.log(arr);

// 중복값 제거
const sortArr = [...new Set(arr)];
console.log(sortArr);

// 필터
const filteredArr = arr.filter( (a, i) => a===5 );
console.log(filteredArr);

// 배열의 길이만큼 반복 [key, value]
// in, of도 사용 가능
for( const [i, ar] of arr.entries()) {console.log(i, ar)}

/**
 * 수학
 */

// 최대 최소
const maxScore1 = Math.max(...arr);
const maxScore2 = Math.max(1, 2, 3);
console.log(maxScore1);
console.log(maxScore2);
