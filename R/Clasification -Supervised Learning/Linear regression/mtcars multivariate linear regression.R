library(datasets)
library(dplyr)
library(ggplot2)

data(mtcars)

cars <- mtcars

# multivariate linear model:
lm_fit <- lm(mpg ~ cyl + hp, data = cars)
summary(lm_fit)

# create a data frame with the prediction for the values in THE ORIGINAL DATA FRAME (THE TRAIN DATA, WHICH IS NOT GOOD)!! and the values of hp:
predicted_df <- data.frame(mpg_pred = predict(lm_fit, cars), hp = cars$hp)

# graphic:
ggplot(data = cars, aes(x = mpg, y = hp)) + 
  geom_point(color = 'blue') + geom_line(color = 'red', data = predicted_df, aes(x = mpg_pred, y = hp))

# predicted line comparing only chosen variables:
ggplot(data = cars, aes(x = mpg, y = hp)) + 
  geom_point(color = 'blue') + 
  geom_smooth(color = 'red', method = 'lm', se = FALSE)

# create false data as TEST data       WORKING ON THIS SHIT

seq_mpg <- seq(from = range(cars$mpg)[1], to = range(cars$mpg)[2], by = .1)
num_datos <- length(seq_mpg)
test_data <- data.frame(mpg = seq_mpg, 
                        cyl = rep(mean(cars$cyl), num_datos),
                        hp = rep(mean(cars$hp), num_datos)) # puedo optar por repetir la media de los valores, a ver que pasa
good_predicted <- data.frame(mpg_pred = predict(lm_fit, test_data), hp = cars$hp)

