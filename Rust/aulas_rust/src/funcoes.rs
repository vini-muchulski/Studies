

fn say_hello(nome: &str){
    println!("ola mundo {}", nome)
}

fn soma(x :i32, y :i32) -> i32 {
 return x + y;

}




fn convert_to_numb(palavra: &str) ->i32{
   return palavra.parse().unwrap();
}




fn main() {

say_hello("vini");
let resultado = soma(32,8);
println!("resultado = {resultado}");





let input = "56 4 10";

let res: Vec<i32> = input
.split(' ')
.map(convert_to_numb)
.map(|n| n*2)
.collect();

println!("{:?}", res);
}   

