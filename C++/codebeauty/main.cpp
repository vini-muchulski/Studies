#include <iostream>
#include <string>
#include <list>
using namespace std;

int main() {
    list<int> numbers;

    numbers.push_back(1);
    numbers.push_back(2);
    numbers.push_front(3);

    numbers.erase(numbers.begin()); // passar um ponteiro para o elemento que queremos apagar

    
    for(list<int>::iterator it = numbers.begin();it != numbers.end();it++){ // iterator works like a pointer
        cout << *it << endl; // iterator is a pointer
       
    }
    
}