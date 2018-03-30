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
graphics.off()

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
graphics.off()

###############
## VIRGINICA ##
###############


  ## SEPAL:
  ## ======

cor(Virginica$sepal.length, Virginica$sepal.width)  # 0.4572278

regresion <- lm(sepal.width ~ sepal.length, data = Virginica)
summary(regresion)

plot(x = Virginica$sepal.length, y = Virginica$sepal.width, xlab = "Sepal length", ylab = "Sepal width") 
abline(regresion)
graphics.off()

  ## PETAL:
  ## ======

cor(Virginica$sepal.length, Virginica$sepal.width)   # 0.4572278

regresion <- lm(petal.width ~ petal.length, data = Virginica)
summary(regresion)

plot(x = Virginica$petal.length, y = Virginica$petal.width, xlab = "Petal lenght", ylab = "Petal width")
abline(regresion)
graphics.off()


################
## VERSICOLOR ##
################


  ## SEPAL:
  ## ======

cor(Versicolor$sepal.length, Versicolor$sepal.width) # 0.5259107

regresion <- lm(sepal.width ~ sepal.length, data = Versicolor) 
summary(regresion)

plot(x = Virginica$sepal.length, y = Virginica$sepal.width, xlab = "Sepal length", ylab = "Sepal width")
abline(regresion)
graphics.off()

  ## PETAL:
  ## ======

cor(Versicolor$petal.length, Versicolor$petal.width) # 0.7866681

regresion <- lm(petal.width ~ petal.length, data = Versicolor)
summary(regresion)

plot(x = Versicolor$petal.length, y = Versicolor$petal.width, xlab = "Petal length", ylab = "Petal widht")
abline(regresion)
graphics.off()
