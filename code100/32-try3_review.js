/**
 * p.342 32. 길찾기 게임
 * 53m 00s
 */

class Node{
    constructor(name, info, left=null, right=null){
        this.name = name;
        this.info = info;
        this.left = left;
        this.right = right;
    }
}

function makeBT(items){
    let root = null;
    for(const [itemName, itemInfo] of items){
        // 첫 노드는 바로 배치
        if (!root){
            root = new Node(itemName, itemInfo);
            continue;
        }
        // 노드 비교하며 내려가기
        let pointer = root;
        while(true){
            if(itemInfo[0] < pointer.info[0]){
                if(pointer.left){
                    pointer = pointer.left;
                } else{
                    pointer.left = new Node(itemName, itemInfo);
                    break;
                } 
            } else{
                if(pointer.right){
                    pointer = pointer.right;
                } else{
                    pointer.right = new Node(itemName, itemInfo);
                    break;
                } 
            }
        }
    }
    return root
}

// 전위 순회
function preOrder(pointer, answer){
    // console.log(pointer)
    if(pointer){
        answer.push(pointer.name);

        preOrder(pointer.left, answer);
        preOrder(pointer.right, answer);
    }
    return answer;
}

// 후위 순회
function postOrder(pointer, answer){
    // console.log(pointer)
    if(pointer){

        postOrder(pointer.left, answer);
        postOrder(pointer.right, answer);
        answer.push(pointer.name);

    }

    return answer;
}

function solution(nodeinfo){
    // 라벨 추가 및 데이터 정렬
    let items = nodeinfo.map( (v,i)=>[i+1, v])
    items.sort((a,b)=>a[1][0]-b[1][0]).sort((a,b)=>b[1][1]-a[1][1]);
    // console.log(JSON.stringify(items));

    // x를 비교해가며 트리 만들기
    let root = makeBT(items);
    // console.log(root.left.right.right.name)

    const preOrderAnswer = preOrder(root, [])
    const postOrderAnswer = postOrder(root, [])

    return [preOrderAnswer, postOrderAnswer];
}

console.log(JSON.stringify(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])));
//[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
