fn main(){
    let u_integer : u8 = 1;
    // let i_integer : i8 = 100;
    // let our_float : f32 = 420.6969;
    let decision : bool = true;
    let our_char : char = 'x';

    println!("u_integer was {}", u_integer);
    
    //Rust doesn't allow bufferoverflow.
    // u_integer -= 2;
    // println!("u_integer after substracting 2 is {}", u_integer);

    println!("Our decision is {}", decision);

    println!("Our character is {}", our_char);
}