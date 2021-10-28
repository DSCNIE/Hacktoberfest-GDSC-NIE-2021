// problem link : https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1

code:-
--------
  
long long getMaxArea(long long arr[], int n)
    {
        // ------- brute force----------
        
        long long area=0;
        for(int i=0;i<n;i++){
            int height=arr[i];
            int l=i,r=i;
            while(l>=0 and arr[l]>=height) l--;
            while(r<n and arr[r]>=height) r++;
            long long ans= (r-l-1)*height;
            area=max(area,ans);
        }
        return area;
        
        //  optimal solution
  
  
        vector<int> left(n),right(n);
        stack<int> st;
        for(int i=0;i<n;i++){
            if(st.empty()){
                left[i]=0;
                st.push(i);
            }
            else{
                while(!st.empty() &&  arr[st.top()]>=arr[i]){
                    st.pop();
                }
                
                left[i]=st.empty()?0 : st.top()+1;
                st.push(i);
            }
            
            
        }
        
        
        while(!st.empty()) st.pop();
        
        for(int i=n-1;i>=0;i--){
            if(st.empty()){
                right[i]=n-1;
                st.push(i);
            }
            else{
                while(!st.empty() && arr[st.top()]>=arr[i]) {st.pop();}
                right[i]=st.empty()? n-1 : st.top()-1;
                st.push(i);
            }
        }
        
        long long area=0;
        for(int i=0;i<n;i++){
            area = max(area, arr[i]*(right[i]-left[i]+1)  );
        }
        return area;
        
        
    }
