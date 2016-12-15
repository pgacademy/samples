

function drawCard(col, row) {
  var card = cards[col + row * 13];
  var no = card["no"];
  var mark = card["mark"];
  context.drawImage(image, no * 32, mark * 64, 32, 64, col * 32, row * 64, 32, 64);
}

function drawDownCard(col, row) {
  context.drawImage(image, 448, 128, 32, 64, col * 32, row * 64, 32, 64);
}


