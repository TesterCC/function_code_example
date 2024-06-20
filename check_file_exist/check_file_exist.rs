use std::path::Path;

// need compiled, rust build cmd:
// rustc check_file_exist.rs && ./check_file_exist
// rustc -o cfe check_file_exist.rs && ./cfe
fn main() {
    let file_path = "./a.txt";
    
    if Path::new(file_path).exists() {
        println!("File exist");
    } else {
        println!("File doesn't exist");
    }
}
