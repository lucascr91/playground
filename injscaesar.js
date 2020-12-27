
function caesar(message, key, mode){
    let SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    let translated=''
    let translatedIndex

    for (symbol of message){
        if (SYMBOLS.includes(symbol)){
            let symbolIndex=SYMBOLS.indexOf(symbol)
            if (mode=="encrypt"){
                translatedIndex=symbolIndex+key
            }
            else if (mode=="decrypt"){
                translatedIndex=symbolIndex-key
            }
            if (translatedIndex>=SYMBOLS.length){
                translatedIndex = translatedIndex-SYMBOLS.length
            }
            else if (translatedIndex<0){
                translatedIndex = translatedIndex-SYMBOLS.length
            }
            translated=translated+ SYMBOLS[translatedIndex]}
        else {
            translated=translated+symbol
        }
    }
    return translated
}

console.log(caesar(message="This is a secret message", key=13, mode='encrypt'))