


use std::io;

fn main() {
    println!("Olá, Rust!");

    println!("Digite seu nome:");
    let mut nome = String::new();
    io::stdin().read_line(&mut nome).expect("Falha ao ler a linha");

    // Retira possíveis espaços em branco ao final da string
    let nome = nome.trim();

    println!("Bem-vindo, {}!", nome);
}



