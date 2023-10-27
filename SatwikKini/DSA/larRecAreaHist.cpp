#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mod 1e9+7
#define vec vector<int>vec

int area(vector<int>& arr){
    int n = arr.size();
    stack<int>fwd,rev;
    fwd.push(-1);
    rev.push(-1);
    vector<int>up(n,0),dwn(n,0);
    for(int i=0;i<n;i++){
        int r = n-i-1;
        while(fwd.top()!=-1 && arr[fwd.top()]>=arr[r]){
            fwd.pop();
        }
        while(rev.top()!=-1 && arr[rev.top()]>=arr[i]){
            rev.pop();
        }
        up[r] = fwd.top();
        dwn[i] = rev.top();
        fwd.push(r);
        rev.push(i);
    }
    int area = -1;
    for(int i=0;i<n;i++){
        if(up[i]==-1) up[i]=n;
        int newArea = 0;
        newArea = arr[i] * (up[i] - dwn[i] - 1);
        area = max(area,newArea);
    }
    return area;
}

int main(){
    int n;
    cin>>n;
    vector<int>arr;
    for(int i=0;i<n;i++){
        int t;
        cin>>t;
        arr.push_back(t);
    }
    int ans = area(arr);
    cout<<ans<<" ";
    cout<<endl;
    return 0;
}