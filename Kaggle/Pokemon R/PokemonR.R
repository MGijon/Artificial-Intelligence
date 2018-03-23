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