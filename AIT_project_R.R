emission <- read.csv("C:/Users/aliya/OneDrive/Documents/University/AIT/datasets/ghgp_data_2023_LDC_Direct_Emissions.csv",skip = 3)
names(emission) <- make.names(names(emission))

emission2<- emission[, c("State.where.Emissions.Occur",
              "Reported.Latitude",
              "Reported.Longitude",
              "Primary.NAICS.Code",
              "Industry.Type..subparts.",
              "Total.reported.direct.emissions.from.Local.Distribution.Companies")]

emission2<- na.omit(emission2)
names(emission2) <- c("State", "Latitude", "Longitude",
                "NAICS", "Industry", "Total_Emissions")

library(randomForest)
set.seed(1)

fit1 <- randomForest(Total_Emissions ~ State + Latitude + Longitude +
                        NAICS + Industry,
                      data = emission2,
                      ntree = 150,
                      importance = TRUE)
print(fit1)
importance(fit1)
varImpPlot(fit1)
############################################################################################
#Research Question 4

cluster_emdata <- emission[, c(
  "Total.reported.direct.emissions.from.Local.Distribution.Companies",
  "CO2.emissions..non.biogenic.",
  "Methane..CH4..emissions",
  "Nitrous.Oxide..N2O..emissions"
)]

names(cluster_emdata) <- c("Total_Emissions", "CO2", "CH4", "N2O")

cluster_emdata <- na.omit(cluster_emdata)
cluster_scaled <- scale(cluster_emdata)

set.seed(2)
k3 <- kmeans(cluster_scaled, centers = 3, nstart = 20)

k3$centers

plot(cluster_scaled[, "CO2"], cluster_scaled[, "CH4"],
     col = k3$cluster, pch = 16,
     xlab = "CO2 (scaled)",
     ylab = "CH4 (scaled)",
     main = "K-Means Clustering of Facilities by Emission Profile")