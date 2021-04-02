#include <iostream>
using namespace std;

int main()
{
	int n;	//테스트 케이스 수
	cin >> n;

	for (int i = 0; i < n; i++) {//테스트 케이스만큼 반복
		int num = 0;		//학생 수
		int sum = 0;		//점수 합계
		int count = 0;		//평균보다 클 경우 count
		double avg = 0;		//평균

		cin >> num;			//학생 수 입력
		int arr[num];			//입력한 학생 수 만큼 배열 만들기
		
		for (int j = 0; j < num; j++) {	//학생 수만큼 반복
			cin >> arr[j];
			sum += arr[j];		//입력된 점수 합하기
		}
		avg = sum / num;		//학생들의 평균 구하기
		
		for (int j = 0; j < num; j++) {	//점수가 평균보다 높을 경우 cout +1
			if (arr[j] > avg) {			
				count ++;
			}
		}
		printf("%.3f%%\n", (float)count / num * 100); //비율 출력
	}
}
