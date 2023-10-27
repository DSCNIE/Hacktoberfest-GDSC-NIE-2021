#include<bits/stdc++.h>
using namespace std;

void merge(int arr[],int l,int m,int h){
    vector<int>ds;
    int left = l;
    int right = m+1;
    while(left<=m && right<=h){
        if(arr[left]<=arr[right]){
            ds.push_back(arr[left]);
            left++;
        }
        else{
            ds.push_back(arr[right]);
            right++;
        }
    }
    while(left<=m){
        ds.push_back(arr[left]);
        left++;
    }
    while(right<=h){
        ds.push_back(arr[right]);
        right++;
    }
    for(int i=l;i<=h;i++){
        arr[i] = ds[i-l];
    }
    return;
}

void mergeSort(int arr[],int l,int h){
    if(l==h) return;
    else{
        int m = (l+h)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,h);
        merge(arr,l,m,h);
    }
}

int main(){
    int n;
    cout<<"Enter the number of elements:";
    cin>>n;
    int arr[n];
    cout<<"Enter the elements:"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    mergeSort(arr,0,n-1);
    for(auto it:arr){
        cout<<it<<" ";
    }
    return 0;
}
