library(datasets)
library(dplyr)
library(ggplot2)

load(iris)
names(iris) <- tolower(names(iris))

Virginica <- filter(iris, species == "virginica")


###########
## PETAL ##
###########

cor(Virginica$petal.length, Virginica$petal.width) # 0.3221082

# linear regression
regresion <- lm(petal.width ~ petal.length, data = Virginica)
summary(regresion)

# basic plot
plot(x = Virginica$petal.length, y = Virginica$petal.width, xlab = "Petal length", ylab = "Petal width", main = "Virginica petal linear regression")
abline(regresion)

# prediction calculations
new.flowers <- data.frame(petal.length = seq(from = 4.5, to = 6.7, by = .1))
predict(regresion, new.flowers)

# inference from the model
confint(regresion)
confint(regresion, level = .3)

# graphic complete
plot(x = Virginica$petal.length, y = Virginica$petal.width, xlab = "Petal length", ylab = "Petal width", main = "Virginica petal linear regression")
abline(regresion)

  # confidence intervals
ic <- predict(regresion, new.flowers, interval = "confidence")
lines(new.flowers$petal.length, ic[, 2], lty = 2, col = "blue")
lines(new.flowers$petal.length, ic[, 3], lty = 2, col = "blue")

  # prediction intervals
ic <- predict(regresion, new.flowers, interval = "prediction")
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


cor(Virginica$sepal.length, Virginica$sepal.width) # 0.4572278

# linear regression
regresion <- lm(sepal.width ~ sepal.length, data = Virginica)
summary(regresion)

# basic plot
plot(x = Virginica$sepal.length, y = Virginica$sepal.width, xlab = "Sepal length", ylab = "Sepal width", main = "Virginica sepal linear regression")
abline(regresion)

# predictions calculations
new.flowers <- data.frame(sepal.length = seq(from = 5, to = 8, by = .1))
predict(regresion, new.flowers)

# inference from the model
confint(regresion)
confint(regresion, level = .3)

# graphic complete
plot(x = Virginica$sepal.length, y = Virginica$sepal.width, xlab = "Sepal length", ylab = "Sepal width", main = "Virginica sepal linear regression")
abline(regresion)

  # confidence intervals
ic <- predict(regresion, new.flowers, interval = "confidence")
lines(new.flowers$sepal.length, ic[, 2], lty = 2, col = "blue")
lines(new.flowers$sepal.length, ic[, 3], lty = 2, col = "blue")

  # prediction intervals
ic <- predict(regresion, new.flowers, interval = "prediction")
lines(new.flowers$sepal.length, ic[, 2], lty = 2, col = "red")
lines(new.flowers$sepal.length, ic[, 3], lty = 2, col = "red")


## Diagnosis of the model
## ======================

residuos <- rstandard(regresion)
valores.ajustados <- fitted(regresion)
plot(x = valores.ajustados, y = residuos, xlab = "Fitted values", ylab = "Residuals", main = "Standarized resuduals against fitted values")

# normality hypotesis is check by a QQ plot of the residual
qqnorm(residuos)
qqline(residuos)
