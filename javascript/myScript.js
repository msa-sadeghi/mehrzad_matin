let basicNum1 = document.getElementById("basicNum1")
let basicNum2 = document.getElementById("basicNum2")
let basicOp = document.getElementById("basicOp")
let basicResult = document.getElementById("basicResult")

function add(a, b){
    return a + b
}
function sub(a, b){
    return a - b
}
function mul(a, b){
    return a * b
}
function div(a, b){
    return a / b
}
function pow(a, b){
    return a ** b
}
function rem(a, b){
    return a % b
}


function calculateBasic(){
    let basicOpVal = basicOp.value
    let basicNum1Val = Number(basicNum1.value)
    let basicNum2Val = Number(basicNum2.value)
    let res
    if(basicOpVal === 'add'){
        res = add(basicNum1Val, basicNum2Val)
    }
    basicResult.innerHTML = res
    basicResult.style.display = "block"
}