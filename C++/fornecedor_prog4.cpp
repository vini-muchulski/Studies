
#include <iostream>
#include <vector>
#include <string>

#include <sstream>

#include <iomanip>

using namespace std;

class Pessoa{
//atributos
protected:
string m_nome;
string m_endereco;
string m_telefone;

// metodos

public:

Pessoa(){}



Pessoa(string nome,string endereco="", string telefone=""){
    m_nome = nome;
   m_endereco= endereco;
   m_telefone= telefone;
}

string get_nome(){
    return m_nome;
}

string get_endereco(){
    return m_endereco;
}

string get_telefone(){
    return m_telefone;
}

/*
string get_(){
    return
}
*/

void set_nome(string parametro){
    m_nome = parametro;
}

void set_endereco(string parametro){
    m_endereco = parametro;
}


void set_telefone(string parametro){
    m_telefone = parametro;
}
string show_info(){
 stringstream palavra;

 palavra << "Nome : " << m_nome << " Endereco: " << m_endereco << " Telefone: " << m_telefone << " \n";

return palavra.str();
}
};


class Fornecedor: public Pessoa{
protected:
//atributos
float valorCredito;
float valorDivida;

public:
//metodos
Fornecedor(string nome,string endereco, string telefone, float p_valorCredito, float p_valorDivida): Pessoa(nome,endereco,telefone){
valorCredito  = p_valorCredito;
valorDivida = p_valorDivida;
}

float get_credito(){
    return valorCredito;
}

float get_Divida(){
    return valorDivida;
}

void set_Credito(float valor){
    valorCredito = valor;
}

void set_Divida(float valor){
    valorDivida = valor;
}

float obter_saldo(){
    float saldo = valorCredito - valorDivida;
    return saldo;
}

};

class Empregado : public Pessoa{
protected:
int codigoSetor; 
float salarioBase;
float imposto;



public:
Empregado(string nome,string endereco, string telefone, int p_codigoSetor, float p_salarioBase,float p_imposto): Pessoa(nome,endereco,telefone){
codigoSetor = p_codigoSetor;
salarioBase = p_salarioBase;
imposto = p_imposto/100;
}

void set_codigoSetor(int codigo){
    codigoSetor = codigo;
}

int get_codigoSetor(){
    return codigoSetor;
}

void set_imposto(float imposto_p){
    imposto = imposto_p;
}

float get_imposto(){
    return imposto;
}

void set_salario(float salr){
    salarioBase = salr;
}

float get_salario(){
    return salarioBase;
}

void calc_salario(){
    salarioBase = salarioBase - (salarioBase*imposto);
}


};

class Adm: public Empregado{
    protected:
    float ajudaDeCusto;



    public:
    Adm(string nome,string endereco, string telefone, int p_codigoSetor, float p_salarioBase,float p_imposto,float custo_auxilio): 
    Empregado(nome,endereco,telefone,p_codigoSetor,p_salarioBase,p_imposto){
    ajudaDeCusto = custo_auxilio;
    }

    void calc_salario(){
        float salario = get_salario() - (get_imposto()*get_salario()) + ajudaDeCusto;
        set_salario(salario);
    }


};


class Operario: public Empregado{
protected:

float valor_producao;
float comissao;

public:
Operario(string nome,string endereco, string telefone, int p_codigoSetor, float p_salarioBase,float p_imposto,float p_valorProducao,float porcen_comisssao): Empregado(nome,endereco,telefone,p_codigoSetor,p_salarioBase,p_imposto){
valor_producao = p_valorProducao;
comissao = porcen_comisssao/100;
}

void calc_salario(){
        float salario = get_salario() - (get_imposto()*get_salario()) + valor_producao*comissao;
        set_salario(salario);
    }

};


class Vendedor: public Empregado{
protected:

float valor_vendas;
float comissao;

public:
Vendedor(string nome,string endereco, string telefone, int p_codigoSetor, float p_salarioBase,float p_imposto,float p_valorvendido,float porcen_comisssao): Empregado(nome,endereco,telefone,p_codigoSetor,p_salarioBase,p_imposto){
valor_vendas = p_valorvendido;
comissao = porcen_comisssao/100;
}

void calc_salario(){
        float salario = get_salario() - (get_imposto()*get_salario()) + valor_vendas*comissao;
        set_salario(salario);
    }

};
int main(){

Fornecedor fnc1("Fornecedor 1", "Rua Paradis", "2710", 5000, 3000);

cout << fnc1.show_info() << endl;
cout<< "Saldo = " << fnc1.obter_saldo() << endl;


Empregado emp1("Empregado 1", "Rua almeida", "1234",240,10000,5);
emp1.calc_salario();
cout << "salario " << emp1.get_salario() << endl;
cout << emp1.show_info() << endl;


cout << "-------------------- \n" << endl;

Adm admin("Ademir ", "Rua Faria Lima", "4587",062,20000,5,2000);
admin.calc_salario();
cout << "salario " << admin.get_salario() << endl;
cout << admin.show_info() << endl;


cout << "-------------------- \n" << endl;
Operario protelario("Proletario ", "Rua Marx", "1616",666,1000,2,1000,5);
protelario.calc_salario();
cout << "salario " << protelario.get_salario() << endl;
cout << protelario.show_info() << endl;


cout << "-------------------- \n" << endl;          //codigo    imposto
Vendedor corretor("Vendedor de curso ", "Rua Udemy", "2999",199,1000,5,5000,10);
corretor.calc_salario();
cout << "salario " << corretor.get_salario() << endl;
cout << corretor.show_info() << endl;



    return 0;
}