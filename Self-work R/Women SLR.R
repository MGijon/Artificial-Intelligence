data(women)
head(women)

heigh = women$heigh
weight = women$weight

pairs(women)

cor(heigh, weight)             # 0.9954948

plot(heigh, weight, xlab = "Heigh", ylab = "Weight")
title("Data: women")

regresion <- lm(weight ~ heigh, data = women)
summary(regresion)

plot(heigh, weight, xlab = "Heigh", ylab = "Weight", main = "Data: women")
abline(regresion, col = "red")
 
confint(regresion, level = .9)

new.heigh <- data.frame(heigh = seq(58, 72))
class(new.heigh)
head(new.heigh)

plot(heigh, weight, xlab = "Heigh", ylab = "Weight", main = "Data: women")
abline(regresion, col = "red")

ic <- predict(regresion, new.heigh, interval = "confidence")
lines(new.heigh$heigh, ic[, 2], lty = 2, col = "blue")
lines(new.heigh$heigh, ic[, 3], lty = 2, col = "blue")

ic <- predict(regresion, new.heigh, interval = "prediction")
lines(new.heigh$heigh, ic[, 2], lty = 2, col = "green")
lines(new.heigh$heigh, ic[, 3], lty = 2, col = "green")

legend("right", legend = c("Regression Line", "Confidence interval", "Prediction interval"), col = c("red", "blue", "green"), lty = 1:2, cex = .8)

