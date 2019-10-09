#install.packages('emmeans')
library(emmeans)
library(tables)

setwd("~/Documents/Programación/Machine-Learning/Self-work R/Clasification -Supervised Learning/ANOVA")

pate <- read.csv('Data/PATE.csv')

## sumas de tipo 1 SS1: dependen del orden


alineamiento por parejas (global o local ) o múltiple
primero vale el valor de a y los siguientes gaps suman el valor de b cada uno