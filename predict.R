load(file = "./Model.RData")

library(xgboost)
args <- commandArgs(trailingOnly=F)
k <- which(args=="--args") + 1

K <- as.integer((args[k]))

inp <- churn_data_mdb[K:(K+1),]
out <- predict(object=trained_model$model, inp)[1]

print(paste("Predicted Probability of Churn", round(out,2)))


