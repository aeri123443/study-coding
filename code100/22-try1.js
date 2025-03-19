/**
 * p.257 22. 오픈채팅방
 * 14m 11s
 */
 

function solution(record) {
    let answer = [];
    let users = {}; // id:name

    // 최종 이름 확인
    for (let r of record){
        r = r.split(' ');
        if ( r[0] === 'Enter' || r[0] === 'Change' ) {
            users[ r[1] ] = r[2];
        }
    }

    // 결과물 
    for (let r of record){
        r = r.split(' ');
        if (r[0] == 'Enter') {
            answer.push( `${users[ r[1] ]}님이 들어왔습니다.` );
        } else if (r[0] == 'Leave') {
            answer.push( `${users[ r[1] ]}님이 나갔습니다.` );
        }
    }
    return answer;
}

console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
//["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
