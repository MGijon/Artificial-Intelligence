library(datasets)
library(dplyr)
library(ggplot2)

data(mtcars)

cars <- mtcars

# multivariate linear model:
lm_fit <- lm(mpg ~ cyl + hp, data = cars)
summary(lm_fit)

# prediction:
predicted_df <- data.frame(mpg_pred = predict(lm_fit, cars), hp = cars$hp)

# graphic:
ggplot(data = cars, aes(x = mpg, y = hp)) + 
  geom_point(color = 'blue') + geom_line(color = 'red', data = predicted_df, aes(x = mpg_pred, y = hp))

# predicted line comparing only chosen variables:
ggplot(data = cars, aes(x = mpg, y = hp)) + 
  geom_point(color = 'blue') + 
  geom_smooth(color = 'red', method = 'lm', se = FALSE)