package sidharthagrwl.StringSearch;

public class StringSearch {
    public static void main(String[] args) {

        //search in string
        String name = "siddharth";
        char b = 't';

//        System.out.println(search(name,b));

        //search in range ques
        int[] a = {18,12,-7,3,14,28};
        int ans = searchInRange(a,1,4,14);
        System.out.println(ans);
    }
    static int searchInRange(int[] arr,int start,int end,int item) {

        for (int i = start; i <= end ; i++) {
            if(arr[i]==item) {
                return i;
            }
        }
        return -1;
    }

    static boolean search(String str,char a) {

        if(str.length()==0) {
            return false;
        }
//        for (int i = 0; i < str.length(); i++) {
//            if(a==str.charAt(i)) {
//                return true;
//            }
//        }
        for(char arr: str.toCharArray()) {
             if(a==arr) {
                 return true;
             }
        }
        return false;
    }
}