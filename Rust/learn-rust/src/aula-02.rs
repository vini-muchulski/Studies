const SEGUNDOS_EM_MINUTOS: u32 = 60;
const MINUTOS_EM_HORAS: u32 = 60;
const SEGUNDOS_EM_HORAS: u32 = SEGUNDOS_EM_MINUTOS * MINUTOS_EM_HORAS;

fn main() {
    //escopo
    let mut total = 25; // variavel inutil  colocase um _ antes dela
    println!("trabalhou {} horas", total);

    total = 30; // variavel inutil  colocase um _ antes dela
    println!("trabalhou {} horas na semana", total);

    {
        let total = "quarenta"; // variavel inutil  colocase um _ antes dela
        println!("trabalhou {} horas na semana", total); //outro escopo
    }

    println!("-------------------------------------");
    println!(" ");

    let total_em_segundos = total * SEGUNDOS_EM_HORAS;
    println!("trabalhou {} segundos", total_em_segundos);
} // fim

//drop

// RAII
