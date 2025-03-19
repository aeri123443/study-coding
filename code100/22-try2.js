/**
 * p.257 22. 오픈채팅방
 * 짧게 풀어보기 (매핑 활용)
 */
 
function solution(record) {
    let log = [];
    let users = {}; // id:name
    const stateMapping = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }

    record.forEach( (r) => {
        const [state, id, name] = r.split(' ');
        if( state !== 'Leave' ) { users[id]=name; }
        if( state !== 'Change' ) { log.push([state, id])}
    })

    return log.map( ([state, id]) => `${users[id]}${stateMapping[state]}`);
}

console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
//["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
