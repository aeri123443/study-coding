/**
 * p.342 32. 길찾기 게임
 * 122m 13s 효율성 out 재귀 빼기
 */

function solution(nodeinfo) {
    // 트리 배열 크기 지정
    // 인덱스 번호+1 추가
    const ySet = new Set();
    const nodeIndex = []; //인덱스+1, x값, y값
    nodeinfo.map( ([x,y], i) => {ySet.add(y); nodeIndex.push([i+1, x, y])});
    
    // 트리 만들기
    const treeDepth = ySet.size;
    let tree = new Array(2**treeDepth).fill(0);

    // y축 내림차순 -> x축 오름차순 정렬
    let nodeArray = [...nodeIndex]
    nodeArray.sort((a,b)=>a[1]-b[1]).sort((a,b)=>b[2]-a[2]);
    // console.log(JSON.stringify(nodeArray));

    // 트리 생성
    for(const node of nodeArray){
        if(tree[1]===0){tree[1]=node; continue;}
        let n=0;
        while(n<tree.length){
            if( node[1] < tree[n][1] ){
                if(tree[2*n]===0){tree[2*n]=node; break;}
                else{n=2*n}
            } else {
                if(tree[2*n+1]===0){tree[2*n+1]=node;break;}
                else{n=2*n+1}
            }
        }
    }
    // console.log(JSON.stringify(tree))

    // 전위 순회
    let preorderResult = [];
    function preorder(idx){
        // console.log(idx)
        if(idx >= tree.length ){return}
        const name = tree[idx][0]
        preorderResult.push(name)

        // preorder(idx, str)
        if(tree[idx*2]!==0){preorder(idx*2)}
        if(tree[idx*2+1]!==0){preorder(idx*2+1)}
    }
    preorder(1);
    // console.log(preorderResult);
    
    // 후위 순회
    let postorderResult = [];
    function postorder(idx){
        // console.log(idx)
        if(idx >= tree.length ){return}
        const name = tree[idx][0]
        // console.log(idx, name)

        // postorder(idx, str)
        if(tree[idx*2]!==0){postorder(idx*2)}
        if(tree[idx*2+1]!==0){postorder(idx*2+1)}
        postorderResult.push(name)

    }
    postorder(1);
    // console.log(postorderResult);

    return [preorderResult, postorderResult]
}

console.log(JSON.stringify(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])));
//[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
