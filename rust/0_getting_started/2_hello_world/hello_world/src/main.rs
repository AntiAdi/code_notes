// println! calls a Rust macro. If it called a function instead, it would be entered as println (without the !)
// Most lines of Rust code end with a semicolon.

/*
    Before running a Rust program, you must compile it using the Rust
    compiler by entering the rustc command and passing it the name of your
    source file, like this:
        $ rustc main.rs
    If you have a C or C++ background, you’ll notice that this is similar to
    gcc or clang. After compiling successfully, Rust outputs a binary executable.
*/


fn main() {
    println!("Hello, world!");
}
