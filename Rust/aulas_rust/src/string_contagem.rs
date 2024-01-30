use std::io;

fn main() {

    println!("{}", "*".repeat(20)); // repeat() repete a string 20 vezes
    let mut s = String::new();
    println!("Digite uma frase: ");


    io::stdin()
    .read_line(&mut s) // read_line() lê a linha do console
    .expect("error ao ler console");

    println!("voce digitou: {}",s);
    println!("qntd de bytes {}", s.trim().len()); // trim() remove os espaços em branco
    println!("qntd de caracteres {}", s.trim().chars().count()); // trim() remove os espaços em branco
    // len() retorna a quantidade de bytes
    // chars().count() retorna a quantidade de caracteres

    println!("{}", "*".repeat(20));

    println!("maiusculo voce digitou {}", s.to_uppercase());  // to_uppercase() retorna a string em maiusculo

    println!("substituicao {}", s.replace("a", "v"));

}   

