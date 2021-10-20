package gfg;
import java.util.HashSet;
import java.util.Set;
class Solution{
    public static int doUnion(int a[], int n, int b[], int m) 
    {
        Set<Integer> set = new HashSet<Integer>();
        int max = Math.max(m,n);
        for(int i = 0; i < max; i++) {
            if (i < n) {
                set.add(a[i]);
            } if(i < m) {
                set.add(b[i]);
            }
        }
        return set.size();
    }
}