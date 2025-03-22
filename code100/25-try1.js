/**
 * p.278 25. 메뉴 리뉴얼
 * 69m 23s
 */

function combination(arr, selectNum){
    if (selectNum===1){return arr.map(x=>[x])}

    const lastIdx = arr.length-1;
    let result = [];

    arr.forEach ((item, idx) => {
        if (idx===lastIdx){return}

        const remain = arr.slice(idx+1);
        const recall = combination(remain, selectNum-1);
        const attach = recall.map(x=>[item, ...x]);

        result.push(...attach);
    })

    return result;
}

function solution(orders, course) {
    let answer = [];
    
    for (let c of course){
        let menu = {};

        for (let o of orders){
            let sorted = [...o].sort();
            
                const com = combination(sorted, c).map(x=>x.join(''));
                com.forEach( item => menu[item] = menu[item] ? menu[item]+1 : 1 );
        }

        const maxNum = Math.max(...Object.values(menu));
        if (maxNum>=2){
            for (let m in menu) {
                if(menu[m]===maxNum){
                    answer.push(m)
                }
            }
        }

    }

    return answer.sort();
}

console.log(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])) // ["AC", "ACDE", "BCFG", "CDE"]
console.log(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) // ["ACD", "AD", "ADE", "CD", "XYZ"]
console.log(solution(["XYZ", "XWY", "WXA"], [2,3,4])) // ["WX", "XY"]
console.log(solution(["XYZ", "XWY", "WXA"], [2])) // ["WX", "XY"]
