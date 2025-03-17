/**
 * p.215 17. 카드 뭉치
 * 10m 14s
 */
 
function solution(cards1, cards2, goal) {

    for( let i=0, j=0, n=0; n<goal.length; n++ ){
        if ( cards1[i]===goal[n] ) { i++; }
        else if ( cards2[j]===goal[n] ) { j++; }
        else {return 'No'}
    }
    return 'Yes';
}

console.log(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])); //Yes
console.log(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])); //No
console.log(solution(["drink", "water"], ["i", "want", "to"], ["i", "want", "to", "drink", "water"])); //Yes
console.log(solution(["i", "drink", "water"], ["to", "want"], ["i", "want", "to", "drink", "water"])); //No
