// function outer(){
//     let counter =  0
//     function inner(){
//         counter++
//         console.log(counter)
//     }
//     return inner
// }

// const myCounter = outer()
// myCounter()
// myCounter()
// myCounter()

// function createCounter(){
//     let count = 0
//     return {
//         increment:function(){
//             count++
//             return count
//         },
//         decrement:function(){
//             count--
//             return count
//         },
//         getCount:function(){
//             return count
//         }
//     }
// }

// const counter1 = createCounter()
// console.log(counter1.increment())
// console.log(counter1.increment())
// console.log(counter1.decrement())
// console.log(counter1.getCount())
// console.log(counter1.decrement())

// const counter2 = createCounter()
// console.log(counter2.increment())



// function createIDGenerator(){
//     let lastID = 0
//     return function(){
//         lastID++
//         return `id: ${lastID}`
//     }
// }

// const generateID1 = createIDGenerator()
// console.log(generateID1())
// console.log(generateID1())
// console.log(generateID1())

// const generateID2 = createIDGenerator()
// console.log(generateID2())
// console.log(generateID2())
// console.log(generateID2())


function createCache(){
    const cache = {}
    return function(key, value){
        if(value !== undefined){
        cache[key] = value
        return `${value} saved in ${key}`
    }else{
        return cache[key]
    }

    }
}

const myCache = createCache()

myCache("name", "sara")
myCache("age", "30")
console.log(myCache("name"))
console.log(myCache("age"))