const SPEED_OF_LIGHT: u32 = 299_792_458;

fn main() {
    println!("Hello world!");
    let const_text = "test";//not muttable
    let mut text = "test mut";
    let number = 1;
    println!("Text: {}, number: {}", text, number);
    text = "change muttable variable";
    println!("{}", text);
    balance();
    balance2();
    const_void();
}

fn balance() {
    let balance = 500;
    let balance = 700;
    println!("{}", balance);
}

fn balance2() {
    let balance = 500;
    let balance = balance*2;
    println!("{}", balance);
}

fn const_void() {
    println!("{}", SPEED_OF_LIGHT);
}