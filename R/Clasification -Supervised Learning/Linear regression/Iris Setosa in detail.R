library(datasets)
library(dplyr)
library(ggplot2)

data(iris)
names(iris) <- tolower(names(iris))

Setosa <- filter(iris, species == 'setosa')

###########
## PETAL ##
###########

cor(Setosa$petal.length, Setosa$petal.width) # 0.33163

# linear regression
regresion <- lm(petal.width ~ petal.length, data = Setosa)
summary(regresion)

# basic plot
plot(x = Setosa$petal.length, y = Setosa$petal.width, xlab = "Petal length", ylab = "Petal width", main = "Setosa petal linear regression")
abline(regresion)

# predictions calculations
new.flowers <- data.frame(petal.length = seq(from = 1, to = 1.8, by = .05))
predict(regresion, new.flowers)

# inference from the model
confint(regresion)
confint(regresion, level = .5)

# graphic complete
graphics.off()
plot(x = Setosa$petal.length, y = Setosa$petal.width, xlab = "Petal length", ylab = "Petal width", main = "Setosa petal linear regression")
abline(regresion)


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

graphics.off()
residuos <- rstandard(regresion)
valores.ajustados <- fitted(regresion)
plot(x = valores.ajustados, y = residuos, xlab = "Fitted values", ylab = "Residuals", main = "Standarized resuduals against fitted values")

# normality hypotesis is check by a QQ plot of the residual
qqnorm(residuos)
qqline(residuos)


###########
## SEPAL ##
###########

