/**
 * p.271 24. 신고 결과 받기
 * 31m 49s
 */

function solution(id_list, report, k) {

    // 신고당한 유저 기준 
    // 피신고자: [신고자, 신고자]
    let getList = {};

    // 신고한 유저 기준 메일 전송 횟수
    // 신고자: 신고횟수
    let mailList = {};
    id_list.forEach(user => mailList[user]=0)

    // 신고당한 사람 정리
    for (let r of report){
        let [give, get] = r.split(' ');

        if(!getList[get]){getList[get]=[]}
        getList[get].push(give);
    }
    // console.log(JSON.stringify(getList));

    // 중복 제거
    for (let user in getList) {
        getList[user] = [...new Set(getList[user])]
    }
    // console.log(JSON.stringify(getList));

    // 메일 받을 횟수 정리
    for (let get in getList){
        if (getList[get].length >= k ) { getList[get].forEach(user => mailList[user]++) }
    }
    // console.log(JSON.stringify(mailList));

    return id_list.map(id => mailList[id]);
}

console.log(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) // [2,1,1,0]
console.log(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) // [0,0]
