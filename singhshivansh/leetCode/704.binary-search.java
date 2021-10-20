/*
 * @lc app=leetcode id=704 lang=java
 *
 * [704] Binary Search
 */

// @lc code=start
class Solution {
    public int search(int[] numbers, int target) {
        int low = 0, high = numbers.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if(numbers[mid] == target)
                return mid;
            else if(numbers[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return -1;
    }
}
// @lc code=end

