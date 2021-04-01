#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int ary[n + 1];

	int min, max;

	min = 1000000;
	max = -1000000;

	for (int i = 0; i < n; i++) {
		cin >> ary[i];

		if (min > ary[i]) {
			min = ary[i];
		}
		if (max < ary[i]) {
			max = ary[i];
		}
	}
	cout << min << " " << max;
}
