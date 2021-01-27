// Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

#include <iostream>
#include <vector>
using namespace std;

// Method 1
// Time : O(n)
// Space: O(d)

  
void leftRotate(int arr[], int d, int n) 
{ 
    vector <int> temp;
    int index = 0;
    for (int i = 0; i < d; i++)
        temp.push_back(arr[i]);
    for (int i = d; i < n; i++) 
         arr[index++] = arr[i];
    for (int i = 0; i < d; i++)
        arr[index++] = temp[i];
} 

void printArray(int arr[], int n) 
{ 
    for (int i = 0; i < n; i++) 
        cout << arr[i] << " "; 
}

int main() {
    int arr[] = { 1, 2, 3, 4, 5, 6, 7 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    leftRotate(arr, 2, n); 
    printArray(arr, n); 
  
    return 0; 
}