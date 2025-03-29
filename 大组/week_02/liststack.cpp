#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

typedef struct stacklist {
    int data;
    struct stacklist* node;
} df;

typedef struct stacki {
    df* top;
    int count;
} linkstack;

bool empty_stack(linkstack* pstack) {
    pstack->top = NULL;
    pstack->count = 0;
    return true;
}

void pull_stack(linkstack* pstack, int d) {
    df* tmp = (df*)malloc(sizeof(df));
    if (tmp == NULL) {
        return;
    }
    tmp->data = d;
    tmp->node = pstack->top;
    pstack->top = tmp;
    pstack->count++;
}

void pop_stack(linkstack* pstack, int* pd) {
    if (pstack == NULL) {
        return;
    }
    df* p = pstack->top;
    *pd = p->data;
    pstack->top = p->node;
    free(p);
    pstack->count--;
}

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

int apply_op(int a, int b, char op) {
    switch (op) {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
    case '/': return b != 0 ? a / b : 0;
    }
    return 0;
}

int main() {
    char expr[100];
    printf("输入一个四则运算表达式（数字不超过10）: ");
    scanf("%s", expr);

    linkstack numStack, opStack;
    empty_stack(&numStack);
    empty_stack(&opStack);

    int i = 0;
    while (expr[i] != '\0') {
        if (isspace(expr[i])) {
            i++;
            continue;
        }
        if (isdigit(expr[i])) {
            int num = expr[i] - '0';
            if (num > 9) {
                printf("输入的数字不能超过10\n");
                return 1;
            }
            pull_stack(&numStack, num);
            i++;
        }
        else {
            while (opStack.count > 0 && precedence(opStack.top->data) >= precedence(expr[i])) {
                int b, a;
                pop_stack(&numStack, &b);
                pop_stack(&numStack, &a);
                char op;
                pop_stack(&opStack, (int*)&op);
                pull_stack(&numStack, apply_op(a, b, op));
            }
            pull_stack(&opStack, expr[i]);
            i++;
        }
    }

    while (opStack.count > 0) {
        int b, a;
        pop_stack(&numStack, &b);
        pop_stack(&numStack, &a);
        char op;
        pop_stack(&opStack, (int*)&op);
        pull_stack(&numStack, apply_op(a, b, op));
    }

    int result;
    pop_stack(&numStack, &result);
    printf("计算结果: %d\n", result);
    return 0;
}