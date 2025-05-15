/**
 * p.311 27. 이진 탐색 트리 구현
 * 교재답안 따라하기
 */

class Node{
    constructor(key){
        this.left = null;
        this.right = null;
        this.val = key;
    }
}

class BST {
    constructor(){
        this.root = null;
    }

    insert(key){
        if(!this.root){
            this.root = new Node(key);
        } else {
            let curr = this.root;
            while(true){
                if(key<curr.val){
                    if(curr.left){
                        curr = curr.left;
                    } else {
                        curr.left = new Node(key);
                        break;
                    }
                } else {
                    if(curr.right){
                        curr = curr.right;
                    } else {
                        curr.right = new Node(key);
                        break;
                    }
                }
            }
        }
    }

    search(key) {
        let curr = this.root;

        while (curr && curr.val!==key){
            if (key < curr.val){
                curr = curr.left;
            } else {
                curr = curr.right;
            }
        }
        return curr;
    }
}

function solution(lst, searchList){
    let bst = new BST();

    for(x of lst) {bst.insert(x)}

    let answer = [];

    for(x of searchList){
        let searchResult = bst.search(x) ? true : false;

        answer.push(searchResult)
        
    }
    return answer;
}

console.log(solution([5,3,8,4,2,1,7,10], [1,2,5,6])) // [true, true, true, false]
console.log(solution([1,3,5,7,9], [2,4,6,8,10])) // [false, false, false, false, false]
console.log(solution([5,3,8,4,2,1,7,10], [1,2,6,8,10])) // [true, true, false, true, true]
