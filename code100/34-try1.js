/**
 * p.373 34. 폰켓몬
 */

function solution(nums) {
    // 집합으로
    const newSet = new Set(nums);
    // 사이즈 비교
    if(newSet.size <= (nums.length/2)){return newSet.size}
    else{return nums.length/2}

}

console.log(solution([3,1,2,3])) // 2
console.log(solution([3,3,3,2,2,4])) // 3
console.log(solution([3,3,3,2,2,2])) // 2
console.log(solution([1,2,2,4,5,6,7,8])) // 4