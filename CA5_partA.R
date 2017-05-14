#sum function
sum <- function(x,y) {
  result <- x+y 
  print(paste(x,"add", y,"is", result))
}
sum(2,3)

#substract function
subtract <- function(x,y) {
  result <- x-y 
  print(paste(x,"minus", y,"is", result))
}
subtract(3,1)

#multiply function
multiply <- function(x,y) {
  result <- x*y 
  print(paste(x,"by", y,"is", result))
}
multiply(3,5)

#divide function
divide <- function(x,y) {
  result <- x/y 
  print(paste(x,"divide by", y,"is", result))
}
divide(30,5)

#exponent function
exponent <- function(x,y) {
  result <- x**y 
  print(paste(x,"to the power", y,"is", result))
}
exponent(2,3)

#square function
square <- function(x) {
  result <- x*x 
  print(paste(x,"square is", result))
}
square(6)

#cube function
cube <- function(x) {
  result <- x*x*x 
  print(paste(x, "cube", "is", result))
}
cube(6)

#celsius to fahrenheit
to_fahrenheit <- function(x) {
  result <- ((9)/5)*x + 32 
  print(paste(x, "celsius", "to fahrenheit", "is", result))
}
to_fahrenheit(40)

#add on function
add <- function(x,y) {
  print(paste(x,"add on", y,"is", x, ",", y))
}
add(3,4)











