/**
 * p.265 23. 베스트 앨범
 * 교재대로 풀어보기
 * 같은 맥락이나 플레이리스트에 배열을 그대로 넣어도 됨, 
 * slice, map으로 깔끔하게 푸시하기
 * 장르 내 노래 정렬시 인덱스도 고려하기
 */

function solution(genres, plays) {
    let answer = [];
    let playlists = {};
    let total = {};

    for (let i=0; i<genres.length; i++){
        const genre = genres[i];
        const play = plays[i];

        if (!playlists[genre]) {
            playlists[genre] = [];
            total[genre] = 0;
        }

        playlists[genre].push([i, play]);
        total[genre] += play;
    }

    // console.log(JSON.stringify(playlists))
    // console.log(JSON.stringify(total))

    // 장르 정렬
    const sortedGenre = Object.keys(total).sort( (a,b) => total[b]-total[a]);
    // console.log(sortedGenre);

    // 장르 별 노래 정렬
    for (let genre of sortedGenre){
        let tmp = playlists[genre].sort( (a,b) => b[1]-a[1] ).slice(0,2).map(a=>a[0])
        // console.log(JSON.stringify(tmp))
        answer.push(...tmp)

    }
    
    return answer;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) // [4, 1, 3, 0]
console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500])) // [4, 1, 0, 3]
console.log(solution(["classic", "pop", "classic", "music", "classic", "pop"], [500, 600, 150, 430, 500, 2500])) // [5, 1, 0, 4, 3]
