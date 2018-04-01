library(datasets)
library(dplyr)
library(ggplot2)

data(iris)
names(iris) <- tolower(names(iris))

Versicolor <- filter(iris, species == "versicolor")

###########
## PETAL ##
###########

cor(Versicolor$petal.length, Versicolor$petal.width) # 0.7866681

# linear regression
regresion <- lm(petal.width ~ petal.length, data = Versicolor) 
summary(regresion)

# basic plot
plot(x = Versicolor$petal.length, y = Versicolor$petal.width, xlab = "Petal lenght", ylab = "Petal width", main = "Versicolor petal linear regression")
abline(regresion)

# predictions calculations
new.flowers <- data.frame(petal.length = seq(from = 3, to = 5, by = .25))
predict(regresion, new.flowers)

# inference from the model
confint(regresion) # confidence intervals
confint(regresion,level = .5) # confidence interval choosing it

# graphic complete
plot(x = Versicolor$petal.length, y = Versicolor$petal.width, xlab = "Petal length", ylab = "Petal width", main = "Versicolor petal linear regression")
abline(regresion, col = 'red')
  
  # confidence intervals
ic <- predict(regresion, new.flowers, interval = "confidence")
lines(new.flowers$petal.length, ic[, 2], lty = 2, col = "blue")
lines(new.flowers$petal.length, ic[, 3], lty = 2, col = "blue")

  # prediction intervals
ic <- predict(regresion, nuevas.edades, interval = "prediction")
lines(new.flowers$petal.length, ic[, 2], lty = 2, col = "red")
lines(new.flowers$petal.length, ic[, 3], lty = 2, col = "red")


## Diagnosis of the model
## ======================


residuos <- rstandard(regresion)
valores.ajustados <- fitted(regresion)
plot(x = valores.ajustados, y = residuos, xlab = "Fitted values", ylab = "Residuals", main = "Standarized resuduals against fitted values")

# normality hypotesis is check by a QQ plot of the residual
qqnorm(residuos)
qqline(residuos)


###########
## SEPAL ##
###########

cor(Versicolor$sepal.length, Versicolor$sepal.width) # 0.5259107

# linear regression
regresion <- lm(sepal.width ~ sepal.length, data = Versicolor)
summary(regresion)

# basic plot 
plot(x = Versicolor$sepal.length, y = Versicolor$sepal.width, xlab = "Sepal length", ylab = "Sepal width", main = "Versicolor sepal linear regression")
abline(regresion)

# predictions calculation
new.flowers <- data.frame(sepal.length = seq(from = 4.5, to = 7, by = .25))
predict(regresion, new.flowers)

# inference from the model
confint(regresion) # confidence intervals
confint(regresion,level = .5) # confidence interval choosing it

# graphic complete
plot(x = Versicolor$sepal.length, y = Versicolor$sepal.width, xlab = "Sepal length", ylab = "Sepal width", main = "Versicolor sepal linear regression")
abline(regresion, col = 'red')


  # confidence intervals
ic <- predict(regresion, new.flowers, interval = "confidence")
lines(new.flowers$sepal.length, ic[, 2], lty = 2, col = "blue")
lines(new.flowers$sepal.length, ic[, 3], lty = 2, col = "blue")

  # prediction intervals
ic <- predict(regresion, nuevas.edades, interval = "prediction")
lines(new.flowers$sepal.length, ic[, 2], lty = 2, col = "red")
lines(new.flowers$sepal.length, ic[, 3], lty = 2, col = "red")

## Diagnosis of the model
## ======================

graphics.off()
residuos <- rstandard(regresion)
valores.ajustados <- fitted(regresion)
plot(x = valores.ajustados, y = residuos, xlab = "Fitted values", ylab = "Residuals", main = "Standarized resuduals against fitted values")

# normality hypotesis is check by a QQ plot of the residual
qqnorm(residuos)
qqline(residuos)

