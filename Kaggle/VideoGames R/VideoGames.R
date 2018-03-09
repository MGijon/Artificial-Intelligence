library(ggplot2)
library(dplyr)
library(DT)
library(tidyr)
library(wesanderson)


# Load the data.set
videogames <- read.csv('/Users/manuelgijonagudo/Documents/Programación/GIT/Machine-Learning/Kaggle/VideoGames R/Data/vgsales.csv', stringsAsFactors = FALSE)

summary(videogames)
#str(videogames)
#head(videogames)

videogames$Year = as.numeric(videogames$Year)

# plot the sales against the year
plot(videogames$Year, videogames$Global_Sales, main = 'Year - Global_Sales')


