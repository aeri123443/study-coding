class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class Queue{
    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    push(data){
        const newNode = new Node(data);

        if(!this.head){
            this.head = newNode;
            this.tail = newNode;
        } else{
            this.tail.next = newNode;
            this.tail = newNode;
        }

        this.size++;
    }

    pop(){
        if (!this.head){
            return null;
        }

        const removeNode = this.head;
        this.head = this.head.next;

        if (!this.head){
            this.tail = null;
        }

        this.size--;

        return removeNode.data;
    }

    isEmpty(){
        return this.size === 0;
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
