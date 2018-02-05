library(ggplot2)
library(dplyr)
library(DT)
library(tidyr)
library(wesanderson)


# Load the data.set
videogames <- read.csv('Data/vgsales.csv', stringsAsFactors = FALSE)

summary(videogames)
str(videogames)
head(videogames)


# plot the sales against the year
plot(videogames$Year, videogames$Global_Sales, main = 'Year - Global_Sales')


