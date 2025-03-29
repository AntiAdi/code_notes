fn main(){
    let mera_faisla = true;

    let bank_balance = if mera_faisla {
        println!("mera faisla was {}. bank balance goes to 696969", mera_faisla);
        696969
    }
    else {
        println!("mera faisla was {}. bank balance goes to 0", mera_faisla);
        0
    };

    println!("bank balance you brokie ! {}", bank_balance);
}