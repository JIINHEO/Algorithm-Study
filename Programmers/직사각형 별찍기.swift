import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])

for _ in 0..<b {
    var star = ""
    for _ in 0..<a {
        star += "*"
    }
    print("\(star)")
}
