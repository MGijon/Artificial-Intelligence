library(MASS)

data(women) # load the data
summary(women) # inspect the data

linear_model <- lm(height ~ weight, data = women) # do a linear model
summary(linear_model) # get the goodness of the model

# simple plot of the data and the model
plot(x = women$weight, y = women$height, xlab = "Weight", ylab = "Height", main = "Women")
abline(linear_model, col = 'red')
