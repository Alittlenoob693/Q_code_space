#include<iostream>
#include<stdlib.h>
using namespace std;
typedef struct node {
	int data;
	struct node* next;
}SN;

//创建单向链表的函数，需要所需创建节点的个数和头节点地址
SN* construction(int n) {
	SN* list = (SN*)malloc(sizeof(SN));
	SN * p = list;
	for (int i = 0;i < n;i++) {
		SN* tmp = (SN*)malloc(sizeof(SN));
		tmp->next = NULL;
		tmp->data = 0;
		p->next = tmp;
		p = p->next;
	}
	return list;
}

int main() {
	int arry[4] = { 1,2,3,4 };
	SN* list = construction(4);
	int i = 0;
	for (SN* p = list->next;p != NULL;p = p->next) {
		p->data = arry[i];
		i++;
	}
	for (SN* p = list->next;p != NULL;p = p->next) {
		cout << p->data << endl;
	}
	return 0;
}