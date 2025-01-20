fn main() {
    let horas: i16 = 24 * 7;
    println!("horas na semana {}", horas);

    let y = 456_654_27;
    println!("valor y = {}", y);

    let x_float = 42.1;
    println!("valor x_float = {}", x_float);

    let texto = "ola mundo";
    println!("texto = {}", texto);

    println!("-------------- \n");
    println!("tupla \n");

    let mut numbers = (1, 2, 3.5);
    println!("{:?} \n", numbers);
    println!("primeiro elemento pos 0 = {:?}", numbers.0);

    let (a, _b, _c) = numbers;
    println!("A = {:?}", a);

    numbers.0 = 50;
    println!("{:?} \n", numbers);
    println!("primeiro elemento pos 0 = {:?}", numbers.0);

    println!("-------------- \n");
    println!("array \n");

    let valores_array = [1.1, 2.0, 3.3];
    println!("{:?} \n", valores_array);
    println!("{:?} \n", valores_array[0]);

  println!("-------------- slice \n");
  println!("{:?} \n", &valores_array[1..]);
}
