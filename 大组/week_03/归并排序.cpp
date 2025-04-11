#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define Size 1000
//�������ݳ��� 
void print_oef(int arr[],int n){
	for(int i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	putchar('\n');
}

//�ϲ����� 
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
//���������� 
void me_sort(int arr[],int temp[],int left,int right){
	if(left<right){
		int mid = (left+right)/2;
		//��������� 
		me_sort(arr,temp,left,mid);
		//�����Ұ��� 
		me_sort(arr,temp,mid+1,right);
		//�ϲ� 
		meorge(arr,temp,left,right,mid);
	}
}

//�鲢����ʼ 
void merge_oef(int arr[],int n){
	int* temparr = (int*)malloc(n*sizeof(int));
	if(temparr==NULL){
		return;
	}
	me_sort(arr,temparr,0,n-1);
	free(temparr);
}
//���Ժ���������������ʱ 
void test_time(){
	clock_t start,end;
	int size;
	scanf("%d",&size);//������Ҫ���Ե����ݵ��� 
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

//������ 
int main(){
	test_time();
	return 0;
}




