#include<iostream>
using namespace std;
int main()
{
	int f,l,mid,key,a[15],n,i;
	cout<<"\nEnter The Number of Elements in Array: ";
	cin>>n;
	cout<<"Enter The Number of Elements : ";
	for(i=0;i<n;i++)
		cin>>a[i];


	int j,temp;

	for(i=0;i<n;i++)

	{
	   for(j=0;j<n-i-1;j++)
	     if(a[j]>a[j+1])
	     {
		    temp=a[j];
		    a[j]=a[j+1];
		    a[j+1]=temp;

	     }



	}
	cout<<"Sorted Array is: ";
	for(i=0;i<n;++i)
	   cout<<a[i]<<"\n";

	cout<<"Enter The Number To Be search: ";
	cin>>key;
	f=0;
	l=n-1;
	mid=(f+l)/2;
	 while(f<=l)
	 {
	 	if(a[mid]==key)
	 	{
	 		cout<<key<<" Found At "<<"Location "<<mid+1;
	 	  break;
	    }
	 	if(a[mid]<key)
	 	{
	 		f=mid+1;
		 }

	 	else
		   l=mid-1;
	 	mid=(f+l)/2;
	 }
	if(f>l)
		cout<<"Not Found "<<key;



}





