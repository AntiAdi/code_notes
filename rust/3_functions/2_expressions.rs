fn main(){
    let mut x : i64 = 4;
    let y = {
        x *= 3; //x becomes 12.
        x*5 //returns 12*5=60
    };

    println!("x is {}\ny is {}", x,y);
}