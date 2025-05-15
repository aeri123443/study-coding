/**
 * p.308 26. 트리 순회
 * 차일 안보고 해보기
 */

function preorder(nodes, idx){
    if(idx < nodes.length){
        let ret = `${nodes[idx]}`;
        ret += preorder(nodes, idx*2+1);
        ret += preorder(nodes, idx*2+2);

        return ret;
    }

    return '';
}

function inorder(nodes, idx){
    if(idx<nodes.length){
        let ret = ''
        ret += inorder(nodes, idx*2+1);
        ret += nodes[idx];
        ret += inorder(nodes, idx*2+2);

        return ret;
    }

    return '';
}

function postorder(nodes, idx){
    if(idx<nodes.length){
        let ret = ''
        ret += postorder(nodes, idx*2+1);
        ret += postorder(nodes, idx*2+2);
        ret += nodes[idx];

        return ret;
    }

    return '';
}

function solution(nodes) {
    return [
        preorder(nodes, 0), 
        inorder(nodes, 0), 
        postorder(nodes, 0)
    ];
}

console.log(solution([1,2,3,4,5,6,7])) // ['1245367', '4251637', '4526731']
