#include<iostream>
#include<string.h>
using namespace std;

struct node 
{
    int prn;
    char name[20];
    struct node *next;
};


class list{
    public:
    struct node *head=NULL,*temp,*newnode,*n;
    node* create(){
        char n[20];
        int p;
        node *newnode = new(struct node);
        cout<<"Enter Name:";cin>>n;
        strcpy(newnode->name,n);
        cout<<"Enter PRN:";cin>>p;
        newnode->prn=p;
        newnode->next=NULL;
        return newnode;
        }  
    void inset_president(){
        node* n = create();
        if(head==NULL){
            head=n;
        }
        else{
            temp=head;
            head=n;
            head->next = temp->next;
        }
    }
    void insert_member(){
        node* n = create();
        int c;
        if(head == NULL){
            head = n;
        }
        else{
            temp = head;
            do{
                temp = temp->next;
                temp -> next = n;
                 cout<<"IF U WISH TO STOP PRESS 1";cin>>c;;
            }while (c!=1);
            
        }
    }
    void display(){
        if(head == NULL){
            cout<<"List is Empty";
        }
        else{
            temp=head;
            while(head!=NULL){
                cout<<"NAME:"<<temp->name<<endl;
                cout<<"PRN:"<<temp->prn;
            }
        }
    }

};

int main(){
    list o;

    o.inset_president();
    o.insert_member();
    o.display();
}