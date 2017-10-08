data("iris")
iris
pairs(iris)

# parece haber una relación lineal entre las variables Petal.Lenth y Pedal.Width

head(iris)
summary(iris)

Lenght <- iris$Petal.Length
Width <- iris$Petal.Width

Lenght_setosa <- Lenght[1:50]
Width_setosa <-  Width[1:50]

Lenght_versicolor <- Lenght[51:100]
Width_versicolor <- Width[51:100]

Lenght_virginica <- Lenght[101:150]
Width_virginica <- Width[101:150]

cor(Lenght_setosa, Width_setosa)           # 0.33163
cor(Lenght_versicolor, Width_versicolor)   # 0.7866681
cor(Lenght_virginica, Width_virginica)     # 0.3221082

# Haré el ajuste con los datos correspondientes a la flor versicolor

plot(Lenght_versicolor, Width_versicolor, xlab = "Longitud pétalos", ylab = "Anchura pétalos", type = "p", col = "black")
title("Versicolor", sub = "Relación entre los tamaños de los pétalos", col.main = "cadetblue", font.main = 4, cex.main = 3, col.sub = "grey") 

regresion <- lm(Width_versicolor ~ Lenght_versicolor)
summary(regresion)

plot(Lenght_versicolor, Width_versicolor, xlab = "Longitud pétalos", ylab = "Anchura pétalos", type = "p", col = "black", main = "Pétalos Versicolor")
abline(regresion, col = "red")

nuevas.longitudes = data.frame(Lenght_versicolor, seq = 3, 5)

plot(Lenght_versicolor, Width_versicolor, xlab = "Longitud pétalos", ylab = "Anchura pétalos", type = "p", col = "black", main = "Pétalos Versicolor")
abline(regresion, col = "red")

ic <- predict(regresion, nuevas.longitudes, interval = "confidence")
lines(nuevas.longitudes$Lenght_versicolor, ic[, 2], lty = 2, col = "blue")
lines(nuevas.longitudes$Lenght_versicolor, ic[, 3], lty = 2, col = "blue")

ic <- predict(regresion, nuevas.longitudes, interval = "predict")
lines(nuevas.longitudes$Lenght_versicolor, ic[, 2], lty = 2, col = "green")
lines(nuevas.longitudes$Lenght_versicolor, ic[, 3], lty = 2, col = "green")

legend("topleft", legend = c("Recta regresión lineal", "Intervalo de confianza", "Intervalo de predicción"), col = c("red", "blue", "green"), lty = 1:2, cex = .8)
