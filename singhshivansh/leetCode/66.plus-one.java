/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 */

// @lc code=start

// Using Stack =================================================

// import java.util.Stack;
// import java.util.Arrays;

// class Solution {

//   public int[] plusOne(int[] digits) {
//     int last = digits.length - 1;
//     if (digits[last] != 9) {
//       digits[last] += 1;
//       return digits;
//     }
//     Stack<Integer> stack = new Stack<Integer>();
//     for (Integer digit : digits) stack.push(digit);
//     boolean flag = true;
//     int arr[] = new int[last + 2];
//     arr[last + 1] = 0;
//     stack.pop();
//     last--;
//     while (stack.size() > 0) {
//       int val = stack.pop();
//       if (flag) {
//         flag = val + 1 >= 10;
//         arr[last + 1] = flag ? 0 : val + 1;
//       } else arr[last + 1] = val;
//       last--;
//     }
//     if(flag) arr[0] = 1;
//     return arr[0] != 0 ? arr : Arrays.copyOfRange(arr, 1, arr.length);
//   }
// }

// ==================================================================================================

class Solution {
    public int[] plusOne(int[] digits) {
        int last = digits.length - 1;
        if (digits[last] != 9) {
            digits[last] += 1;
            return digits;
        }
        boolean flag = true;
        for(int i = last; i >= 0; i--) {
            if(flag) {
                digits[i] += 1;
                flag = digits[i] == 10;
                if(flag) digits[i] -= 10;
            }
        }
        if(flag) {
            int[] arr = new int[digits.length + 1];
            arr[0] = 1;
            return arr;
        }
        return digits;
    }
}

// @lc code=end
