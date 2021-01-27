// Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

#include <iostream>
#include <vector>
using namespace std;

// Method 4 - Reversal Algorithm
// Time : O(n)
// Space: O(1)

void reverseArray(int arr[], int start, int end) 
{ 
    while (start < end) { 
        int temp = arr[start]; 
        arr[start] = arr[end]; 
        arr[end] = temp; 
        start++; 
        end--; 
    } 
} 
  
void leftRotate(int arr[], int d, int n) 
{ 
    if (d == 0) 
        return; 
    d = d % n; 
    reverseArray(arr, 0, d - 1); 
    reverseArray(arr, d, n - 1); 
    reverseArray(arr, 0, n - 1); 
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