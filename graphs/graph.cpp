#include<iostream>
#include<list>
#include<unordered_map>

using namespace std;

class graph{
public:
     unordered_map<int, list<int> >adj;

     void addEdge(int u, int v, bool direction){
        // dirn = 0 -> undirected graph
        // dirn = 1 -> directed graph

        adj[u].push_back(v);

        if(direction == 0){
            adj[v].push_back(u);
        } 
     }

     void printList(){
        for(auto i:adj){
            cout<<i.first<<"->";
            for(auto j: i.second){
                cout<<j<<",";
            }
            cout<<endl;
        }
     }

};

int main(){
    int n,m;
    cout<<"Nodes: "<<endl;
    cin>>n;

    cout<<"Edges: "<<endl;
    cin>>m;

    graph g;

    for(int i=0; i<m; i++){
        int u,v;

        cin>>u>>v;
        g.addEdge(u, v, 0);
    }

    g.printList();
}

