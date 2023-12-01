#include<iostream>
#include<string.h>
using namespace std;

struct node{
    int prn;
    string name;
    struct node *next;
    node(string name,int prn){
        this->name=name;
        this->prn=prn;
        this->next=NULL;
    }
};

class list{
    node *head;
    public:
    list(){head = NULL;}
    
    void create(string name,int prn){
        node *newnode = new node(name,prn);
        if(head == NULL){head = newnode;return;}
        node *temp = head;
        while(temp->next != NULL){temp = temp->next;}
        temp->next = newnode;
    }

    string n;int p;

    void insert_president(){
        
        cout<<"Enter Name of President:";cin>>n;

        cout<<"Enter PRN of President:";cin>>p;
        create(n,p);
    }

    void insert_member(){
        int c;
        while (c)
        {
            cout<<"Enter name of Member:";cin>>n;
            cout<<"Enter PRN of Member:";cin>>p;
            create(n,p);
            cout<<"Do you wish to continue the list(0|1):";cin>>c;
        }
    }

    void display(){
        node *temp = head;
        cout<<"------------------------STUDENT COUNCIL------------------------"<<endl;
        cout<<"STUDENT NAME\t"<<"PRN Number"<<endl;
        if (temp == NULL){cout<<"list is empty";}
        while(temp != NULL){
            cout<<"\t"<<temp->name<<"\t"<<temp->prn<<endl;
            temp = temp->next;
        }
    }
    void count(){
        int counter = 0;
        node *temp = head;
        while(temp != NULL){
            counter++;
            temp = temp->next;
        }
        cout<<"Total number of members in council is "<<counter-1<<endl;
    }
};

int main(){
    list obj;
    obj.insert_president();
    obj.insert_member();
    obj.display();
    obj.count();
}
