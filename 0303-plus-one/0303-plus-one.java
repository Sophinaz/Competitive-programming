public class Solution {
    public int[] plusOne(int[] digits) {
        if (digits.length == 0 || digits == null){
            return null;
        }
        int index = 1;
        for (int i =digits.length-1 ; i>=0; i--){
            int value = (digits[i]+index) % 10;
            index = (digits[i]+index) / 10;
            digits[i] = value;
        }
        
        if (index == 1){
            int[] array = new int[digits.length+1];
            array[0] = 1;
            int j=1;
            for(int i : digits){
                array[j]=i;
                j++;
            }
            return array;
        }
        return digits;
    }
}