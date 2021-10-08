//can use binary search tree as well as that will reduce the time complxity of find operation from:
/*
binary Search:O(logn)
linear search:O(n)
*/
#include<bits/stdc++.h>
#include<iostream>
using namespace std;

struct Edge {
    int head;
    vector<int>neighbors;
};

class Adjacency_list
{
  public:
  vector<Edge*>Edges;
  Edge *get_newEdge(int head,vector<int>neighbours);
  void insertEdge(Edge *newEdge);
  void addNeighbour(vector<int> Neighbours);
  void display();

};

Edge *Adjacency_list::get_newEdge(int head,vector<int>neighbours)
{
     Edge *newEdge=new Edge;
     newEdge->head=head;
     newEdge->neighbors=neighbours;
     return newEdge;
}
void Adjacency_list::insertEdge(Edge* newEdge)
{

}
void Adjacency_list::addNeighbour(vector<int>Neighbours)
{

}
void Adjacency_list::display()
{
  cout<<"Your graph contains "<<Edges.size()<<" number of vertices"<<endl;
  int edges=0;
  for(int i=0;i<Edges.size();i++)
  {
      int number=Edges[i]->neighbors.size();
      edges+=number;
  }
  cout<<"Your graph contains "<<edges<<" number of edges"<<endl;
  cout<<"Edge"<<"\t \t"<<"Neighbours"<<endl;
   for(int i=0;i<Edges.size();i++)
  {
      cout<<Edges[i]->head<<"\t \t \t";
      for(int j=0;j<Edges[i]->neighbors.size();j++)
      {
          cout<<Edges[i]->neighbors[j]<<" ";
      }
      cout<<endl;
  }
  
}
int main()
{
    Adjacency_list List;
    vector<int>neighbour1={3,4,8};
    vector<int>neighbour2={1,9,6};
    vector<int>neighbour3={6,8,7};
    vector<int>neighbour4={1,6,8};
    vector<int>neighbour5={1,2,3};
    vector<int>neighbour6={3,9,4};
    vector<int>neighbour7={2,4,9};
    vector<int>neighbour8={3,6,9};
    vector<int>neighbour9={1,4,5};
    vector<int>neighbour10={4,8,6};
    auto Edge1=List.get_newEdge(1,neighbour1);
    auto Edge2=List.get_newEdge(2,neighbour2);
    auto Edge3=List.get_newEdge(3,neighbour3);
    auto Edge4=List.get_newEdge(4,neighbour4);
    auto Edge5=List.get_newEdge(5,neighbour5);
    auto Edge6=List.get_newEdge(6,neighbour6);
    auto Edge7=List.get_newEdge(7,neighbour7);
    auto Edge8=List.get_newEdge(8,neighbour8);
    auto Edge9=List.get_newEdge(9,neighbour9);
    auto Edge10=List.get_newEdge(10,neighbour10);
    List.Edges.push_back(Edge1);
    List.Edges.push_back(Edge2);
    List.Edges.push_back(Edge3);
    List.Edges.push_back(Edge4);
    List.Edges.push_back(Edge5);
    List.Edges.push_back(Edge6);
    List.Edges.push_back(Edge7);
    List.Edges.push_back(Edge8);
    List.Edges.push_back(Edge9);
    List.Edges.push_back(Edge10);
    List.display();
    return 0;
}