//use std::io;
use rand::Rng;
//use std::cmp::Ordering;

fn main() {
    println!("Bem-vindo ao jogo de adivinhação!");

    let numero_secreto = rand::thread_rng().gen_range(1.. 101);

    println!("O número secreto é: {}", numero_secreto);

}