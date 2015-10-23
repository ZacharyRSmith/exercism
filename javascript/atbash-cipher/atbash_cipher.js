module.exports = {
  encode: encode
}

function encode(text){
  var formatted = text.replace(/\s|\.|,/g, "").toLowerCase();
  var result = "";
  // var counter = 0;
  formatted.split("").forEach(function(letter, i){
    // counter++;
    var code = letter.charCodeAt();
    result += code > 96 ? String.fromCharCode(97-code+122) : letter;
    if((i+1)%5===0){ result+=" "; }
  })
  return result.trim();
}