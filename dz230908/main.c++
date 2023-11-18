

#include <iostream>

using namespace std;

int main()
{
    int size,Arraylist[10];
    size = 10;
    srand(time(0));
    for (int i=0; i<size;i++)
    {
        Arraylist[i] = -100 + rand() % 201;
    }
   
    int maximum = Arraylist[0];
    for (int i=1; i<size;i++)
    {
        if (Arraylist[i]>maximum){
            maximum = Arraylist[i];
        }
    }
    
    
      for (int i=0; i<size;i++)
    {
        cout<<Arraylist[i]<<" ";
    }
    
    cout<<endl<<maximum<<endl;
    
    return 0;
}
