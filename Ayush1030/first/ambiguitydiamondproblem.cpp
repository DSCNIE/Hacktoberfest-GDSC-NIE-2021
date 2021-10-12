#include<iostream>
using namespace std;
class basea{
public:
int a;
};
class base1:  virtual public basea{
    public:
base1(){
a=5;
}
};
class base2:   virtual public basea{
    public:
base2(){
    a=6;
}
};
class derived: public base1, public base2{ //piche wale base class ke value print hoti hai jaise isme 6 hui print
    public:
    void print(){
        cout<<a;
    }
    //bina virtual lgae msg aata hai a is ambiguos kyunki derived class ko pta nhi 
        //kaunsa a print karna hai
    
};
int main(){
    derived obj;
    obj.print();
    return 0;
}