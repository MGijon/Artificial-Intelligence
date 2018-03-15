library(ggplot2)
library(dplyr)
library(DT)
library(tidyr)
library(wesanderson)


## Load the data.set
## =================

videogames <- read.csv('/Users/manuelgijonagudo/Documents/Programación/GIT/Machine-Learning/Kaggle/VideoGames R/Data/vgsales.csv', stringsAsFactors = FALSE)

## Data preparation
## ================

summary(videogames)   # explore the data
# We see that the variable year is taken as a character, we have to fix this
videogames$Year = as.numeric(videogames$Year)
summary(videogames)
# Now we see that there are videogames untill 2020, another thing to fix.
# We are gonna have dates until 2016
videogames = videogames[videogames$Year < 2017,]
summary(videogames)

## Visualization
## =============

# plot the sales against the year
plot(videogames$Year, videogames$Global_Sales, main = 'Year - Global_Sales') 
ggplot(videogames, aes(Year, Global_Sales)) + geom_point()
ggplot(videogames, aes(Year, Global_Sales)) + geom_point(aes(colour = factor(Platform)), size = 2)
Year_GS_Plot <- ggplot(videogames, aes(Year, Global_Sales, colour = Platform))  + geom_point() 
print(Year_GS_Plot)
print(Year_GS_Plot + ggtitle("Year against Global Sales"))  # adding title
print(Year_GS_Plot  + labs(y = "Global Sales", x = "Year")) # adding labeled axes

# plot the global sales against the japanese sales
Year_GS_JS <- ggplot(videogames, aes(JP_Sales, Global_Sales, colour = Platform))  + geom_point() 
print(Year_GS_JS)
print(Year_GS_JS + ggtitle("Global Sales against Japanese sales"))  # adding title
print(Year_GS_JS + labs(y = "Global Sales", x = "Japanese Sales")) # adding labeled axes

