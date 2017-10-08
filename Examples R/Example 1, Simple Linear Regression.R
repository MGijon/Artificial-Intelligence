# Example 1, Simple Linear Regression
# https://www.uam.es/personal_pdi/ciencias/joser/paginaR/regresion.html

grasas <- read.table("http://www.uam.es/joser.berrendero/datos/EdadPesoGrasas.txt", header = TRUE)
names(grasas)

pairs(grasas)     # vemos que sí hay relación lineal entre las variables edad y grasas

# calculamos la matriz de coeficiente de correlación
cor(grasas)
# edad y grasas = 0.8373534

regresion <- lm(grasas ~ edad, data = grasas) # grasas = variable respueste, edad = variable regresora o independiente
summary(regresion)

plot(grasas$edad, grasas$grasas, xlab = "Edad", ylab = "Grasas")
abline(regresion)    # Recta de mínimos cuadrados


## Cálculo de predicciones

nuevas.edades <- data.frame(edad = seq(30, 50))
predict(regresion, nuevas.edades)

## Inferencia en el modelo de Regresión Simple

confint(regresion)  # obtenemos los intervalos de confianza para los parámetros
# podemos también elegir el intervalo de confianza con esta función
confint(regresion, level = .9)
# los intervalos de confianza para la respuesta media y los intervalos de precicción para la respuesta se pueden obtener con predict

# calculamos los dos tipos de intervalos para el rango de edades entre 20 y 60 años, los de predicción en color rojo

nuevas.edades <- data.frame(edad = seq(20, 60))
# gráfico de dispersión y recta
plot(grasas$edad, grasas$grasas, xlab = "Edad", ylab = "Grasas")
abline(regresion)

# intervalos de confianza para la respuesta media: ic es una matriz con tres columnas:
# la primera la predicción, el resto los extremos de los intervalos
ic <- predict(regresion, nuevas.edades, interval = "confidence")
lines(nuevas.edades$edad, ic[, 2], lty = 2)
lines(nuevas.edades$edad, ic[, 3], lty = 2)

# intervalos de predicción
ic <- predict(regresion, nuevas.edades, interval = "prediction")
lines(nuevas.edades$edad, ic[, 2], lty = 2, col = "red")
lines(nuevas.edades$edad, ic[, 3], lty = 2, col = "red")


## Diagnóstico del modelo

# los valores ajustados y los residuos se pueden obtener con los comandos residuals y fitted, los
# residuos estandarizados se obtienen con rstandard

# aquí una representación de los valores estandarizados frente a los valores ajustados, útil para llevar
# a cabo el diagnóstico del modelo

residuos <- rstandard(regresion)
valores.ajustados <- fitted(regresion)
plot(valores.ajustados, residuos)

# La hipótesis de normalidad se suele comprobar mediante un QQ plot de los residuos
qqnorm(residuos)
qqline(residuos)

