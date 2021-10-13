package sidharthagrwl.binary_search;

public class BinarySearch {
    public static void main(String[] args) {

       /* binary search -> sorted array
       * find the middle element
       * check if the target element is greater than middle element, if yes then search in right else
       * search in the left
       *if middle element is equal to the target element then we found the answer
       * take 2 pointers (start,end)
       * if start > end -> element not found
       * k = logN , k is the total no. of comparisons in the worst case and N is the size of the array
       * hence time complexity -> O(logN)
       *
       * order-agnostic binary search says that you are given a sorted array, but you don't know if its ascending or descending
       * */

        int[] arr = {-18,-12,-4,0,2,3,4,15,16,18,22,45,89};
        int ans = binarySearch(arr,15);

        System.out.println(ans);
    }
    static int binarySearch(int[] a,int target) {
        int start = 0;
        int end = a.length-1;

        while(start<=end) {
            //find the middle
//            int mid = (start+end)/2; // might be possible that (start+end) exceeds the range of int in java.
            int mid = start + (end-start)/2; // better way to find mid
            
            if(target < a[mid]) {
                end = mid - 1;
            } else if(target > a[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
