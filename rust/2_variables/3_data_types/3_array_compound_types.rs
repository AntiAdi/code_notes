fn main(){
    let our_array = [1,2,3,4,5,6,7,69];
    
    /* 
        println!("First and last element is : {} and {}", our_array[0], our_array[-1]);
           
            error: negative integers cannot be used to index on a `[{integer}; 8]`
            --> 3_array_compound_types.rs:3:79
            |
            3 |     println!("First and last element is : {} and {}", our_array[0], our_array[-1]);
            |                                                                               ^^ cannot use a negative integer for indexing on `[{integer}; 8]`
            |
            help: to access an element starting from the end of the `[{integer}; 8]`, compute the index
            |
            3 |     println!("First and last element is : {} and {}", our_array[0], our_array[our_array.len() -1]);
            |                                                                               +++++++++++++++
    */

    println!("First and last element is : {} and {}", our_array[0], our_array[our_array.len()-1]);

}