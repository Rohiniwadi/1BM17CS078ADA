#include<iostream>
using namespace std;
 
void find(int ,int ,int);

int  main()
{
  int t,k,N,a[100];
  cin>>t;
  for(int i=0;i<t;i++)
  {
    cin>>N>>k;
    for(int j=0;j<N;j++)
     {
       cin>>a[j];
     }
     find(N,k,a);
   } 
 return 0;
}
 
void find(int N,int k,int a[])
{
  int f=0;
  int l=N-1;
  int m;
  m=(l+f)/2;
  while(f<=l)
   {
     if(k == a[m])
      { cout<<"1";}
     else if(k<a[m])
      { l=m-1;}
     else
      {f=m+1;}
   }
   if(f>l)
   { cout<<"-1";}
}
    

     

