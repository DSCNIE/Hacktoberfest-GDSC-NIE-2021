#include<iostream>
using namespace std;

class node
{
public:
    int data;
    node *next;
    node *prev;
};

class double_linked_list
{
public:
    node *head;
    node *tail;
    int len = 0;

    // constructor
    double_linked_list()
    {
        head = NULL;
        tail = NULL;
    }

    // to get length of linked list
    int get_length()
    {
        return len;
    }

    // to get head element of linked list
    int get_head()
    {
        return head->data;
    }

    // to get tail element of linked list
    int get_tail()
    {
        return tail->data;
    }

    // to add node at the beginning
    void add_first(int value)
    {
        node *newest = new node;
        newest->data = value;
        newest->next = NULL;
        newest->prev = NULL;

        if(head == NULL)
        {
            head = newest;
            tail = newest;
        }
        else
        {
            newest->next = head;
            head->prev = newest;
            head = head->prev;
        }

        len++;
    }

    // to add a node at the end
    void add_last(int value)
    {
        node *newest = new node;
        newest->data = value;
        newest->next = NULL;
        newest->prev = NULL;

        if(tail == NULL)
        {
            head = newest;
            tail = newest;
        }
        else
        {
            tail->next = newest;
            newest->prev = tail;
            tail = tail->next;
        }
        len++;
    }

    // to add a node at any position
    // pos is the the position at which the new node should be
    void add_any(int value, int pos)
    {
        if(pos==1)
            add_first(value);
        else if(pos == len+1)
            add_last(value);
        else if(pos > len+1)
            cout << "position not applicable" << endl;
        else
        {
            node *newest = new node;
            newest->data = value;
            newest->next = NULL;
            newest->prev = NULL;

            node *temp = head;
            int i=1;
            while(i<pos-1)
            {
                temp = temp->next;
                i++;
            }
            newest->next = temp->next;
            temp->next->prev = newest;
            temp->next = newest;
            newest->prev = temp;
            len++;
        }
    }

    void delete_first()
    {
        if(len == 0)
        {
            cout << "Linked list is empty." << endl;
        }
        else if(len == 1)
        {
            node *deleted = new node;
            deleted = head;
            cout << "first element deleted: " << deleted->data << endl;
            head = NULL;
            tail = NULL;
            delete deleted;
            len--;
        }
        else
        {
            node *deleted = new node;
            deleted = head;
            head = head->next;
            head->prev = NULL;
            cout << "First element deleted: " << deleted->data << endl;
            delete deleted;
            len--;
        }
    }

    void delete_last()
    {
        if(head == NULL)
        {
            cout << "Linked list is empty." << endl;
        }

        else
        {
            node *deleted = new node;
            deleted = tail;
            len--;
            if(len == 0)
            {
                head = NULL;
                tail = NULL;
            }
            else
            {
                tail = tail->prev;
                tail->next = NULL;
                deleted->prev = NULL;
            }

            cout << "Last element deleted: " << deleted->data << endl;
            delete deleted;

        }
    }

    // to delete a node from a particular position.
    void delete_any(int pos)
    {
        if(pos == 1)
            delete_first();
        else if(pos == len)
            delete_last();
        else if(pos > len)
            cout << "Position " << pos << " not applicable" << endl;
        else
        {
            node *temp = head;
            int i = 1;
            while(i<pos-1)
            {
                temp = temp->next;
                i++;
            }
            int removed = temp->next->data;

            temp->next = temp->next->next;
            temp->next->next->prev = temp;
            len--;
            cout << "Element deleted " << removed << endl;
        }
    }

    // to display entire linked list
    void display()
    {
        if(len == 0)
        {
            cout << "list is empty." << endl;
        }
        node *temp;
        temp = head;
        cout << "Linked list: ";
        while(temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main()
{
    double_linked_list d1;

    d1.add_first(5);
    d1.add_first(4);
    d1.add_first(3);
    d1.add_first(2);
    d1.add_first(1);
    d1.add_last(6);
    d1.add_last(7);

    d1.display();
    cout << "length of the list: " << d1.get_length() << endl << endl;


    d1.delete_first();
    d1.delete_last();
    cout << endl;

    d1.display();
    cout << "length of the list: " << d1.get_length() << endl << endl;
    cout << "Head element: " << d1.get_head() << endl;
    cout << "Tail element: " << d1.get_tail() << endl << endl;;

    d1.add_any(7,6);
    d1.add_any(1,1);
    d1.add_any(40,4);
    d1.display();
    cout << "Head element: " << d1.get_head() << endl;
    cout << "Tail element: " << d1.get_tail() << endl << endl;

    d1.delete_any(4);
    d1.delete_any(7);
    d1.delete_any(1);
    d1.delete_any(7);
    d1.display();
    cout << "length of the list: " << d1.get_length() << endl;
    cout << "Head element: " << d1.get_head() << endl;
    cout << "Tail element: " << d1.get_tail() << endl << endl;
}
