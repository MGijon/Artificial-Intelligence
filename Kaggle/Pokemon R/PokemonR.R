library(ggplot2)
library(dplyr)
library(DT)
library(tidyr)
library(wesanderson)

## Load the data.sets
## ==================

pokemon <- read.csv('Data/pokemon.csv', stringsAsFactors = FALSE)
train <- read.csv('Data/tests.csv', stringsAsFactors = FALSE)
combats <- read.csv('Data/combats.csv', stringsAsFactors = FALSE)

## Data exploration
## ================

  # pokemon
summary(pokemon)
head(pokemon, 3)

  # train samples
summary(train)  
head(train)

  # combats
summary(combats)  
head(combats)
  
  # list of diffent types of pokemon
Type <- levels(factor(pokemon$Type.1))
Type

  # Descriptive analysis of some of the variables

    # HP
length(pokemon$HP) 
summary(pokemon$HP)
table(pokemon$HP)     # too much information, not very useull
range(pokemon$HP)
var(pokemon$HP)
sd(pokemon$HP)
quantile(pokemon$HP, 0.25) # first quantile
quantile(pokemon$HP, 0.75) # third quantile
IQR(pokemon$HP) # the interquartile range

  # Attack
summary(pokemon$Attack)
range(pokemon$Attack)
var(pokemon$Attack)
sd(pokemon$Attack)
quantile(pokemon$Attack, 0.25)
quantile(pokemon$Attack, 0.75)
IQR(pokemon$Attack)


###############################################
  # means of different quantities by first type 
tapply(pokemon$HP, pokemon$Type.1, mean)
tapply(pokemon$Attack, pokemon$Type.1, mean)
tapply(pokemon$Sp..Atk, pokemon$Type.1, mean)
tapply(pokemon$Defense, pokemon$Type.1, mean)
tapply(pokemon$Sp..Def, pokemon$Type.1, mean)
tapply(pokemon$Speed, pokemon$Type.1, mean)

 # means of difernet quantities by seconf type
    # obs: there are pokemons with no second type
tapply(pokemon$HP, pokemon$Type.2, mean)
tapply(pokemon$Attack, pokemon$Type.2, mean)
tapply(pokemon$Sp..Atk, pokemon$Type.2, mean)
tapply(pokemon$Defense, pokemon$Type.2, mean)
tapply(pokemon$Sp..Def, pokemon$Type.2, mean)
tapply(pokemon$Speed, pokemon$Type.2, mean)
  
  # it would by very interesting to have both variables as one in order to see 
  # how this properties distributed
pokemon$Types <- as.character(paste(pokemon$Type.1, pokemon$Type.2, sep = '-'))

Types <- levels(factor(pokemon$Types))
Types

  # now represent the best combination of types for each one of the combinations     <- NO ACABADO
aux <- tapply(pokemon$HP, pokemon$Types, mean)
aux[2]
aux <- as.data.frame(aux)
colnames(aux)
which(aux$aux == max(aux$aux))



tapply(pokemon$Attack, pokemon$Types, mean)
tapply(pokemon$Sp..Atk, pokemon$Types, mean)
tapply(pokemon$Defense, pokemon$Types, mean)
tapply(pokemon$Sp..Def, pokemon$Types, mean)
tapply(pokemon$Speed, pokemon$Types, mean)

  # now represent the worst combination of types for each one of the combinations
tapply(pokemon$HP, pokemon$Types, mean)
tapply(pokemon$Attack, pokemon$Types, mean)
tapply(pokemon$Sp..Atk, pokemon$Types, mean)
tapply(pokemon$Defense, pokemon$Types, mean)
tapply(pokemon$Sp..Def, pokemon$Types, mean)
tapply(pokemon$Speed, pokemon$Types, mean)

######################################
  # Graphics of some atributes by type
ggplot(pokemon, aes(x = Type.1, y = HP)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Attack)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Sp..Atk)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Defense)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Sp..Def)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Speed)) + geom_boxplot()

  # Differences between legendary and regular pokemon by type
ggplot(pokemon, aes(x = Type.1, y = HP, fill = Legendary)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Attack, fill = Legendary)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Sp..Atk, fill = Legendary)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Defense, fill = Legendary)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Sp..Def, fill = Legendary)) + geom_boxplot()
ggplot(pokemon, aes(x = Type.1, y = Speed, fill = Legendary)) + geom_boxplot() 

