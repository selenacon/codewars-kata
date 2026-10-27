def multiTable(n: Int): String = {
  var resultado: String = ""
  for
      multiplo <- 1 to 10
  do
     resultado = resultado + multiplo + " * " + n + " = " + multiplo * n
     if (multiplo != 10) {
       resultado = resultado + "\n"
     }
  return resultado
}

