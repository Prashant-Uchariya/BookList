#include<iostream>
using namespace std;

int main()
{
	int n;
	int i,k;
	int j=0;
	cout<<"Enter the number of digits in series : ";
	cin>>n;
	int sum=0;
	for(k=1;k<=n;k++)
	{
	
	for(i=1;i<=k;i++)
	{
	if(k%i==0)
     j++;
	}
	if(j==2)
	sum=sum+(k*k*k);
	else
	sum=sum+(k*k);	
	


}

cout<<"The sum of series is : "<<sum;
}

