/**
 * p.135 07. 방문 길이
 * 소요시간: 34m 57s
 */

function solution(dirs) {

    // (0,0) 시작
    let x = 0;
    let y = 0;
    let path = [];

    for (let k of dirs){
        // console.log(k);
        // 5를 넘어갈경우 계산값 무시
        // x, y +- 1
        if ( (k === 'U') && (y<5) ) { y+=1; path.push(`(${x}, ${y-1})(${x}, ${y})`); }
        else if ( (k === 'D') && (y>-5) ) { y-=1; path.push(`(${x}, ${y})(${x}, ${y+1})`); }
        else if ( (k === 'R') && (x<5) ) { x+=1; path.push(`(${x-1}, ${y})(${x}, ${y})`); }
        else if ( (k === 'L') && (x>-5) ) { x-=1; path.push(`(${x}, ${y})(${x+1}, ${y})`); };
        // console.log(x, y)
    }
    
    path = [...new Set(path)];
    return path.length;
}
console.log(solution("ULURRDLLU"));
console.log(solution("LULLLLLLU"));
console.log(solution("LULLLLLLRR"));
console.log(solution("UUDD"));
