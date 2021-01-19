#include <iostream>

using namespace std;

int main(int argc, char*argv[])
{
    string name;
    cout << "Let us start" << endl;
    cout << "Name? : ";
    // cin >> name;
    getline(cin, name);
    cout << "Hello " << name << endl;
    cout << "Welcome to C++ " << name <<endl;
    return 0;
}
