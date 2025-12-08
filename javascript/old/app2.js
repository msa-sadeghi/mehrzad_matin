// let colors = ["red", "blue",  "purple", "yellow"]
// let new_colors = colors.map(function(c){
//     return c.toUpperCase()
// })
// console.log(new_colors)
// let filtered_colors = colors.filter(function(c){
//     return c[0] == "r"
// })
// console.log(filtered_colors)
// users = [
//     {
//         id:1,
//         name:"sara",
//         age : 32
//     },
//     {
//         id:2,
//         name:"reza",
//         age : 22
//     },
//     {
//         id:1,
//         name:"artin",
//         age : 35
//     },
// ]
// let filtered_users = users.filter(function(u){
//     return u.age > 30
// })
// console.log(filtered_users)








// // for(let i = 0; i < colors.length; i+=3){
// //     console.log(colors[i])
// // }
// // let my = function(c, index){
// //     if(index % 3 == 0)
// //     console.log(c, index)
// // }
// // colors.forEach(my)

// // for(let c in colors){
// //     console.log(colors[c])
// // }
// // for(let c of colors){
// //     console.log(c)
// // }


// const my = (name, age) => {
//     let message = `hello ${name}, you are ${age}`
//     return message
// }

// console.log(my("sara", 30))


// const add = (a,b) => a + b
// console.log(add(7, 8))

let numbers = [1,2,3,4,5,6]
let doubled = numbers.map((n) => n * 2)
console.log(doubled)

let evenNumbers = numbers.filter(x => x % 2 == 0)
console.log(evenNumbers)
console.log(doubled)
let new_odd = numbers.map(n => {
    if(n % 2 == 0){
        return n + 1
    }
    return n
})
console.log(new_odd)