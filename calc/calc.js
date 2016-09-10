$(function() {

  // exp ::= term | exp + term | exp - term
  // term ::= factor | term * factor | term / factor
  // factor ::= num | (exp)


var regex = /[0-9.]+|[\*\/\+\-]/g;

var expr = "9+456*24.5/4";

var tokens = [];
while ((array = regex.exec(expr)) !== null) {
  tokens.push(array[0]);
}
tokens;





});

