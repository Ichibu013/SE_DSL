#include<iostream>
#include<string.h>
using namespace std;

struct node
{
    int prn;
    char name[20];
    struct node* next;
    node(int prn,char name[20]) {
        this->prn = prn;
        this->name[20] = name[20];
        this->next = NULL;
    }
};

class list {
    node* head;
public:
    list() { head = NULL; }

    void create(int prn,char name[20]) {
        node* newnode = new node(prn,name);
        if (head == NULL) { head = newnode; return; }
        node* temp = head;
        while (temp->next != NULL) { temp = temp->next; }
        temp->next = newnode;
    }
};

int main() {
    char n[20];
    int p;
    list obj;
    for (int i = 0; i < 4; i++) {
        cout << "Enter Student Name:"; cin >> n;
        cout << "Enter Student PRN:"; cin >> p;
        obj.create(p,n);
    }
}