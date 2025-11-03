function convertTemperature(){
    let tempInput = document.getElementById("tempInput").value
    let tempFrom = document.getElementById("tempFrom").value
    let tempTo = document.getElementById("tempTo").value
    let tempResult = document.getElementById("tempResult")
    if(tempInput === ""){
        tempResult.textContent = "لطفا دما را وارد نمائید"
        tempResult.style.display = "block"
        tempResult.style.backgroundColor = "red"
        return
    }
    let temp = Number(tempInput)
    let result
    if(tempFrom === tempTo){
        result = temp
    }else if(tempFrom === "celsius"){
        if(tempTo === "fahrenheit"){
            result = temp * 2
        }else if(tempTo === "kelvin"){
            result = temp * 3
        }

    }
    tempResult.textContent = `نتیجه ${result}`
    tempResult.style.display = "block"

}