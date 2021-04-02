#include <iostream>
#include<vector>
using namespace std;

long long sum(vector<int>& a) {
	long long ans = 0;
    
    //배열의 크기만큼 반복하여 a[i]를 더합니다.
	for (int i = 0; i < a.size(); i++) {
		ans += a[i];
	}
    
	return ans;
}
