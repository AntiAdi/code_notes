/*
    To obtain user input and then print the result as output, we need to bring
    the io (input/output) library into scope. The io library comes from the
    standard library (which is known as std):
*/
use std::io;

//fn main() is the entry of the program.
fn main() {
    println!("Guess the number!\nPlease input your guess.");
    
    /*
        mutable variable guess. 
        ::new() is an associated function (a function that is tied to the String type) that creates a new String.
        When you call String::new(), it returns an empty String (not a reference to a string, but a fully owned string).
    */
    let mut guess = String::new();

    /*
        io::stdin()
            This is how Rust knows you're trying to get input from the user.
            io is short for "input/output," and stdin stands for "standard input," which is just a fancy way of saying "the keyboard."
            So, io::stdin() is Rust’s way of saying, “I want to read something from the user.”

        .read_line(&mut guess)
            After you’ve set up reading from the user, .read_line() is the method you use to actually grab what they type.
            You give it a variable to store the input, and it will fill that variable with the text the user types.
            Here, &mut guess is where the input will be saved.
            The &mut means "borrow this variable as mutable," meaning it’s okay to change the guess variable
            (because the program will fill it with whatever the user types).

        .expect("Failed to read line")
            This part is just there to make sure things go smoothly.
            If there’s any problem reading the input (like if the program crashes), it will stop and show an error message: "Failed to read line".
            This helps make sure your program handles any unexpected issues clearly.
    */
    io::stdin().read_line(&mut guess).expect("Failed to read line");

    
    println!("You guessed: {}", guess);
}