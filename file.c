#include<stdio.h>
int main(){
	int array[100], low, high, mid, key, n;

	printf("Enter the number of elements in the array:\n");
	scanf("%d", &n);

	printf("Enter the Elements of array:\n");
	for(int i=0; i<n; i++){
		scanf("%d", array[i]);
	}

	printf("Enter the element you want to find:");
	scanf("%d", &key);

	low = 0;
	high = n-1;

	while(low<=high){
		int mid = (low+high)/2;

		if(array[mid]==key){
			printf("Element found at index: %d", mid);
			break;
		}

		else if(array[mid]<key){
			high = mid-1;
		}
		else{
			low = mid+1;
		}
	}
return 0;
}
