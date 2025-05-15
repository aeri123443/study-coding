/**
 * p.319 29. 다단계 칫솔 판매
 * 43m 58s
 */

function solution(enroll, referral, seller, amount) {
    let member = {}; // 피영업자 : [수익, 영업자]

    for (let i=0; i<enroll.length; i++){
        member[enroll[i]] = [0, referral[i]];
    }

    for (let i=0; i<seller.length; i++){
        let a = amount[i]*100;
        let child = seller[i];

        let profit = Math.floor(a/10);
        while(true){
            member[child][0] += (a-profit);
            a = profit;
            profit = Math.floor(profit/10);
            child = member[child][1];
            if (a < 1 || child==='-') { break; }
        }
        // console.log(JSON.stringify(member))
    }
    return enroll.map(x=>member[x][0]);
}

console.log(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
)) // [360, 958, 108, 0, 450, 18, 180, 1080]
console.log(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4]
)) // [0, 110, 378, 180, 270, 450, 0, 0]