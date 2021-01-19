#include <iostream>
#include <vector>
#include <cmath> 

using namespace std;

vector <int> generate(int numRows) 
{
	vector <int> pascal;
	for (int i = 0; i < numRows; i++)
    	pascal.push_back (pow(11, i));
  	return pascal;
}

int main()
{
	int numRows;
	cin >> numRows;
	vector <int> result = generate (numRows);

	for (const int i: result)
	    cout << i << endl;
	
    return 0;
}
