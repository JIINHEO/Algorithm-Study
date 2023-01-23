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
<<<<<<< HEAD
 [ 삼각혁의 완성조건 (2) ]
 
 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

 입출력 예
 sides    result
 [1, 2]    1
 [3, 6]    5
 [11, 7]    13
 https://school.programmers.co.kr/learn/courses/30/lessons/120868
 */

func solution_triangle2(_ sides:[Int]) -> Int {
    let a = sides[0]
    let b = sides[1]
    let sum = a + b

    let max = a < b ? b : a
    let min = a < b ? a : b
    
    var result = 0
    // case1. 한 변이 sides에 있을 때
    for i in 0...sum {
        if max < min + i && min + i < sum {
            result += 1
        }
    }

    // case2. 한 변이 나머지 한 변일 때
    for _ in max..<sum {
        result += 1
    }

    return result
}


print(solution_triangle2([1, 2]))
print(solution_triangle2([3, 6]))
print(solution_triangle2([11, 7]))

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

/*
 [ 잘라서 배열로 저장하기 ]

 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

 입출력 예
 my_str    n    result
 "abc1Addfggg4556b"    6    ["abc1Ad", "dfggg4", "556b"]
 "abcdef123"    3    ["abc", "def", "123"]
 */

func solution_n_cut_array(_ my_str:String, _ n:Int) -> [String] {
      var arr = [String]()
      var str = ""
      
      for i in my_str.enumerated() {

          if i.offset % n == 0 && i.offset != 0{
              arr.append(str)
              str = ""
          }
          str += String(i.element)
          
          if my_str.count - 1 == i.offset {
              arr.append(str)
          }

      }
      return arr
}

print(solution_n_cut_array("abc1Addfggg4556b", 6))
print("=================================================")

/*
 [ 직사각형 넓이 구하기 ]

 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
 
 입출력 예
 dots    result
 [[1, 1], [2, 1], [2, 2], [1, 2]]    1
 [[-1, -1], [1, 1], [1, -1], [-1, 1]]    4
 
 https://school.programmers.co.kr/learn/courses/30/lessons/120860
 */

func solution_rec_area(_ dots:[[Int]]) -> Int {
    var x = [Int]()
    var y = [Int]()
    
    for i in dots {
        x.append(i[0])
        y.append(i[1])
    }
    
    let width = x.max()! - x.min()!
    let height = y.max()! - y.min()!
    
    return width * height
}

print(solution_rec_area([[1, 1], [2, 1], [2, 2], [1, 2]] ))
print("=================================================")

/*
 [ 캐릭터의 좌표 ]
 
 머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

 [0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
 
 입출력 예
 keyinput    board    result
 ["left", "right", "up", "right", "right"]    [11, 11]    [2, 1]
 ["down", "down", "down", "down", "down"]    [7, 9]    [0, -4]
 https://school.programmers.co.kr/learn/courses/30/lessons/120861
 */

func solution_cha_coordinate(_ keyinput:[String], _ board:[Int]) -> [Int] {
    var x = 0
    var y = 0
    
    let boardX = board[0] / 2
    let boardY = board[1] / 2
    
    for move in keyinput {
        switch move {
        case "left":
            if x > -boardX {
                x -= 1
            }
        case "right":
            if x < boardX {
                x += 1
            }
        case "up":
            if y < boardY {
                y += 1
            }
        case "down":
            if y > -boardY {
                y -= 1
            }
        default:
            print("")
        }
    }
    return [x, y]
}

print(solution_cha_coordinate( ["left", "right", "up", "right", "right"], [11, 11]))
print(solution_cha_coordinate( ["down", "down", "down", "down", "down"], [7, 9]))
print("=================================================")


/*
 [ 다항식 더하기 ]
 
 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.
 
 입출력 예
 polynomial    result
 "3x + 7 + x"    "4x + 7"
 "x + x + x"    "3x"
 https://school.programmers.co.kr/learn/courses/30/lessons/120863
 */

func solution_polynomial_add(_ polynomial:String) -> String {
    var x = 0
    var num = 0
    
    let arr = polynomial.split(separator: " ")
    
    for i in arr where !i.contains("+"){
        if i.contains("x"){
            if i == "x" {
                x += 1
            } else {
                let strX = i.replacingOccurrences(of: "x", with: "")
                x += Int(strX)!
            }
        } else {
            num += Int(i)!
        }
    }
    
    if x > 0 && num > 0{
        if x == 1 {
            return   "x + \(num)"
        }
        return  "\(x)x + \(num)"
    } else if x == 0 && num > 0{
        return   "\(num)"
    } else if x == 1 {
        return "x"
    }
    return "\(x)x"
}

print(solution_polynomial_add("3x + 7 + x"))
print(solution_polynomial_add("x + 7 + 1"))
print(solution_polynomial_add("1 + 7 + 1"))
print("=================================================")

/*
 [ 옹알이 (1) ]
 
 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
 
 입출력 예
 babbling    result
 ["aya", "yee", "u", "maa", "wyeoo"]    1
 ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]    3
 */

func solution_babbling(_ babbling:[String]) -> Int {
    var result = 0
    for items in babbling {
        var item = items
        item = item.replacingOccurrences(of: "aya", with: "-")
        item = item.replacingOccurrences(of: "ye", with: "-")
        item = item.replacingOccurrences(of: "woo", with: "-")
        item = item.replacingOccurrences(of: "ma", with: "-")
        item = item.replacingOccurrences(of: "-", with: "")
        if item == "" {
            result += 1
        }
    }
    return result
}

