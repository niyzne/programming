import * as calculator from "./calculator.js";

while (true) {
  let userChoice = prompt("Welcome to BMI calculator, please make your choice [1] KG and CM, [2] Lb and Ft [q]: ");
  if (userChoice == "1") {
    console.log("Mode: KG and CM");
    let weight = prompt("Enter your weight: ");
    let height = prompt("Enter your height: ");
    console.log(calculator.bmiCalculator(weight, height));
  } else if (userChoice == "2") {
    console.log("Mode: Lb and Ft");
    let weight = prompt("Enter your weight: ");
    poundWeight = weight * 0.453592;
    let height = prompt("Enter your height: ");
    feetHeight = height * 30.48;
    console.log(calculator.bmiCalculator(poundWeight, feetHeight));
  } else if (userChoice == "q") {
    break
  } else {
    console.log("wrong input, try again")
  }
}
