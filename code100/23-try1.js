/**
 * p.265 23. 베스트 앨범
 */

function solution(genres, plays) {
    let playlists = {};
    let genreTotal = {};
    let answer = [];

    for (let i=0; i<genres.length; i++){
        const genre = genres[i];
        const play = plays[i];

        // 장르별 합산
        genreTotal[genre] = (genreTotal[genre] || 0) + play;
        
        // 플레이리스트 추가
        let tmpObj = (playlists[genre] || {});
        tmpObj[i]=play;
        playlists[genre] = tmpObj;
    }

    // 장르 정렬
    genreTotal = Object.entries(genreTotal).sort( (a,b) => b[1]-a[1]);

    // 장르별 노래 정렬
    for (let [genre, _] of genreTotal){
        let songs = Object.entries(playlists[genre]);
        if (songs.length <= 1) {answer.push(Math.floor(songs[0][0]))} 
        else {
            songs = songs.sort( (a,b) => b[1]-a[1]);
            answer = [...answer, Math.floor(songs[0][0]), Math.floor(songs[1][0])];
        }

    }

    return answer;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) // [4, 1, 3, 0]
console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500])) // [4, 1, 0, 3]
console.log(solution(["classic", "pop", "classic", "music", "classic", "pop"], [500, 600, 150, 430, 500, 2500])) // [5, 1, 0, 4, 3]
