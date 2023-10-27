#include<bits/stdc++.h>
using namespace std;

int capacityShip(vector<int>& nums,int limit){
    int n = nums.size();
    int m = *max_element(nums.begin(),nums.end());
    int sum = accumulate(nums.begin(),nums.end(),0);
    int low=m,high=sum;
    while(low<=high){
        int mid=(low+high)/2,sum1=0,day=1;
        for(int i=0;i<n;i++){
            sum1+=nums[i];
            if(sum1>mid){
                day++;
                sum1=nums[i];
            }
        }
        if(day<=limit) high=mid-1;
        else low=mid+1;
    }
    return low;
}

int main(){
    int n;
    cin>>n;
    vector<int>nums;
    for(int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        nums.push_back(tmp);
    }
    int limit;
    cin>>limit;
    int ans = capacityShip(nums,limit);
    cout<<ans;
}