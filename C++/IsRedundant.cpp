#include <iostream>
#include <stack>

using namespace std;

bool IsRedundantBrackets(string exp) {
    int brackets = 0;
    int operation = 0;
    for (int i = 0; i < exp.size(); i++) {
        if (exp[i] == '(' && exp[i + 2] == ')')
            return true;
        if (exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/')
            operation++;
        if (exp[i] == '(')
            brackets++;
    }
    if (brackets > operation)
        return true;
    return false;
}

int main() {
    string expression;
    getline(cin, expression);
    cout << IsRedundantBrackets(expression) << endl;
    return 0;
}

//Sample Input 1: "((a + b))"
//Sample Output 1: 1

//Sample Input 2: "(a + (a + b))"
//Sample Output 2: 0