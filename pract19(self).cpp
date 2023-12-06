#include<iostream>
#include<string.h>
#include<iomanip>

using namespace std;

struct node {
    int prn;
    string name;
    struct node* next;
    node(string name, int prn) {
        this->name = name;
        this->prn = prn;
        this->next = NULL;
    }
};

class list {
    node* head;
public:
    list() { head = NULL; }

    void create(string name, int prn) {
        node* newnode = new node(name, prn);
        if (head == NULL) { head = newnode; return; }
        node* temp = head;
        while (temp->next != NULL) { temp = temp->next; }
        temp->next = newnode;
    }

    string n; int p;

    void insert_president() {

        cout << "Enter Name of President:"; cin >> n;

        cout << "Enter PRN of President:"; cin >> p;
        create(n, p);
    }

    void insert_member() {
        int c = 1;
        while (c)
        {
            cout << "Enter name of Member:"; cin >> n;
            cout << "Enter PRN of Member:"; cin >> p;
            create(n, p);
            cout << "Do you wish to continue the list(0|1):"; cin >> c;
        }
    }

    void display() {
        node* temp = head;
        if (temp == NULL) { cout << "List is empty" << endl; }
        else {
            int sr=0;
            cout << "------------------------STUDENT COUNCIL------------------------" << endl;
            cout << left << setw(8)<<"SR NO." << setw(20) << "STUDENT NAME" << left << setw(20) << "PRN NUMBER"<<endl;
            while (temp != NULL) {
                sr++;
                cout << left << setw(8) << sr << setw(20) << temp->name << left << setw(20) << temp->prn << endl;
                temp = temp->next;
            }
        }
    }
    int count() {
        int counter = 0;
        node* temp = head;
        while (temp != NULL) {
            counter++;
            temp = temp->next;
        }
        return counter;
    }

    void delete_president() {
        node* temp = head;
        head = temp->next;
    }
    void delete_sec() {
        node* temp = head, * prest = NULL;
        while (temp->next != NULL) {
            prest = temp;
            temp = temp->next;
        }
        prest->next = NULL;
        delete temp;
        
    }

    void delete_member() {
        node* pre = NULL;
        int counter = 0; int pos;
        cout << "Enter the position to be deleted:"; cin >> pos;
        node* temp = head;
        if (count() < pos) { cout << "Enter position is out of range\n"; }
        else {
            while (counter != pos) {
                counter++;
                pre = temp;
                temp = temp->next;
            }
            pre->next = temp->next;
            delete temp;
        }
    }
    void concat() {
    node *head1 = NULL,*head2=NULL;
    cout<<"FIRST GROUP:"<<endl;
    insert_president();
    insert_member();
    

    }
};

int main() {
    int choice = 0;
    list obj;
    cout << "Perform the following operations:\n\t1]Add President\n\t2]Add Members\n\t3]Display All Members";
    cout << "\n\t4]Count all members\n\t5]Delete President\n\t6]Delete Secretary\n\t7]Delete a member";
    cout << "\n\t8]Concat 2 lists\n\t9]End" << endl;
    repeat:
    cout << "Select choice:"; cin >> choice; 
    switch (choice) {
        case 1:cout << "\n";
            obj.insert_president();
            cout << "\n";
            goto repeat;
            break;
        case 2:cout << "\n";
            obj.insert_member();
            cout << "\n";
            goto repeat;
            break;
        case 3:cout << "\n";
            obj.display();
            cout << "\n";
            goto repeat;
            break;
        case 4:cout << "\n"; 
            cout << "Student council has a President and " << obj.count() - 1 << " members." << endl;
            cout << "\n";
            goto repeat;
            break;
        case 5:cout << "\n"; 
            obj.delete_president();
            obj.display();
            cout << "\n";
            goto repeat;
            break;
        case 6:cout << "\n"; 
            obj.delete_sec();
            obj.display();
            cout << "\n";
            goto repeat;
            break;
        case 7:cout << "\n"; 
            obj.delete_member();
            obj.display();
            cout << "\n";
            goto repeat;
            break;
        case 8:cout << "\n"; 
            obj.concat();
            cout << "\n";
            goto repeat;
            break;
        case 9:choice = 10;;
            break;
        default:
            cout << "\n";
            cout << "Please enter a correct input";
            break;
    }

}
