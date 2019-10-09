data(iris)
head(iris)
sapply(iris, class)

install.packages('FactoMineR')
library(FactoMineR)
pc <- PCA(iris, quali.sup = 5)

r1 <- lm(pc$ind$coord[, 1] ~ iris[, 5])
summary(r1)

attributes(pc$quali.sup)

pc$quali.sup$eta2

cor(iris[, 1:4], pc$ind$coord[, 1])

r3 <- lm(pc$ind$coord[, 1] ~ iris[, 1])
summary(r3)

cor(iris[, 1], pc$ind$coord[, 1])

2*sqrt(1/152)