print(solution_babbling(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
print("=================================================")

/*
 [ 외계어 사전 ]
 
 PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
 
 입출력 예
 spell    dic    result
 ["p", "o", "s"]    ["sod", "eocd", "qixm", "adio", "soo"]    2
 ["z", "d", "x"]    ["def", "dww", "dzx", "loveaw"]    1
 ["s", "o", "m", "d"]    ["moos", "dzx", "smm", "sunmmo", "som"]    2
 */

func solution_spell_dic(_ spell:[String], _ dic:[String]) -> Int {
    var arr = [String]()
    for item in dic {
        if item.count == spell.count {
            arr.append(item)
        }
    }
    for item in arr {
        for j in spell.enumerated() {
            let count = item.components(separatedBy: j.element).count
            if  count != 2 {
                break
            }
            if j.offset == spell.count - 1{
                return 1
            }
        }
    }
    return 2
    
  /*
    func solution(_ spell: [String], _ dic: [String]) -> Int {
    dic.map { String($0.sorted()) }.contains(spell.sorted().joined()) ? 1 : 2 }
   */
}

print(solution_spell_dic( ["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution_spell_dic( ["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
print("=================================================")

/*
 [ 종이 자르기 ]
 
 머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
 
 입출력 예
 M    N    result
 2    2    3
 2    5    9
 1    1    0
 https://school.programmers.co.kr/learn/courses/30/lessons/120922?language=swift
 */

func solution_cut_paper(_ M:Int, _ N:Int) -> Int {
//    let max = M <= N ? M : N
//    let min = M <= N ? N : M
//
//    return (max - 1) + (max * (min - 1))
    // m - 1 + mn - m  = nm - 1
    return M * N - 1
}

print(solution_cut_paper(2, 2))
print(solution_cut_paper(2, 5))
print(solution_cut_paper(1, 1))
print("=================================================")

/*
 [ 로그인 성공? ]
 
 머쓱이는 프로그래머스에 로그인하려고 합니다. 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.
 
 회원들의 아이디는 같을 수 있지만 아이디는 같을 수 없다

 입출력 예
 id_pw    db    result
 ["meosseugi", "1234"]    [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]    "login"
 ["programmer01", "15789"]    [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]    "wrong pw"
 ["rabbit04", "98761"]    [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]    "fail"
 https://school.programmers.co.kr/learn/courses/30/lessons/120883
 */

func solution_login_true_or_false(_ id_pw:[String], _ db:[[String]]) -> String {
    let id = id_pw[0]
    let pw = id_pw[1]
    var arrID = [[String]]()
    
    for item in db.enumerated() {
        if id == item.element[0]{
            arrID.append(item.element)
            if pw == item.element[1] {
                return "login"
            }
        }
    }
    
    if arrID.count > 0 {
        return "wrong pw"
    } else {
        return "fail"
    }
}

print(solution_login_true_or_false(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution_login_true_or_false(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))
print("=================================================")


/*
 [ 문자열 밀기 ]
 
 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
 
 입출력 예
 A    B    result
 "hello"    "ohell"    1
 "apple"    "elppa"    -1
 "atat"    "tata"    1
 "abc"    "abc"    0

 https://school.programmers.co.kr/learn/courses/30/lessons/120921
 */

func solution_push_string(_ A:String, _ B:String) -> Int {
    if A == B {
        return 0
    }
    
    let str = B + B
    if str.contains(A) {
        let arr = str.components(separatedBy: A)
        return arr[0].count
    }
    return -1
}

print(solution_push_string("hello", "ohell"))
print(solution_push_string("hello", "elloh")) //testcase 7
print(solution_push_string("apple", "elppa"))
print(solution_push_string("atat", "tata"))
print(solution_push_string("abc", "abc"))
print(solution_push_string("asgwrfer2", "fer2asgwr"))
print("=================================================")

/*
 [ 치킨 쿠폰 ]
 
 프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.
 
 입출력 예
 chicken    result
 100    11
 1,081    120
 https://school.programmers.co.kr/learn/courses/30/lessons/120884
 */

func solution_service_chicken(_ chicken:Int) -> Int {
    var cupon = chicken
    var serviceChicken = 0
    while cupon / 10 > 0 {
        serviceChicken += cupon / 10
        cupon = (cupon / 10) + (cupon % 10)
    }
    
    return serviceChicken
}

print(solution_service_chicken(100))
print(solution_service_chicken(1081))
print("=================================================")

/*
 [ 유한소수 판별하기 ]
 
 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
 
 입출력 예
 a    b    result
 7    20    1
 11    22    1
 12    21    2
 https://school.programmers.co.kr/learn/courses/30/lessons/120878
 */

func solution_finite_decimal(_ a:Int, _ b:Int) -> Int {
    var gcdNum = 0
    gcdNum = gcd(a, b)
    let denominator = b / gcdNum
    
    if a % b == 0 { // 정수
        return 1
    }
    
    var primes = [Int]()
    var num = denominator
    for i in 2...denominator {
         while num % i == 0 {
             primes.append(i)
             if i != 2 && i != 5 {
                 return 2
             }
            num /= i
        }
    }
    return 1
}

func gcd(_ a: Int, _ b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return gcd(b, a%b)
    }
}

print(solution_finite_decimal(7, 20))
print(solution_finite_decimal(11, 22))
print(solution_finite_decimal(12, 21))
print(solution_finite_decimal(3500, 500))
print("=================================================")

// 20, 5의 최대공약수는 = 5


//finite decimal
//
//numerator denominator
