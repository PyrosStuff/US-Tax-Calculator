console.log("Welcome to the US sales tax calculator!");
console.log("STATES");
console.log("1: Florida");
console.log("2: Georgia");
console.log("3: Tennessee");
console.log("4: South Carolina");
console.log("5: North Carolina");
console.log("6: Alabama");
console.log("7: Mississippi");

var state = parseInt(prompt("Please enter your state number: "));
var county = 0;

if (state == 1){
    console.log("You have selected: Florida.");
    county = parseInt(prompt("Select your county: "));
} else if (state == 2){
    console.log("You have selected: Georgia.");
    county = parseInt(prompt("Select your county: "));
} else if (state == 3){
    console.log("You have selected: Tennessee.");
    county = parseInt(prompt("Select your county: "));
} else if (state == 4){
    console.log("You have selected: South Carolina.");
    county = parseInt(prompt("Select your county: "));
} else if (state == 5){
    console.log("You have selected: North Carolina.");
    county = parseInt(prompt("Select your county: "));
} else if (state == 6){
    console.log("You have selected: Alabama.");
    county = parseInt(prompt("Select your county: "));
} else if (state == 7){
    console.log("You have selected: Mississippi.");
    county = parseInt(prompt("Select your county: "));
}

console.log("State: " + state);
console.log("County: " + county);
