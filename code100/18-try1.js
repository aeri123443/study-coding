/**
 * p.240 18. 두 개의 수로 특정 값 만들기
 * 14m 07s
 */
 
function solution(arr, target) {
    const n = arr.length
    for (let i=0; i<n; i++){
        for (let k=i+1; k<=n; k++){

            let tmp = arr[i]+arr[k];
            if(tmp === target) {return "True"}
        }
    }
    return "False";
}

console.log(solution([1, 2, 3, 4, 8], 6)); //True
console.log(solution([2, 3, 4, 9], 10)); //false
console.log(solution([2, 3, 7, 9], 10)); //True
