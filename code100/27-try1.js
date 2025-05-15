/**
 * p.311 27. 이진 탐색 트리 구현
 * 27m 49s
 * 재귀함수 말고 생성자로 구현해보기 
 */

function adddata(tree, data, idx){
    if(tree.length===0){tree.push(data); return;}

    if(tree[idx]){
        if(data<tree[idx]){adddata(tree, data, idx*2+1)}
        else{adddata(tree, data, idx*2+2)}
    } else {
        tree[idx] = data;
    }
}

function finddata(tree, data, idx){
    if(tree[idx]===data){return true};
    if(idx > tree.length){return false};

    let ans = false;
    if(data<tree[idx]){ans = finddata(tree, data, idx*2+1)}
    else{ans = finddata(tree, data, idx*2+2)}
    return ans
}

function solution(lst, searchList) {
    let tree = [];
    let answer = [];

    for(x of lst){
        adddata(tree, x, 0);
    }
    for(x of searchList){
        answer.push( finddata(tree, x, 0) );
    }

    return answer;
}

console.log(solution([5,3,8,4,2,1,7,10], [1,2,5,6])) // [true, true, true, false]
console.log(solution([1,3,5,7,9], [2,4,6,8,10])) // [false, false, false, false, false]
console.log(solution([5,3,8,4,2,1,7,10], [1,2,6,8,10])) // [true, true, false, true, true]
