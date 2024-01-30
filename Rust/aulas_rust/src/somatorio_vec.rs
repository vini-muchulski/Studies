use std::io;

fn clean(c: &str) -> i32 {
    c.trim().parse().expect( "erro ao converter")
}


fn main() {

    println!("{:-^40}", "calculadora"); // repeat() repete a string 20 vezes
    let mut s = String::new();
    
    let banner = 
    "
    Digite numeros
    separados por virgula e
    veja o somatorio";

    println!("{banner}");


    io::stdin()
    .read_line(&mut s) // read_line() lê a linha do console
    .expect("error ao ler console");

    let nums: Vec<i32> = s.split(",").map(clean).collect();

    let result: i32 = nums.iter().sum();

    println!("{}\n", "*".repeat(20));

    println!("voce digitou: {:?}",nums);
    println!("soma {}", result);
    

}   

