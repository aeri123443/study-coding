/**
 * p.244 19. 문자열 해싱을 이용한 검색 함수 만들기
 * 24m 54s
 * 향후 시간복잡도에 대한 이해가 필요함.
 */
 
function strHash(str){
    let hash = 0;
    const p = 31;
    const m = 1000000007;

    for(let i=0; i<str.length; i++){
        const strCode = str.charCodeAt(i)-97;
        
        // hash += (strCode * (p**i)) % m ;
        hash = (hash*p + strCode) % m ;
    }

    return hash ;
}

function countSort(arr){
    let sortedArr = [];
    for (let x of arr){
        sortedArr[x] = 1;
    }

    return sortedArr;
}
function solution(stringList, queryList) {
    let stringHash = stringList.map( (str) => strHash(str));
    let queryHash = queryList.map( (str) => strHash(str));

    let hashTable = countSort(stringHash);

    let answer=[];

    for (let num of queryHash){
        let b = hashTable[num]===1 ? true : false;
        answer.push(b)
    }


    return answer;
}

console.log(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"])) // t f f t
