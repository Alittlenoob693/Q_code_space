#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define Size 1000
//数组数据呈现 
void print_oef(int arr[],int n){
	for(int i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	putchar('\n');
}

//合并函数 
void meorge(int arr[],int temp[],int left,int right,int mid){
	int l_num = left;
	int r_num = mid+1;
	int pose = left;
	while(l_num<=mid&&r_num<=right){
		if(arr[l_num]<arr[r_num]){
			temp[pose] = arr[l_num];
			pose++;
			l_num++;
		}
		else{
			temp[pose] = arr[r_num];
			pose++;
			r_num++;
		}
	}
	while(l_num<=mid){
		temp[pose++] = arr[l_num++];
	}
	while(r_num<=right){
		temp[pose++] = arr[r_num++];
	}
	while(left<=right){
		arr[left] = temp[left];
		left++;
	}
}
//排序函数进入 
void me_sort(int arr[],int temp[],int left,int right){
	if(left<right){
		int mid = (left+right)/2;
		//分离左半区 
		me_sort(arr,temp,left,mid);
		//分离右半区 
		me_sort(arr,temp,mid+1,right);
		//合并 
		meorge(arr,temp,left,right,mid);
	}
}

//归并排序开始 
void merge_oef(int arr[],int n){
	int* temparr = (int*)malloc(n*sizeof(int));
	if(temparr==NULL){
		return;
	}
	me_sort(arr,temparr,0,n-1);
	free(temparr);
}
//测试函数，用来测试用时 
void test_time(){
	clock_t start,end;
	int size;
	scanf("%d",&size);//输入需要测试的数据的量 
	int* arr = (int*)malloc(size*sizeof(int));
	start = clock();
	for(int i=0;i<size;i++){
		arr[i] = rand();
	}
	merge_oef(arr,size);
	end = clock();
	double time = ((double)(end-start))/CLOCKS_PER_SEC;
	printf("%lf",time);
}

//主函数 
int main(){
	test_time();
	return 0;
}




