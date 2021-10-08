#include<iostream>
using namespace std;
struct Node
{
    int data;
    Node *next;
};
class SingleLinkedList
{
       private:
       Node *head;
       public:
       SingleLinkedList()
       {
           head=NULL;
       }
       Node *getnewnode(int data);
       void display();
       void insertB(int data);
       void insertL(int data);
       void insert(int data,int position);
       void deletel();
       void deleteB();
       void deletepos(int position);
       Node *nthnodelast1(int n);
       Node *nthnodelast2(int n);
       void form_cycle();
       int cycle_length();
       int detect_cycle();
       Node *startingNode();
};
Node* SingleLinkedList::getnewnode(int data)
{
    Node *newnode=new Node;
    newnode->data=data;
    newnode->next=NULL;
    return newnode;
}
void SingleLinkedList::display()
{
    Node *temp=head;
    if(head == NULL)
    {
        cout<<"error liist is empty"<<endl;
    }
    while(temp != NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}
void SingleLinkedList::insertB(int data)
{
    Node *newnode=getnewnode(data);
    newnode->next=head;
    head=newnode;
}
void SingleLinkedList::insertL(int data)
{
    Node *newnode=getnewnode(data);
    if(head == NULL)
    {
        cout<<"The list was empty therefore inseerting in front"<<endl;
        insertB(data);
    }
    Node *temp=head;
    while(temp->next != NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;
    newnode->next=NULL;
}
void SingleLinkedList::insert(int data,int position)
{
    if(position == 0)
    {
        insertB(data);
    }
    else
    {
        Node *newnode=getnewnode(data);
        Node *temp=head;
        for(int i=0;i<position-1;i++)
        {
            temp=temp->next;
        }
        Node *agla=temp->next;
        temp->next=newnode;
        newnode->next=agla;
    }
    
}
void SingleLinkedList::deleteB()
{
    Node*temp=head;
    head=head->next;
    delete(temp);
}
void SingleLinkedList::deletel()
{
    if(head == NULL)
    {
        cout<<"underflow"<<endl;
    }
    Node *temp=head;
    while(temp->next->next != NULL)
    {
        temp=temp->next;
        }
        Node *del=temp->next;
        temp->next=NULL;
        delete(del);
}
void SingleLinkedList::deletepos(int position)
{
    Node *temp=head;
    for(int i=0;i<position-1;i++)
    {
        temp=temp->next;
    }
    Node *agla=temp->next->next;
    Node *del=temp->next;
    temp->next=agla;
    delete(del);
}
void SingleLinkedList::form_cycle()
{
    Node *start=head->next;
    Node *temp=head;
    while (temp->next != NULL)
    {
        temp=temp->next;
    }
    cout<<start->data<<endl;
    cout<<temp->data<<endl;
    temp->next=start;
}
int SingleLinkedList::detect_cycle()
{
     Node *slow=head,*fast=head;
     while (slow != NULL && fast != NULL && fast->next != NULL)
     {
         slow=slow->next;
         fast=fast->next->next;
         if(slow == fast)
         {
             return 1;
             break;
         }

     }
     
return 0;
    
}
int SingleLinkedList::cycle_length()
{
  Node *slow=head;
  Node *fast=head;
  while(slow!= NULL && fast!= NULL && fast->next!= NULL)
  {
      slow=slow->next;
      fast=fast->next->next;
      if(slow==fast)
      { int counter=0;
      fast=fast->next;
          while (fast!= slow)
          {
              fast=fast->next;
            ++counter;
          }
          return ++counter;
      }
  }

}
Node* SingleLinkedList::startingNode()
{
    Node *slow=head,*fast=head;
    while (slow!= NULL && fast!= NULL && fast->next != NULL)
    {
        slow=slow->next;
        fast=fast->next->next;
        if(fast == slow)
        {
            slow=head;
            while (slow !=fast)
            {
                slow=slow->next;
            }
            return slow;
        }
    }
    
}
int main()
{
    SingleLinkedList l1;
    l1.display();
    l1.insertB(1);
    l1.insertB(2);
    l1.insertB(3);
    l1.insertB(4);
    l1.insertB(5);
    l1.insertB(6);
    l1.insertL(3);
    l1.display();
    l1.insertL(23);
    l1.display();
    l1.form_cycle();
    cout<<l1.detect_cycle()<<endl;
    cout<<"The length of cycle is = "<<l1.cycle_length()<<endl;
    cout<<"The starting node is= "<<l1.startingNode()->data<<endl;
    return 0;
}