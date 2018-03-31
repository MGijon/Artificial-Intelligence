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




























###########
## SEPAL ##
###########