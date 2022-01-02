func solution(_ phone_number:String) -> String {
    
    let number: Substring = phone_number[phone_number.index(phone_number.endIndex, offsetBy: -4)...]
    
    var phoneNumber = ""
    for _ in 0..<(phone_number.count - 4){
        phoneNumber += "*"
    }
    
    phoneNumber += number
    return phoneNumber
    
}
