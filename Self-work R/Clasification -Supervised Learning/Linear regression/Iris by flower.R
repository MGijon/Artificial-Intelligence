library(datasets)
library(dplyr)
library(ggplot2)

data(iris)
summary(iris)
names(iris) <- tolower(names(iris))

Setosa <- filter(iris, species == "setosa")
Virginica <- filter(iris, species == "virginica")
Versicolor <- filter(iris, species == "versicolor")


############
## SETOSA ##
############

pairs(Setosa) # looking for a linear relation

  ## SEPAL:
  ## ======

cor(Setosa$sepal.width, Setosa$sepal.length) # 0.4572278

ggplot(Setosa, aes(x = sepal.width, y = sepal.length)) + geom_point()

regresion <- lm(sepal.width ~ sepal.length, data = Setosa) # sepal.width in function of sepal.length
summary(regresion)

plot(x = Setosa$sepal.length, y = Setosa$sepal.width, xlab = "Sepal length", ylab = "Sepal width")
abline(regresion)

#regresion$coefficients

#ggplot(Setosa, aes(x = sepal.width, y = sepal.length)) + geom_point()
#+ geom_abline(aes(intercept = 1.4463054, slope = 0.2318905))


  ## PETAL:
  ## ======

cor(Setosa$petal.width, Setosa$petal.length) # 0.3221082

regresion <- lm(petal.width ~ petal.length, data = Setosa)   # width in function of lenght
summary(regresion)

plot(x = Setosa$petal.length, y = Setosa$petal.width, xlab = "Petal length", ylab = "Petal width")
abline(regresion)


###############
## VIRGINICA ##
###############


  ## SEPAL:
  ## ======

  ## PETAL:
  ## ======


################
## VERSICOLOR ##
################


  ## SEPAL:
  ## ======

  
  ## PETAL:
  ## ======

