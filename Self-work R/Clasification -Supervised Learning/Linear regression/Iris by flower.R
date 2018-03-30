library(datasets)
library(dplyr)

data(iris)
summary(iris)
names(iris) <- tolower(names(iris))

Setosa <- filter(iris, species == "setosa")
Virginica <- filter(iris, species == "virginica")
Versicolor <- filter(iris, species == "versicolor")
