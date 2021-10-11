#include<iostream>
using namespace std;
struct Node
{
    int data;
    Node *right;
    Node *down;
};
struct NodeFlatten 
{
    int data;
    NodeFlatten *next;
};
class List
{
    private:
    Node *head;
    NodeFlatten *khopdi;
    public:
    List()
    {
        head=NULL;
        khopdi=NULL;
    }
    Node *getnewnode(int data);
    NodeFlatten *getnewnodeF(int data);
    void insert(int data);
    void initialrow(int data);
    void insertDown(int data,int rightPos);
    void print();
    void flatten(Node *head);
    void display(NodeFlatten *head);
    NodeFlatten *gethead();
    
    Node *getHead();
};
Node* List::getnewnode(int data)
{
    Node *newnode=new Node;
    newnode->data=data;
    newnode->right=NULL;
    newnode->down=NULL;
    return newnode;
}
NodeFlatten* List::getnewnodeF(int data)
{
    NodeFlatten *newnode=new NodeFlatten;
    newnode->data=data;
    newnode->next=NULL;
    return newnode;
}
void List::insert(int data)
{
   NodeFlatten *newnode=getnewnodeF(data);
   newnode->next=khopdi;
   khopdi=newnode;
}
void List::initialrow(int data)
{
    Node *newnode=getnewnode(data);
    newnode->right=head;
    newnode->down=NULL;
    head=newnode;
}
void List::print()
{
    Node *temp=head;
    while (temp!=NULL)
    {
        Node *temp1=temp;
        while (temp1!= NULL)
        {
            cout<<temp1->data<<"->";
            temp1=temp1->down;
        }
        cout<<"NULL";
        cout<<endl;
     
        temp=temp->right;
        
    }
    
}
void List::insertDown(int data,int rightPos)
{
    Node *newnode=getnewnode(data);
    Node *temp=head;
    for(int i=0;i<rightPos;i++)
    {
        temp=temp->right;
    }
      if(temp->down == NULL)
      {
          temp->down=newnode;
          newnode->down=NULL;
      }
      else
      {
          while (temp->down!=NULL)
          {
              temp=temp->down;
          }
          temp->down=newnode;
          newnode->down=NULL;
          
      }
      
      
     
}
Node* List::getHead()
{
    return head;
}
void List::flatten(Node *head)
{
    Node *temp=head;
    while (temp != NULL)
    {
        Node *temp1=temp;
        while (temp1 != NULL)
        {
            insert(temp1->data);
            temp1=temp1->down;
        }
        temp=temp->right;
        
    }

    
}
void List::display(NodeFlatten *head)
{
    NodeFlatten *temp=head;
    while (temp != NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
    
}
NodeFlatten* List::gethead()
{
    return khopdi;
}
int main()
{
    List l1;
    l1.initialrow(1);
    l1.initialrow(2);
    l1.initialrow(3);
    l1.initialrow(4);
    l1.initialrow(5);
    l1.initialrow(6);
    l1.initialrow(7);
    l1.initialrow(8);
    l1.initialrow(9);
    l1.print();
    cout<<endl<<endl;
    l1.insertDown(91,0);
    l1.insertDown(92,0);
    l1.insertDown(93,0);
    l1.insertDown(94,0);
    l1.insertDown(95,0);
    l1.insertDown(96,0);
    l1.insertDown(97,0);
    l1.insertDown(98,0);
    l1.insertDown(99,0);
    l1.print();
    cout<<endl<<endl<<endl;
    l1.insertDown(81,1);
    l1.insertDown(82,1);
    l1.insertDown(83,1);
    l1.insertDown(84,1);
    l1.insertDown(85,1);
    l1.insertDown(86,1);
    l1.insertDown(87,1);
    l1.insertDown(88,1);
    l1.insertDown(89,1);

    l1.insertDown(71,2);
    l1.insertDown(72,2);
    l1.insertDown(73,2);
    l1.insertDown(74,2);
    l1.insertDown(75,2);
    l1.insertDown(76,2);
    l1.insertDown(77,2);
    l1.insertDown(78,2);
    l1.insertDown(79,2);

    l1.insertDown(61,3);
    l1.insertDown(62,3);
    l1.insertDown(63,3);
    l1.insertDown(64,3);
    l1.insertDown(65,3);
    l1.insertDown(66,3);
    l1.insertDown(67,3);
    l1.insertDown(68,3);
    l1.insertDown(69,3);

    l1.insertDown(51,4);
    l1.insertDown(52,4);
    l1.insertDown(53,4);
    l1.insertDown(54,4);
    l1.insertDown(55,4);
    l1.insertDown(56,4);
    l1.insertDown(57,4);
    l1.insertDown(58,4);
    l1.insertDown(59,4);

    l1.insertDown(41,5);
    l1.insertDown(42,5);
    l1.insertDown(43,5);
    l1.insertDown(44,5);
    l1.insertDown(45,5);
    l1.insertDown(46,5);
    l1.insertDown(47,5);
    l1.insertDown(48,5);
    l1.insertDown(49,5);

    l1.insertDown(31,6);
    l1.insertDown(32,6);
    l1.insertDown(33,6);
    l1.insertDown(34,6);
    l1.insertDown(35,6);
    l1.insertDown(36,6);
    l1.insertDown(37,6);
    l1.insertDown(38,6);
    l1.insertDown(39,6);

    l1.insertDown(21,7);
    l1.insertDown(22,7);
    l1.insertDown(23,7);
    l1.insertDown(24,7);
    l1.insertDown(25,7);
    l1.insertDown(26,7);
    l1.insertDown(27,7);
    l1.insertDown(28,7);
    l1.insertDown(29,7);

    l1.insertDown(11,8);
    l1.insertDown(12,8);
    l1.insertDown(13,8);
    l1.insertDown(14,8);
    l1.insertDown(15,8);
    l1.insertDown(16,8);
    l1.insertDown(17,8);
    l1.insertDown(18,8);
    l1.insertDown(19,8);


    l1.print();
    cout<<endl<<endl<<endl;
    Node *head=l1.getHead();
    l1.flatten(head);
    l1.display(l1.gethead());

    

    return 0;

}
// reverse order mei hui hai coz I implemented insertB but you can use insertL to flatten in same order