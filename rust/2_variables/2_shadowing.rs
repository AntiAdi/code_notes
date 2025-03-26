/*
    In Rust, the r#""# syntax is used for raw string literals,
    which allow you to write strings that include special characters like newlines, quotes, and backslashes without having to escape them.
    This is particularly useful when you need to work with strings that contain characters like " or \ that would normally require escaping.
    
    How it works:
        The r#""# syntax starts and ends the raw string literal.
        
        The # can be repeated (e.g., r##""##) if you need to include a # inside the string.
        This is to avoid confusion with the delimiter itself.
*/





fn main(){
    println!(r#"
let x:i32 = 10;
println!("Value of x is {{}}",x );

let x:i32 = 13;
println!("Value of x is {{}}",x );

let x:&str = "this_text";
println!("Value of x is {{}}",x );
"#);


    let x:i32 = 10;
    println!("Value of x is {}",x );

    let x:i32 = 13;
    println!("Value of x is {}",x );

    let x:&str = "this_text";
    println!("Value of x is {}",x );

}   