fn main() {
    //println! --> Print line macro
    println!("Hello, world!");

    //declaring variables. By default are immutable(cannot be changed later). 
    let x = 1;
    println!("x is {}", x) ;

    //making mutable variables
    let mut y ;
    y = 14 ;
    println!("y is {}", y) ;
    y = 42 ;
    println!("y now mutated to {}", y) ;

}
