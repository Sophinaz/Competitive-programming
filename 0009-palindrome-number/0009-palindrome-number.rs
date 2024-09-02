impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s = x.to_string();
        s == s.chars().rev().collect::<String>()
    }
}