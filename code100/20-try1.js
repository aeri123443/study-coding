/**
 * p.247 20. 완주하지 못한 선수
 * 15m 02s
 */
 

function solution(participant, completion) {

    let obj = {};

    for (let c of completion){
        if (obj[c]) {obj[c] += 1;}
        else {obj[c] = 1;}
    }

    for (let p of participant){
        if (obj[p] && obj[p]>0) {obj[p]-=1;}
        else {return p}
    }

    return null;
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) // "leo"
console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) // "vinko"
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) // "mislav"
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "mislav"])) // "ana"
