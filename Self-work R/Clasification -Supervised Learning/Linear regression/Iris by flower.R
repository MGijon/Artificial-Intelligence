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

regresion <- lm(sepal.width ~ sepal.length, data = Setosa) # sepal.lenght in function of sepal.width
summary(regresion)

plot(Setosa$sepal.length, Setosa$sepal.width, xlab = "Sepal width", ylab = "Sepal length")
abline(regresion)

#regresion$coefficients

#ggplot(Setosa, aes(x = sepal.width, y = sepal.length)) + geom_point()
#+ geom_abline(aes(intercept = 1.4463054, slope = 0.2318905))





  ## PETAL:
  ## ======

cor(Setosa$petal.length, Setosa$petal.width) # 0.3221082


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

