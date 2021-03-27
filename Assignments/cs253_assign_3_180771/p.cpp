#include<bits/stdc++.h>
using namespace std;
int main(int argc, char ** argv)
{
	int a,b;
	scanf("%d%d",&a,&b);
	cout<<a<<","<<b<<'\n';
	a=abs(a);
	b=abs(b);
	if(a%2==0){
		if(b%2==0){
			cout<<"[message]a and b are both even\n";
		}
		else if(b%3==0){
			cout<<"[message]a is even and b is an odd multiple of 3\n";
		}
		else{
			cout<<"[message]a is even and b is not divisble by 2 or 3\n";
		}
	}
	else{
		if(b%2==1){
			cout<<"[message]a and b are both odd\n";
		}
		else if(b%5==0){
			cout<<"[message]a is odd and b is a multiple of 5\n";
		}
		else{
			cout<<"[message]a is odd and b is not divisible by 5\n";
		}
	}
	return 0;
}