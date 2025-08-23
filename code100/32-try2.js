/**
 * p.342 32. 길찾기 게임
 * 53m 30s 
 * 효율성을 위해 재귀 대신 연결리스트로
 * 원래 전위후위탐색은 재귀가 편하긴 함!!
 */

//노드
class Node{
    constructor(info, num, left=null, right=null){
        this.info = info; // 좌표
        this.left = null;
        this.right = null;
        this.num = num; // 번호(이름)
    }
}

// 이진트리 구현
function makeBT(root, nodes){
    for(const node of nodes){
        if(!root){
            root = new Node([node[0], node[1]], node[2]); 
            continue;
        }
        let pointer = root;
        const newNode = new Node([node[0], node[1]], node[2]);
        while(true){
            if( newNode.info[0] < pointer.info[0] ){
                if(!pointer.left){ // 왼쪽에 값이 없으면
                    pointer.left = newNode;
                    break;
                } else { // 왼쪽에 값이 있으면
                    pointer = pointer.left;
                }
            } else {
                if(!pointer.right){ // 왼쪽에 값이 없으면
                    pointer.right = newNode;
                    break;
                } else { // 왼쪽에 값이 있으면
                    pointer = pointer.right;
                }
            }
        }
        
    }
    return root;
}

// 전위 순회
function preOrder(root){
    const stack = [];
    const result = [];
    stack.push(root);

    while(stack.length){
        const pointer = stack.pop();
        result.push(pointer.num);
        if(pointer.right){stack.push(pointer.right)}
        if(pointer.left){stack.push(pointer.left)}
    }
    return result
}

// 후위 순회
function postOrder(root){
    const stack = [];
    const result = [];
    const order = [] // 검사용
    stack.push([root, false]);
    order.push(root.num+"F")
    while(stack.length){
        const [pointer, visited] = stack.pop();
        order.pop();
        // console.log(pointer)
        if(visited){result.push(pointer.num);}
        else{
            stack.push([pointer, true]);
            order.push(pointer.num+"T")
            if(pointer.right){stack.push([pointer.right, false]); order.push(pointer.right.num+"F")}
            if(pointer.left){stack.push([pointer.left, false]); order.push(pointer.left.num+"F")} 
        }
        // console.log(order)
        // console.log(" ")
    }
    return result
}

function solution(nodeinfo){
    // 정렬
    const nodes = nodeinfo.map( ([x,y],i) => [x,y,i+1]); // [x, y, num]
    nodes.sort((a,b) => (a[0]-b[0])).sort((a,b)=>b[1]-a[1]);
    // console.log(JSON.stringify(nodes))

    // 트리 만들기
    let root = null;
    root = makeBT(root, nodes);
    // console.log(root.left.right.num)

    // 전위
    let preResult = preOrder(root)
    // console.log(preResult);

    // 후위

    let postResult= postOrder(root);
    // console.log(postResult)

    return [preResult, postResult];
}
console.log(JSON.stringify(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])));
//[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
