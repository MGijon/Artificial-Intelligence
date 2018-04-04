library(rpart)

data(iris)
names(iris) <- tolower(names(iris))

###########
## SEPAL ##
###########

tree <- rpart(species ~ sepal.length + sepal.width, data = iris)

printcp(tree)   # display the results 
plotcp(tree)    # visualize cross-validation results 
summary(tree)   # detailed summary of splits

# plot tree 
plot(tree, uniform = TRUE, 
     main = "Classification Tree for iris based on sepal measures")
text(tree, use.n = TRUE, all = TRUE, cex = .8)

  # create postscript plot of tree 
post(tree, file = "c:/tree.ps", 
     title = "Classification Tree for iris based on sepal measures")

# prune the tree 
p_tree <- prune(tree, cp = tree$cptable[which.min(tree$cptable[,"xerror"]),"CP"])

# plot the pruned tree 
plot(p_tree, uniform = TRUE, 
     main = "Pruned Classification Tree for iris based on sepal measures")
text(p_tree, use.n = TRUE, all = TRUE, cex = .8)

  # create postscript plot of tree 
post(p_tree, file = "c:/ptree.ps", 
     title = "Pruned Classification Tree for iris based on sepal measures")


###########
## PETAL ##
###########

tree <- rpart(species ~ petal.length + petal.width, data = iris)

printcp(tree)   # display the results 
plotcp(tree)    # visualize cross-validation results 
summary(tree)   # detailed summary of splits

# plot tree 
plot(tree, uniform = TRUE, 
     main = "Classification Tree for iris based on petal measures")
text(tree, use.n = TRUE, all = TRUE, cex = .8)

# create postscript plot of tree 
post(tree, file = "c:/tree.ps", 
     title = "Classification Tree for iris based on petal measures")

# prune the tree 
p_tree <- prune(tree, cp = tree$cptable[which.min(tree$cptable[,"xerror"]),"CP"])

# plot the pruned tree 
plot(p_tree, uniform = TRUE, 
     main = "Pruned Classification Tree for iris based on petal measures")
text(p_tree, use.n = TRUE, all = TRUE, cex = .8)

# create postscript plot of tree 
post(p_tree, file = "c:/ptree.ps", 
     title = "Pruned Classification Tree for iris based on petal measures")


###################
## SEPAL & PETAL ##
###################

tree <- rpart(species ~ sepal.length + sepal.width + petal.length + petal.width, data = iris)

printcp(tree)   # display the results 
plotcp(tree)    # visualize cross-validation results 
summary(tree)   # detailed summary of splits

# plot tree 
plot(tree, uniform = TRUE, 
     main = "Classification Tree for iris based on petal and sepal measures")
text(tree, use.n = TRUE, all = TRUE, cex = .8)

# create postscript plot of tree 
post(tree, file = "c:/tree.ps", 
     title = "Classification Tree for iris based on petal and sepal measures")

# prune the tree 
p_tree <- prune(tree, cp = tree$cptable[which.min(tree$cptable[,"xerror"]),"CP"])

# plot the pruned tree 
plot(p_tree, uniform = TRUE, 
     main = "Pruned Classification Tree for iris based on petal and sepal measures")
text(p_tree, use.n = TRUE, all = TRUE, cex = .8)

# create postscript plot of tree 
post(p_tree, file = "c:/ptree.ps", 
     title = "Pruned Classification Tree for iris based on petal and sepal measures")

# https://www.statmethods.net/advstats/cart.html