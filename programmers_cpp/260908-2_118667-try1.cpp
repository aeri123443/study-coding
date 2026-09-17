#include <iostream> 
#include <string>
#include <vector>
#include <numeric>

using namespace std;

// 투포인터로 후보 범위 반환
vector<pair<int, int>> get_candidate_range(vector<int> q, long long target_sum){
    vector<long long> prefix_sum;
    prefix_sum.reserve(q.size()+1);

    prefix_sum.push_back(0);
    for (int idx=0; idx < q.size(); idx++){
        prefix_sum.push_back(prefix_sum.back()+q[idx]);
    }

    vector<pair<int, int>> result;
    result.reserve(prefix_sum.size()+1);

    int i=0, j=0;
    while ( 0 <= j && j < prefix_sum.size() && 
            0 <= i && i < prefix_sum.size() ){

        long long cur_diff = prefix_sum[j] - prefix_sum[i];

        if (cur_diff > target_sum){
            i += 1;
        } else if (cur_diff < target_sum) {
            j += 1;
        } else {
            result.push_back({i, j});
            j += 1;
        }
    }

    return result;
}

int get_least_cal(vector<pair<int, int>> candidate_range, int sj){
    int result = 1e9;

    for (int idx=0; idx<candidate_range.size(); idx++){
        int ei=candidate_range[idx].first, ej=candidate_range[idx].second;

        if (ej < sj) continue;
        result = min(result, ei+ej);
    }

    if (result != 1e9){
        return result - sj;
    } else {
        return -1;
    }
}

int solution(vector<int> queue1, vector<int> queue2) {
    // 타겟합 구하기
    long long target_sum = accumulate(queue1.begin(), queue1.end(), 0LL) + accumulate(queue2.begin(), queue2.end(), 0LL);
    if( (target_sum % 2) != 0 ) { return -1; }
    target_sum /= 2;

    // 투포인터로 후보 범위 반환
    vector<int> q;
    q.reserve(queue1.size()*2 + queue2.size());
    q.insert(q.end(), queue1.begin(), queue1.end());
    q.insert(q.end(), queue2.begin(), queue2.end());
    q.insert(q.end(), queue1.begin(), queue1.end());

    vector<pair<int, int>> candidate_range = get_candidate_range(q, target_sum);

    // 후보 범위 중 가장 연산 수가 적은 경우를 반환 
    
    if (candidate_range.size() == 0) return -1;
    int answer = get_least_cal(candidate_range, queue1.size());

    return answer;
}


int main() {
    // 함수의 결과를 변수에 저장한 뒤 출력

    cout << solution({3, 2, 7, 2}, {4, 6, 5, 1}) << "\n";
    cout << solution({1, 2, 1, 2}, {1, 10, 1, 2}) << "\n";
    cout << solution({1, 1}, {1, 5}) << "\n";

    return 0;
}