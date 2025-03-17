/**
 * p.215 17. 카드 뭉치
 * 6m 45s (문제 이해시간 제외)
 * 큐 활용해보기
 */

class Queue{
    constructor(data){
        this.items = data;
        this.front = 0;
        this.rear = data.length;
    }

    pop(){
        if(this.front===this.rear) {return null;}
        return this.items[ this.front++ ];
    }

    first(){
        return this.items[ this.front ]
    }
}
 
function solution(cards1, cards2, goal) {

    let c1 = new Queue(cards1);
    let c2 = new Queue(cards2);
    let g = new Queue(goal);

    for (let i=0; i<goal.length; i++){
        if ( c1.first() === g.first() ) {
            c1.pop();
            g.pop()
        } else if ( c2.first() === g.first() ) {
            c2.pop();
            g.pop();
        } else {return 'No'}
    }

    return 'Yes';
    
}

console.log(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])); //Yes
console.log(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])); //No
console.log(solution(["drink", "water"], ["i", "want", "to"], ["i", "want", "to", "drink", "water"])); //Yes
console.log(solution(["i", "drink", "water"], ["to", "want"], ["i", "want", "to", "drink", "water"])); //No
