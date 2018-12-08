library(datasets)

cars <- mtcars
columnas <- names(cars)

ajuste_lineal1 <- lm(mpg ~ wt, data = cars)
summary(ajuste_lineal1)

# ahroa de lo que se trata es de calcular bla bla bla bal
