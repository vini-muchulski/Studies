#include <iostream>
#include <string>
#include <list>
using namespace std;

// https://www.youtube.com/watch?v=dXI9_9WoTVw

void printar_lista(list<int> &lista){ // se passar &lista, ele vai alterar a lista original

    for(list<int>::const_iterator it = lista.begin();it != lista.end();it++){ // const it = nao pode alterar o valor do iterador
        cout << *it << " "; // iterator is a pointer
    }
    cout << " " << endl;
}



void novo_jogador(int novo_jogador_xp ,list<int> &lista){ 

    // essa funcao insere o novo jogador na lista de forma ordenada
    // aqui ele compara o valor do iterador com o novo jogador e insere na posicao correta
    // se o valor do iterador for maior que o novo jogador, ele insere o novo jogador antes do iterador
    
    for(list<int>::iterator it = lista.begin();it != lista.end();it++){ 
        if(*it > novo_jogador_xp){ 
            lista.insert(it,novo_jogador_xp);
            return;
        }
    }
    lista.push_back(novo_jogador_xp);
}


int main() {
     list<int> all_players = {2,9,6,7,3,1,4,8,3,2,9};

     list<int> iniciantes; // rating 1-5
     list<int> pros; // 6 - 10

     for(list<int>::iterator it = all_players.begin();it != all_players.end();it++){
        int rating = *it; // desreferencia o iterador para pegar o valor do elemento
        if(rating > 5){
            //pros.push_back(rating);
            novo_jogador(rating,pros);
        }

        else{
            //iniciantes.push_back(rating);
            novo_jogador(rating,iniciantes);
        }

     }

     printar_lista(iniciantes);
     printar_lista(pros);



    
}