#include <iostream>
using namespace std;


int getMax(int num1, int num2){
    int result = (num1 > num2) ? num1: num2;

    return result;
}


int main() {

    cout << getMax(1, 2);

    return 0;
}