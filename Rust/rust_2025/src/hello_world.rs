// use std::io; // Importa a biblioteca io do Rust
//use rand::Rng;
//use std::cmp::Ordering;


fn main() {
    println!("Olá, Rust!");

    let nome = String::from("Vinicius"); 
    
    //io::stdin().read_line(&mut nome).expect("Falha ao ler a linha");

    // Retira possíveis espaços em branco ao final da string
    let nome = nome.trim();

    println!("Bem-vindo, {}!", nome);
}