#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
void print_oef(int arr[], int n) {
	for (int i = 0;i < n;i++) {
		printf("%d ", arr[i]);
	}
	putchar('\n');
}

void cou_sort(int arr[], int n) {
	if (n <= 1) {
		return;
	}
	int m = arr[0];
	for (int i = 1;i < n;i++) {
		if (arr[i] > m) {
			m = arr[i];
		}
	}
	int* count = (int*)malloc((m + 1) * sizeof(int));
	memset(count, 0, (m + 1) * sizeof(int));
	for (int i = 0;i < n;i++) {
		count[arr[i]]++;
	}
	for (int i = 1;i <= m;i++) {
		count[i] += count[i - 1];
	}
	int* output = (int*)malloc(n * sizeof(int));
	for (int i = 0;i < n;i++) {
		output[count[arr[i]] - 1] = arr[i];
		count[arr[i]]--;
	}
	for (int i = 0;i < n;i++) {
		arr[i] = output[i];
	}
	free(output);
	free(count);
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
	cou_sort(arr,size);
	end = clock();
	double time = ((double)(end-start))/CLOCKS_PER_SEC;
	printf("%lf",time);
}

int main() {
	test_time();
	return 0;
}
