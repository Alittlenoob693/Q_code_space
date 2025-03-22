#include<stdio.h>
#include<stdlib.h>

typedef struct node {
	struct node* prior;
	int data;
	struct node* next;
}Dlist;
//创建n个节点，可以接收n个数据
Dlist* construction(int n) {
	if (n <= 0) {
		return NULL;
	}
	Dlist* list = (Dlist*)malloc(sizeof(Dlist));
	Dlist* p = list;
	list->prior = NULL;
	list->data = 0;
	for (int i = 1;i < n;i++) {
		Dlist* tmp = (Dlist*)malloc(sizeof(Dlist));
		tmp->data = 0;
		tmp->prior = p;
		tmp->next = NULL;
		p->next = tmp;
		p = p->next;
	}
	return list;
}
//在第n个节点处插入新节点
void charu(int n,Dlist* list) {
	if (list == NULL || n < 1) {
		return;
	}
	Dlist* p = list;
	for (int i = 1;i < n && p != NULL;i++) {
		p = p->next;
	}
	if (p == NULL) {
		return;
	}
	Dlist* New = (Dlist*)malloc(sizeof(Dlist));
	New->data = 0;
	if (p->prior != NULL) {
		Dlist* old_front = p->prior;
		Dlist* old_next = p;
		New->prior = old_front;
		New->next = old_next;
		old_front->next = New;
		old_front->prior = New;
	}
	else {
		New->next = list->next;
		list = New;
	}
}

