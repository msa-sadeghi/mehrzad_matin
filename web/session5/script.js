// let name = prompt("Enter your name");
// let d = new Date();
// console.log(d);
// let time = d.getHours();
// let greeting = "Good ";
// if (time < 12) {
//     greeting += "Morning";
// }else if (time < 18) {
//     greeting += "Afternoon";    
// }
// else {      
//     greeting += "Evening";
// }
// console.log(greeting);
// console.log(time);
// console.log(name);
// // alert("Hello " + name + " "+ greeting + ", welcome to the JavaScript world!");

// document.body.innerHTML = "<h3>" + "Hello " + name +
//  " "+ greeting + ", welcome to the JavaScript world!" +"</h3><br>"


let firstElem = document.getElementById("first")
firstElem.innerHTML = "Hello World!"
firstElem.style.color = "red"
firstElem.style.fontSize = "50px"

let betweenElem  = document.createElement("h3")
betweenElem.innerText="BETWEEN"

firstElem.after(betweenElem)

let secondElem = document.getElementById("second")
secondElem.innerHTML = "How are you"
secondElem.style.color = "green"
secondElem.style.fontSize = "50px"