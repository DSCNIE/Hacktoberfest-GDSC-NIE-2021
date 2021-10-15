/*
 * @lc app=leetcode id=42 lang=java
 *
 * [42] Trapping Rain Water
 */

// @lc code=start

// ! New to java not at all optimal code
// ! 5ms runtime -> 12.8% better
// https://leetcode.com/problems/trapping-rain-water/



// * Implementation using STACK


import java.util.Stack;
class Solution {
    public int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int max = height[0], sum = 0;
        stack.push(height[0]);
        for(Integer i:height) {
            if(stack.peek() - i < 0 && i > max) {
                sum += max * stack.size();
                while(stack.size() != 0)
                    sum -= stack.pop();
            }
            stack.push(i);
            max = max < i ? i : max;
        }
        while(stack.size() != 1) {
            int prev = stack.pop();
            if(prev > stack.peek()) {
                sum += prev - stack.pop();
                stack.push(prev);
            }
        }
        return sum;
    }
}
// @lc code=end

