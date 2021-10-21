/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        Deque<Integer> dq = new ArrayDeque<>();
        int max = Math.max(m,n);
        for(int i = 0; i < max; i++) {
            if (i < m) {
                dq.offerFirst(nums1[i]);
            } if(i < n) {
                dq.offerLast(nums2[i]);
            }
        }
        for (int j = m + n - 1; j >= 0; j--) {
            if(dq.peekFirst() >= dq.peekLast()) 
                nums1[j] = dq.pollFirst();
            else 
                nums1[j] = dq.pollLast();
        }
    }
}
// @lc code=end

