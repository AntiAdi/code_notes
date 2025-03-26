/*
    First, we add a line that lets Rust know we’ll be using the rand crate as
    an external dependency. This also does the equivalent of calling "use rand",
    so now we can call anything in the rand crate by placing rand:: before it.
*/
extern crate rand;

use std::io;

/*
    The Rng trait defines methods that random number generators implement,
    and this trait must be in scope for us to use those methods. 
*/
use rand::Rng;



fn main() {
       /*
        The rand::thread_rng function will give us the particular random number generator that we’re going to use.
        One that is local to the current thread of execution and seeded by the operating system.
        Next, we call the gen_range method on the random number generator.
        This method is defined by the Rng trait that we brought into scope with the use rand::Rng statement.
        The gen_range method takes two numbers as arguments and generates a random number between them.
        It’s inclusive on the lower bound but exclusive on the upper bound,
        so we need to specify 1 and 101 to request a number between 1 and 100.
    */
    let secret_number = rand::thread_rng().gen_range(1, 101);
    
    println!("The secret number is: {}", secret_number);   
}