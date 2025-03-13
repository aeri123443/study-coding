/**
 * 자바스크립트로 큐 구현하기
 * p.200
 */

class Queue {
    items = [];
    front = 0;
    rear = 0;

    push(item){
        this.items.push(item);
        this.rear++;
    }

    pop(){
        // 앞의 요소를 팝한 후 front를 1 증가시킴
        return this.items[this.front++];
    }

    isEmpty(){
        return this.front===this.rear;
    }
}

let q = new Queue;

console.log(q.isEmpty());

q.push('a');
q.push('b');
q.push('c');

console.log(q.pop());
console.log(q.pop());
console.log(q.isEmpty());

console.log(q.pop());
console.log(q.isEmpty());

// true
// a
// b
// false
// c
// true
