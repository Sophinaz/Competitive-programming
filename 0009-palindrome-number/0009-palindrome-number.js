/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let temp = String(x)
    for (let i = 0 ; i < (temp.length / 2) ; i++){
        console.log(i, temp[0])
        if (temp[i] !== temp[temp.length - i - 1]) {
            return false
        }
    }
    return true
};