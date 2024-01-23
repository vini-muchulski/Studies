fn main() {
    let frase : &str = "teste string";
    //contem a variavel inicial onde a string comeca

    
    println!("{}",frase);

    //heap string -- string dinamica
    let mut s = String::new();
    s.push_str("vini");
    println!("{}",s);
    
}
