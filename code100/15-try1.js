/**
 * p.104 15. 요세푸스 문제
 * 14m 11s
 */
 
function solution(N, K){
    let size = N;
    let queue = [...new Array(N)].map( (_,i)=> i+1 );

    // while size===1
    // k-1칸 shift -> push 이동
    // shift
    while (size>1) {
        for(let i=0; i<K-1; i++){
            queue.push( queue.shift() );
        }
        queue.shift();
        size--;
        // console.log(queue);
    }

    return queue[0];
}

console.log(solution(5, 2)); //3
