#include <iostream> 
#include <stack>

using namespace std; 

bool IsRedundantBrackets(string exp) { 
	stack<char> st; 
	for (const char ch : exp) { 
		if (ch == ')') { 
			char top = st.top(); 
			st.pop(); 

			bool reducdant = true; 

			while (top != '(') {
				if (top == '+' || top == '-' ||top == '*' || top == '/') 
					reducdant = false; 
				top = st.top(); 
				st.pop(); 
			} 
			if (reducdant == true) 
				return true; 
		} 

		else
			st.push(ch); 
	} 
	return false; 
} 

int main() 
{ 
	string expression;
    getline(cin, expression);
    cout << IsRedundantBrackets(expression) << endl;
    return 0;
} 
