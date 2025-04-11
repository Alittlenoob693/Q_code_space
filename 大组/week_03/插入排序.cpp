#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
void print_oef(int arr[],int n){
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	cout<<"\n";
}

void is_sort(int arr[],int n){
	int i = 0;
	for(int j=i+1;j<n;j++){
		int k = j;
		while(k-1>=0){
			if(arr[k-1]>arr[k]){
				int tmp = arr[k-1];
				arr[k-1] = arr[k];
				arr[k] = tmp;
				k--;
			}
			else{
				break;
			}
		}
	}
}
void test_time(){
	clock_t start,end;
	int size;
	scanf("%d",&size);//输入需要测试的数据的量 
	int* arr = (int*)malloc(size*sizeof(int));
	start = clock();
	for(int i=0;i<size;i++){
		arr[i] = rand();
	}
	is_sort(arr,size);
	end = clock();
	double time = ((double)(end-start))/CLOCKS_PER_SEC;
	printf("%lf",time);
}

int main(){
	test_time();
	return 0;
}
