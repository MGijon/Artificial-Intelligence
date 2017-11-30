# source : https://www.kaggle.com/mrisdal/exploring-survival-on-the-titanic

# load the librarys
library('ggplot2') # visualization
library('ggthemes') # visualization
library('scales') # visualization
library('dplyr') # data manipulation
library('mice') # imputation
library('randomForest') # classification algorithm

# load the data
train <- read.csv('train.csv', stringsAsFactors = FALSE)
test <- read.csv('test.csv', stringsAsFactors = FALSE)
full_model <- bind_rows(train, test)

# check the data
str(full_model)
summary(full_model)

## Feature Engineering
## ===================

# seeing the aprox. variable structure
print(full_model$Name[1:5])

# grab the title from the names
full_model$Title <- gsub('(.*, )|(\\..*)', '', full_model$Name)

# show title cpunts by sex
table(full_model$Sex, full_model$Title)

# title with every low cell counts to be combined to "rare" level
rare_title <- c('Dona', 'Lady', 'the Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer')

# reasign some og them
full_model$Title[full_model$Title == 'Mlle'] <- 'Miss'
full_model$Title[full_model$Title == 'Ms'] <- 'Miss'
full_model$Title[full_model$Title == 'Mme'] <-'Mrs'
full_model$Title[full_model$Title %in% rare_title] <- 'Rare Title'

# show the table again
table(full_model$Sex, full_model$Title)

# grab the surname from the passanger name
full_model$Surname <- sapply(full_model$Name, function(x) strsplit(x, split = '[,.]')[[1]][1])

cat(paste('We have ', nlevels(factor(full_model$Surname)), ' unique surnames.'))


## Do we families sink or swiim together?
## ======================================

# Create a family size variable including the passenger themselves
full_model$Fsize <- full_model$SibSp + full_model$Parch + 1

# crate a family variable
full_model$Family <- paste(full_model$Surname, full_model$Fsize, sep = '_')

str(full_model)

# use ggplot2 to visualize tge relationship between family size and survivval
ggplot(full_model[1, 891,], aes(x = Fsize, fill = factor(Survived))) + 
  geom_bar(stat = 'count', position = 'dodge') +
  scale_x_continuous(breaks = c(1:11)) +
  labs(x = 'Family Size') 


