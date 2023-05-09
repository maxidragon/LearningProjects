use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    guess = guess.trim().to_string();
    if guess == "5" {
        println!("You win!");
    } else {
        println!("You lose!");
    }
}
