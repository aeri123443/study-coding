/**
 * 순열과 조합
 */

// 조합
function combination(arr, selectNum){
    if (selectNum===1){return arr.map(x=>[x])}

    let result = [];
    let lastIdx = arr.length-1;
    arr.forEach((item, idx)=>{
        if(idx===lastIdx){return}

        const remain = arr.slice(idx+1);
        const recall = combination(remain, selectNum-1);
        const attach = recall.map(x=>[item, ...x]);
        result.push(...attach);
    })
    return result;
}

console.log(JSON.stringify(combination([1,2,3,4], 3)))
// [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]

// 순열
function permutation(arr, selectNum){
    if(selectNum===1){return arr.map(x=>[x])}

    let result=[]
    arr.forEach( (item, idx) => {
        const remain = [...arr.slice(0, idx), ...arr.slice(idx+1)];
        const recall = permutation(remain, selectNum-1);
        const attach = recall.map(x=>[item, ...x]);

        result.push(...attach);
    })
    return result;
}

console.log(JSON.stringify(permutation([1,2,3,4], 3)))
console.log(permutation([1,2,3,4], 3).length)
// [[1,2,3],[1,2,4],[1,3,2],[1,3,4],[1,4,2],[1,4,3],[2,1,3],[2,1,4],[2,3,1],[2,3,4],[2,4,1],[2,4,3],[3,1,2],[3,1,4],[3,2,1],[3,2,4],[3,4,1],[3,4,2],[4,1,2],[4,1,3],[4,2,1],[4,2,3],[4,3,1],[4,3,2]]
// 24
