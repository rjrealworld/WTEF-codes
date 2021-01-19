#include <iostream>
#include <vector>

using namespace std;

vector <int> collatz(int number, vector <int> v)
{
    if (number == 4) 
    	return v;
    v.push_back(number);
    if (number % 2 == 0)
    	v = collatz(number / 2, v);
    else
       	v = collatz(3 * number + 1, v);
    return v;
}

int main()
{
    int number;
    cin >> number;
    vector <int> v;
    v = collatz (number, v);
    int i;
    for (i = 0; i < v.size(); i++)
       	cout << v[i] << " ";
    cout << "4 2 1";
    return 0;
}
