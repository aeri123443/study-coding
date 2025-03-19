/**
 * p.251 21. 할인 행사
 */
 

function solution(want, number, discount) {
    let answer = 0;
    let basket = {};
    
    want.map( (w, i) => basket[w]=number[i]);
    // console.log(basket);

    for (let i=0; i<discount.length; i++){
        const item = discount[i];
        if (i>=10 && basket[discount[i-10]]!==undefined) { basket[discount[i-10]]++; }
        if (basket[item]!==undefined) {
            basket[item]--;
            if (i>=9 && basket[item]===0) {
                let flag = true;
                for(let x in basket) {
                    if(basket[x]>0){flag=false; break;}
                }
                if(flag){answer++;}
            }
        }

        // console.log(basket);
    }

    return answer;
}

console.log(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) // 3
console.log(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])) // 0

