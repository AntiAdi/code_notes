fn main(){
    let countdown_total : i32 = 10 ;
    
    for countdown in (1..countdown_total+1).rev() {
        println!("{}",countdown);
    }

    let array_of_words = ["Get", "Set", "Go"];

    for word in array_of_words.iter() {
        println!("{}", word);
    }

    println!("Liftoff !");

}