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
print("=================================================")

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
print("=================================================")
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
    
    let array = s.components(separatedBy: " ")
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
print("=================================================")

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
print("=================================================")

/*
 [ 이진수 더하기 ]
 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때,
 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
 
 입출력 예
 bin1    bin2    result
 "10"    "11"    "101"
 "1001"    "1111"    "11000"
 */

func solution_binary_sum(_ bin1:String, _ bin2:String) -> String {
    let sum = Int(bin1, radix: 2)! + Int(bin2, radix: 2)!
    return String(sum, radix: 2)
}

print(solution_binary_sum("10", "11"))
print(solution_binary_sum("1001", "1111"))
print("=================================================")

/*
 [ 7의 개수 ]
 
 머쓱이는 행운의 숫자 7을 가장 좋아합니다.
 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
 
 입출력 예
 array    result
 [7, 77, 17]    4
 [10, 29]    0
 */

func solution_count_7(_ array:[Int]) -> Int {
    var count = 0
    for item in array {
        let array = Array(String(item))
        count += array.filter{$0 == "7"}.count
    }
    
    return count
}

print(solution_count_7([7, 77, 17]))
print(solution_count_7([10, 29]))
print("=================================================")


/*
 [ 숨어있는 숫자의 덧셈 (2) ]
 
 문자열 my_string이 매개변수로 주어집니다.
 my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
 my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

 연속된 수는 하나의 숫자로 간주합니다.
 
 입출력 예
 my_string    result
 "aAb1B2cC34oOp"    37
 "1a2b3c4d123Z"    133
 */

func solution_sum_hidden_num(_ my_string:String) -> Int {
    // 이 방법보단... 문자열을 replace "" 하고 split 해서 더해주는게 더 좋지 않았을까t
    let ascii = Int(UnicodeScalar("9").value)
    let arr = Array(my_string)
    
    var i = 0
    var result = 0
    while (i < arr.count) {
        if arr[i].asciiValue! <= ascii {
            var j = 1
            var str  = String(arr[i])
            while(i + j < arr.count && arr[i + j].asciiValue! <= ascii) {
                str += String(arr[i + j])
                j += 1
            }
            result += Int(str)!
            i += j
        }
        i += 1
    }
    return result
    
}

print(solution_sum_hidden_num("aAb1B2cC34oOp"))
print(solution_sum_hidden_num("1a2b3c4d123Z"))
print("=================================================")

/*
 [ 영어가 싫어요 ]

 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
 
 입출력 예
 numbers    result
 "onetwothreefourfivesixseveneightnine"    123456789
 "onefourzerosixseven"    14067
 */

func solution_en_to_num(_ numbers:String) -> Int64 {
    let arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    var str = numbers
    
    for i in 0..<arr.count{
        str = str.replacingOccurrences(of: arr[i], with: "\(i)")
    }
    return Int64(str)!
}

print(solution_en_to_num("onetwothreefourfivesixseveneightnine"))
print(solution_en_to_num("onefourzerosixseven"))
print("=================================================")

/*
 [ 문자열 계산하기 ]

 my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

 입출력 예
 my_string    result
 "3 + 4"    7
 */

func solution_cal_string(_ my_string:String) -> Int {
    let arr = my_string.split(separator: " ")
    var result = Int(arr[0])!
    for i in arr.enumerated() {
        if i.element == "+" {
            result += Int(arr[i.offset + 1])!
        }
        if i.element == "-" {
            result -= Int(arr[i.offset + 1])!
        }
    }
    return result
}

print(solution_cal_string("3 + 4"))
print("=================================================")

/*
 [ OX퀴즈 ]

 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

 입출력 예
 quiz    result
 ["3 - 4 = -3", "5 + 6 = 11"]    ["X", "O"]
 ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]    ["O", "O", "X", "O"]
 */

func solution_OX_quiz(_ quiz:[String]) -> [String] {
    var result = [String]()
    for item in quiz {
        let arr = item.split(separator: " ")
        var cal = 0

        if arr[1] == "+" {
            cal = Int(arr[0])! + Int(arr[2])!
        } else {
            cal = Int(arr[0])! - Int(arr[2])!
        }
        
        if Int(arr[4])! == cal {
            result.append("O")
        }else {
            result.append("X")
        }
    }
    return result
}

print(solution_OX_quiz(["3 - 4 = -3", "5 + 6 = 11"]))
print("=================================================")
