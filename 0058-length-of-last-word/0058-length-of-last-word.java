class Solution {
    public int lengthOfLastWord(String s) {
        int length = 0;
        boolean t = false;
        for (int i = s.length()-1; i >= 0 ; i--){
            if (s.charAt(i) != ' '){
                length+=1;
                t = true;
            }
            else if (s.charAt(i) == ' '){
                if (t){
                     break;
                }
               
            }
            else{
                ;
            }
        }
        return length;
        
    }
}