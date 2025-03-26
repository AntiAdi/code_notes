extern crate rand;
use std::io;
use rand::Rng;

use std::cmp::Ordering;


fn main() {
    let secret_number = rand::thread_rng().gen_range(1, 101);

    loop{
            println!("Try your luck between 1 and 100 ! 0 to Quit !");
            let mut chosen_number = String::new();
        
            io::stdin().read_line(&mut chosen_number).expect("Oops. You're Cooked !");
        
            /*
                Switching from an expect call to a match expression is how you generally
                move from crashing on an error to handling the error. Remember that parse
                returns a Result type and Result is an enum that has the variants Ok or Err.
            */
            let chosen_number: u32 = match chosen_number.trim().parse(){
                Ok(num) => num,
                Err(_) => continue,
            };
    
            match chosen_number.cmp(&secret_number){
                Ordering::Less => println!("Too small!"),
                Ordering::Greater => println!("Too big!"),
                Ordering::Equal => {
                    println!("You win!");
                    break;
                }
            }
    }

}