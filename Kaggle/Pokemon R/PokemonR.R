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