//
//  11659번 구간합구하기4.swift
//  Algorithm
//
//  Created by jiinheo on 2023/04/05.
//

import Foundation

/**
 백준 
 https://www.acmicpc.net/problem/3020
 */

func findSumInterval() {
    var answer = [Int]()
    let count = readLine()!.components(separatedBy: " ")
    let n = Int(count[0])
    let m = Int(count[1])

    let arr = readLine()!.split(separator: " ").map{ Int(String($0))! }
    var sumArray = [Int](repeating: 0, count: arr.count) // 구간합

    sumArray[0] = arr[0]

    for i in 1..<n! {
        sumArray[i] = sumArray[i-1] + arr[i]
    }

    for _ in 0..<m! {
        let arr = readLine()!.split(separator: " ").map{Int(String($0))!}
        
        if arr[0] == 1 {
            answer.append(sumArray[arr[1] - 1])
        } else {
            let start = arr[0] - 2
            let end = arr[1] - 1
            answer.append(sumArray[end] - sumArray[start])
        }
    }

    for item in answer {
        print(item)
    }


}
