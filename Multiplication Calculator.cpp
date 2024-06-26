/**
 * Practice Problem ~ Shadman S.
 * Multiplication-Table Calculator 
 */
 
#include <iostream>
using namespace std;

void multiplicationTable(int table,int start, int end){ // Function to calculate the (numbers x numbers)
    
    while (start <= end){ // while loop to print the multiplication-table result
        cout << table << " x " << start << " = " << table*start << endl;
        start++;
    }
}

int main()
{
    int table; // Declaring a variable for taking in numbers and finding that numbers multiplication table
    int end; // Another declared variable for taking in numbers for the stopping point
    int start; // variable to start the operation from
    
    start = 0;
    
    cout << "Enter the number for multiplication table:  ";
    cin >> table;
    
    cout << "Multiply till what number?" << endl;
    cout << "Enter the number: ";
    cin >> end;
    
    cout << "Multiplication Table of: " << table << endl;
    
    multiplicationTable( table,start, end);
}
