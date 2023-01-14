import UIKit

/*
 [ 소인수분해 ]
 
    소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
 
 입출력 예 #1
 12를 소인수분해하면 2 * 2 * 3 입니다. 따라서 [2, 3]을 return합니다.
 
 입출력 예 #2
 17은 소수입니다. 따라서 [17]을 return 해야 합니다.
 
 입출력 예 #3
 420을 소인수분해하면 2 * 2 * 3 * 5 * 7 입니다. 따라서 [2, 3, 5, 7]을 return합니다.
 
 소수(Prime Number)란 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수
 
 만약 n까지의 소수를 구하라면
 단순히 나누어 떨어지는지 확인해 보았을 때 O(n)이므로 비효율적이다
 약수는 대칭적이기때문에 제곱근 즉, 가운데 수까지만 확인해도 O(n^1/2)이라 비효율적이다.
 에라토스테네스의 체는 2부터 자연수를 쓴 후 2, 3, 4...n의 배수를 지워나간다 -> O(nloglogn)
 */

import Foundation

// n까지 소수 구하기
func solution_prime(_ n:Int) -> [Int] {
    var arr = Array(repeating: true, count: n+1)
    var primes = [Int]()
    
    for i in 2..<n {
        if arr[i] == true {
            for j in stride(from: i, through: n, by: i) {
                arr[j] = false
            }
            primes.append(i)
        }
    }
    
    return primes

}
print(solution_prime(17))

// n 을 소인수분해하기 + 오름차순 + 중복제거
func solution_prime_factorization(_ n:Int) -> [Int] {
    var primes = [Int]()
    var num = n
    for i in 2...n {
         while num % i == 0 {
            primes.append(i)
            num /= i
        }
    }
    return Set(primes).sorted()
}

print(solution_prime_factorization(12))
print(solution_prime_factorization(17))


/*
[ 컨트롤 제트 ]
 
 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다.
 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

 입출력 예 #2
 10 + 20 + 30 + 40 = 100을 return 합니다.
 
 입출력 예 #3
 "10 Z 20 Z 1"에서 10 다음 Z, 20 다음 Z로 10, 20이 지워지고 1만 더하여 1을 return 합니다.
 */

func solution_control_z(_ s:String) -> Int {
    
    var array = s.components(separatedBy: " ")
    var result = 0

    for i in 0..<array.count {
        if array[i] != "Z" {
            result += Int(array[i])!
        } else {
            result -= Int(array[i - 1])!
        }
    }
    return result
}

print(solution_control_z("1 2 Z 3")) // 1, 3 = 4
print(solution_control_z("10 20 30 40")) // 100
print(solution_control_z("10 Z 20 Z 1")) // 1
print(solution_control_z("10 Z 20 Z")) // 0
print(solution_control_z("-1 -2 -3 Z")) //-3


/*
 [ 한 번만 등장한 문자 ]
 문자열 s가 매개변수로 주어집니다.
 s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
 
 입출력 예
 s    result
 "abcabcadc"    "d"
 "abdc"    "abcd"
 "hello"    "eho"
 */

func solution_1_char(_ s:String) -> String {
    let dic = Dictionary(s.map{($0, 1)},uniquingKeysWith: +)
    var array = [Character]()
    for (key, value) in dic {
        if value == 1 {
            array.append(key)
        }
    }
    return String(array.sorted())
}

print(solution_1_char("abcabcadc"))
print(solution_1_char("s"))
print(solution_1_char("abdc"))
print(solution_1_char("hello"))
