#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mod 1e9+7
#define vec vector<int>vec

int celeb(vector <vector<int> > &mat, int n){
    stack<int>s;
    for(int i=0;i<n;i++){
        s.push(i);
    }
    while(s.size()>1){
        int a = s.top();
        s.pop();
        int b = s.top();
        s.pop();
        if(mat[a][b] == 1) s.push(b);
        else s.push(a);
    }
    int r=0,c=0;
    for(int i=0;i<n;i++){
        if(mat[i][s.top()] == 1) c++;
        if(mat[s.top()][i] == 0) r++;
    }
    if(r==n && c==n-1) return s.top();
    return -1;
}

int main(){
    int n;
    cin>>n;
    vector <vector<int> > mat;
    for(int i=0;i<n;i++){
        vector<int>tmp;
        for(int i=0;i<n;i++){
            int t;
            cin>>t;
            tmp.push_back(t);
        }
        mat.push_back(tmp);
    }
    int ans = celeb(mat,n);
    cout<<ans<<endl;
    return 0;
}