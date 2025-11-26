let basicNum1 = document.getElementById("basicNum1")
let basicNum2 = document.getElementById("basicNum2")
let basicOp = document.getElementById("basicOp")
let basicResult = document.getElementById("basicResult")
let historyListElement = document.getElementById("historyList")

historyList = []

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
    let basicOpValText 
    let basicNum1Val = Number(basicNum1.value)
    let basicNum2Val = Number(basicNum2.value)
    let res
    if(basicOpVal === 'add'){
        res = add(basicNum1Val, basicNum2Val)
        basicOpValText = "+"
    }else if(basicOpVal === 'subtract'){
        
        res = sub(basicNum1Val, basicNum2Val)
        basicOpValText = "-"
    }
    basicResult.innerHTML = res
    basicResult.style.display = "block"
    const basicOpText = `${res} = ${basicNum1Val} ${basicOpValText} ${basicNum2Val}`
    addToHistory(basicOpText)
}



function addToHistory(calculation){
    historyList.unshift(calculation)
    if(historyList.length > 10){
        historyList.pop()
    }
    updateHistoryList()
}

function updateHistoryList(){
    if(historyList.length === 0){

        historyListElement.innerHTML = '<p/>تاریخچه ای وجود ندارد<p>'
        return
    }
    historyListElement.innerHTML = historyList.map(item => 
        `<div class ="history-item">${item}</div>`
    ).join('')
}



function clearHistory(){
    historyList = []
     historyListElement.innerHTML = '<p/>تاریخچه ای وجود ندارد<p>'
}