/**
 * p.369 33. 유니온-파인드 알고리즘 구현하기
 */

// 루트 노드 찾는 함수
function find(parents, x) {
    if(parents[x]===x){return x}

    parents[x] = find(parents, parents[x])
    return parents[x];
}

// 두 개의 집합을 합치는 함수
function union(parents, x, y) {
    const root1 = find(parents, x);
    const root2 = find(parents, y);
    
    parents[root2] = root1
}

function solution(k, operations) {
    const parents = Array.from( {length: k}, (_,i) => i);
    let n = k

    for(const op of operations){
        if(op[0]==='u'){
            union(parents, op[1], op[2]);
        }else if(op[0]==='f'){
            find(parents, op[1]);
        }
    }

    n = new Set(parents).size;
    return n
}

console.log(solution(3,[['u', 0, 1], ['u', 1, 2], ['f', 2]])) // 반환값 : 1
console.log(solution(4,[['u', 0, 1], ['u', 2, 3], ['f', 0]])) // 반환값 : 2