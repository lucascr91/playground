function caesar(message, key, mode){
    let SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    let translated=''
    let translatedIndex=0

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
                translatedIndex = translatedIndex+SYMBOLS.length
            }
            translated=translated+ SYMBOLS[translatedIndex]}
        else {
            translated=translated+symbol
        }
    }

    return document.querySelector('.result').innerHTML =translated
}

function encrypt() {
    return caesar(message=document.getElementById("user-text").value,
    key=Number(document.getElementById("key").value), mode="encrypt")
}

function decrypt() {
    return caesar(message=document.getElementById("user-text").value,
    key=Number(document.getElementById("key").value), mode="decrypt")
}

function copy(){
    encText=document.getElementById("enc-text").value
    return copyTextToClipboard(encText)
}

function copyTextToClipboard(text) {
  var textArea = document.createElement("textarea");

  textArea.style.position = 'fixed';
  textArea.style.top = 0;
  textArea.style.left = 0;
  textArea.style.width = '2em';
  textArea.style.height = '2em';
  textArea.style.padding = 0;
  textArea.style.border = 'none';
  textArea.style.outline = 'none';
  textArea.style.boxShadow = 'none';
  textArea.style.background = 'transparent';
  textArea.value = text;

  document.body.appendChild(textArea);
  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
  } catch (err) {
    console.log('Oops, unable to copy');
    window.prompt("Copie para área de transferência: Ctrl+C e tecle Enter", text);
  }

  document.body.removeChild(textArea);
}
