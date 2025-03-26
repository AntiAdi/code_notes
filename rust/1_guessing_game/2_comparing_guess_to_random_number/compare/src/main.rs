extern crate rand;
use std::io;
use rand::Rng;


use std::cmp::Ordering;


fn main() {
    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("Try your luck between 1 and 100 !");
    let mut chosen_number = String::new();
    
    
    /*
        *ERROR*
            warning: unused import: `std::io`
            --> src/main.rs:2:5
            |
            2 | use std::io;
            |     ^^^^^^^
            |
            = note: `#[warn(unused_imports)]` on by default

        *CAUSE*
            io was imported :
                use std::io
            but wasn't used. Instead this was used :
                std::io::
            instead of directly using :
                io::
        
        *CODE*
            std::io::stdin().read_line(&mut chosen_number).expect("Oops. You're Cooked !");
    */
    io::stdin().read_line(&mut chosen_number).expect("Oops. You're Cooked !");
    
    /*
        Over shadowing.
        
        u32 for unsigned 32 bit integer.
        
        .trim() to trim off spaces off the sides. Strings end with \n in here.
        
        The parse method on strings parses a string into some kind of number.
        Because this method can parse a variety of number types, we need to tell
        Rust the exact number type we want by using let chosen__number: u32.

        .expect() for error handling.
    */
    let chosen_number: u32 = chosen_number.trim().parse().expect("Please type a number!");

    match chosen_number.cmp(&secret_number){
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }

}