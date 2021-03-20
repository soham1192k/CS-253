#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("new.txt","r",stdin);
    int n;cin>>n;int b;cin>>b;
    vector<int>v[n];
    for(int i=0;i<n;i++){
        for(int j=0;j<b;j++){
            int u;cin>>u;
            v[i].push_back(u);
        }
    }
    vector<int>hold[n];
    for(int i=0;i<n;i++){
        for(int j=0;j<b;j++){
            if(v[i][j]==1) hold[i].push_back(j);
        }
    }
    int k;cin>>k;
    vector<bool>visited(b,false);
    vector<bool>available(n,true);
    vector<int>taken;
    for(int itr=1;itr<=k;itr++){
        int maxx=-1;int id=-1;
        for(int i=0;i<n;i++){
            int cnt=0;
            if(available[i]){   
                for(auto x:hold[i]){
                    if(!visited[x]) cnt++;
                }
            }
            else continue;
            if(cnt>maxx){
                maxx=cnt;id=i;
            }
        }
        available[id]=false;
        for(auto x:hold[id])
            visited[x]=true;
        taken.push_back(id+1);
    }
    for(auto x:taken) cout<<x<<'\n';
    return 0;
}