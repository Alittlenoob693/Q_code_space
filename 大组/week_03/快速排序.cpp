#include<stdio.h>
#include<stdlib.h>
#include<time.h> 
//快速排序
int st_and(int arr[],int left,int right){
	int priority = arr[left];
	while(left < right){
		while(left < right && arr[right] >= priority){
			right--;
		}
		arr[left] = arr[right];
		while(left < right && arr[left] <= priority){
			left++;
		}
		arr[right] = arr[left];
	}
	arr[left] = priority;
	return left;
}
//快排进入 
void me_stand_eog(int arr[],int left,int right){
	if(left < right){
		int pni = st_and(arr,left,right);
		me_stand_eog(arr,left,pni-1);
		me_stand_eog(arr,pni+1,right);
	}
}

void print_oef(int arr[],int n){
	for(int i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	putchar('\n');
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
	me_stand_eog(arr,0,size-1);
	end = clock();
	double time = ((double)(end-start))/CLOCKS_PER_SEC;
	printf("%lf\n",time);
}
int main(){
	test_time();
	return 0;
}
