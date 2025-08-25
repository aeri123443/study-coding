/**
 * p.376 35. 영어 끝말잇기
 * 22m 52s
 */

function solution(n, words) {

    const wordSet = new Set();

    for(let i=0; i<words.length; i++){
        if(wordSet.size===0){wordSet.add(words[i]); continue;}
        
        // 중복된 단어인지 확인
        // 끝글자 - 앞글자 같은지 확인
        const lastWord = words[i-1];
        const recentWord = words[i];
        if(wordSet.has(words[i]) || lastWord[lastWord.length-1]!==recentWord[0]){
        // 턴, 사람 리턴
            return [i%n+1, Math.ceil((i+1)/n)]
        } else {
            wordSet.add(words[i]);
        }
    }
    return [0,0]

}

// [3,3]
console.log(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
// [0,0]
console.log(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) // 3
// // [1,3]
console.log(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
