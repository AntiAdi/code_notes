fn main(){
    let our_tuple : (u8, u8, f64, &str) = (1, 2, 3.2, "Hello");
    
    println!("Elements of Our Tuple : {}, {}, {}, {}", our_tuple.0 , our_tuple.1, our_tuple.2, our_tuple.3);
    
    //error !
    // println!("Directly Printing the tuple : {}", our_tuple);
    //{:#?} for pretty print. {:?} for normal print.
    println!("Directly Printing the tuple : {:#?}", our_tuple);
    println!("Directly Printing the tuple : {:?}", our_tuple);

    println!("let (a, b, c ,d) = our_tuple;");
    let (a, b, c ,d) = our_tuple;
    println!("c is {}", c);
}