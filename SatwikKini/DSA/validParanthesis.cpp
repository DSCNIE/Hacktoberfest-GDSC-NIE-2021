#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mod 1e9+7
#define vec vector<int>vec

bool validP(string s){
    stack<char>stk;
    int n = s.size();
    for(int i=0;i<n;i++){
        if(s[i] == '{' || s[i] == '(' || s[i] == '[') stk.push(s[i]);
        else{
            if(!stk.empty()){
                if(s[i] == '}' && stk.top() == '{') stk.pop();
                else if(s[i] == ']' && stk.top() == '[') stk.pop();
                else if(s[i] == ')' && stk.top() == '(') stk.pop();
                else stk.push(s[i]);
            }
            else stk.push(s[i]);
        }
    }
    if(stk.empty()) return true;
    else return false;
}

int main(){
    string s;
    cin>>s;
    cout<<validP(s);
    return 0;
}