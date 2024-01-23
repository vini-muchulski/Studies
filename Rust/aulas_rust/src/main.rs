use std::io;

fn main() {
    let mut s = String::new();
    println!("Digite uma frase: ");


    io::stdin()
    .read_line(&mut s)
    .expect("error ao ler console");

    println!("voce digitou: {}",s);

}
