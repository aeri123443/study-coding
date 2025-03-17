/**
 * p.240 18. 두 개의 수로 특정 값 만들기
 * 해시 활용하기
 */

function countSort(arr, k){
    let hashTable = new Array(k+1).fill(0);

    for (let num of arr){
        if (num<k){
            hashTable[num] = 1;
        }
    }
    return hashTable;
}

function solution(arr, target){
    const hashTable = countSort(arr, target);

    for (let num of arr){
        const needNum = target - num;

        if(num<target && needNum!==num && hashTable[needNum]===1){return true}
    }

    return false

}

console.log(solution([1, 2, 3, 4, 8], 6)); //True
console.log(solution([2, 3, 4, 9], 10)); //False
console.log(solution([2, 3, 7, 9], 10)); //True
