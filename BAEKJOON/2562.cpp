#include <iostream>
using namespace std;

int main()
{
    int arr[9];             //정적으로 9개를 담는 배열을 선언 
    int max = 0;
    int num;

    for (int i = 0; i < 9; i++) { //9번 반복, 입력받으면서 비교
        cin >> arr[i];     
        if (arr[i] > max) { 	//입력 받을 때 마다 이전 값중에 가장 큰 값인지 확인
            max = arr[i];   	//arr[i]번째 값이 더 클경우 그 값을 max변수에 복사
            num = i+1;     	//i가 0부터 시작하여 +1을 해주어 몇번째 인지 나타냄
        }
    }
    cout << max << endl;
    cout << num;
}
