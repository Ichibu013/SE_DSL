#include<iostream>
#include<stack>
using namespace std;

bool balexp(string exp){
    stack<char> st;
    char x;
    int i;
    for(i = 0;i<exp.length();i++){
        if(exp[i]=='('||exp[i]=='['||exp[i]=='{'){
            st.push(exp[i]);
            continue;
        }
        if(st.empty())return false;
    }
    switch (exp[i])
    {
    case ')':
        x = st.top();
        st.pop();
        if(x == '{'||x == '[')
        return false;
        break;
    case ']':
        x = st.top();
        st.pop();
        if (x == '('||x =='{')
        return false;
        break;
    case '}':
        x = st.top();
        st.pop();
        if(x == '('||x == '[')
        return false;
        break;
    default:
        break;
    }
}

int main(){
    string exp = "{[()]}";
    if(balexp(exp)==false)
    cout<<"Experssion is balenced"<<endl;
    else
    cout<<"Expression is not balanced"<<endl;
}