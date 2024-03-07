#include <iostream>

using namespace std;

// https://www.youtube.com/watch?v=HKfj0l7ndbc

class Node {
public:
    int data;
    Node* next;
};

void printar_links(Node* n){
    while(n != NULL){
        cout << n->data << " " << n->next << endl;
        //cout << n->data << " " << endl;
        n = n->next;
    }

}


int main() {
    // arrays sao estruturas que armazenam varios valores do mesmo tipo e tem um tamanho fixo
    // vector sao estruturas que armazenam varios valores do mesmo tipo e tem um tamanho variavel
    // vector eh uma classe da biblioteca padrao do c++
    // list sao estruturas que armazenam varios valores do mesmo tipo e tem um tamanho variavel e diferem dos vetores por nao terem acesso direto aos elementos

    // linked list eh uma estrutura de dados que armazena uma sequencia de elementos e cada elemento tem um ponteiro para o proximo elemento
    // linked list eh uma estrutura de dados dinamica, ou seja, o tamanho da lista pode mudar durante a execucao do programa


    Node* head = new Node();
    Node* segundo = new Node();
    Node* terceiro = new Node();

    head->data = 1;
    head->next = segundo;

    segundo->data = 2;
    segundo->next = terceiro;

    terceiro->data = 3;
    terceiro->next = NULL;

    printar_links(head);





    return 0;
}
