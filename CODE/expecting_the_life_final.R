data = read.csv('Life Expectancy Data.csv')
library(car)
library(dplyr)

# Can inspect 2014 first, but we could apply the same procedure to every year
data2014 = filter(data, data$Year == '2014') # len 183
data2014
data2014 = na.omit(data2014) # len 131

data2014 = subset(data2014, select = - c(Country, Adult.Mortality, infant.deaths, under.five.deaths, Income.composition.of.resources))

data2014 = within(data2014,{
  Status = as.factor(Status)
  Status = relevel(Status, ref="Developing")
})

# REINDEX
row.names(data2014) = NULL
data2014 = data2014 %>% mutate(Index = row_number())

res.full = lm(Life.expectancy ~ . , data = data2014)
res.null = lm(Life.expectancy ~ 1, data = data2014)

#start with no predictor in the model
forward1=step(res.null,scope = list(upper=res.full),
              direction="forward",data=data2014)

#start with no predictor in the model
both1=step(res.null,scope = list(upper=res.full),
           direction="both",data=data2014)


res = lm(Life.expectancy ~ Schooling + HIV.AIDS + percentage.expenditure + BMI + Total.expenditure + Status, data=data2014)
summary(res)
vif(res)
par(mfrow=c(2,2))
plot(res)

# REMOVE SIERRA LEONE
data2014FINAL = data2014[-121, ]

res2014 = lm(Life.expectancy ~ Schooling + HIV.AIDS + percentage.expenditure + BMI + Total.expenditure + Status, data=data2014FINAL)
summary(res2014)
vif(res2014)
par(mfrow=c(1,1))
plot(res2014)

#################################
# Predictions on other countries using our model

predictor2014.fx = function(year) {
  year.data = subset(data, data$Year == year)
  
  year.data = na.omit(year.data)
  
  year.data = subset(year.data , select = - c(Country, Adult.Mortality, infant.deaths, under.five.deaths, Income.composition.of.resources))
  
  predictions = predict(res2014, year.data)
  plot(year.data$Life.expectancy, predictions, xlab = "Life Expectancy", ylab="Model Predictions", main=year)
  abline(a = 0, b = 1, col = "red", lty = "dashed", lwd = 2)
  
  return
}

par(mfrow = c(3,5))
years = c("2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014")
for (y in years) {
  predictor2014.fx(y) 
}

####################################

data2000 = filter(data, data$Year == '2000') # len 183
data2000 = na.omit(data2000) # len 131

data2000 = subset(data2000, select = - c(Country, Adult.Mortality, infant.deaths, under.five.deaths, Income.composition.of.resources))

data2000 = within(data2000,{
  Status = as.factor(Status)
  Status = relevel(Status, ref="Developing")
})

# REINDEX
row.names(data2000) = NULL
data2000 = data2000 %>% mutate(Index = row_number())

res.full = lm(Life.expectancy ~ . , data = data2000)
res.null = lm(Life.expectancy ~ 1, data = data2000)

#start with no predictor in the model
forward1=step(res.null,scope = list(upper=res.full),
              direction="forward",data=data2000)

#start with no predictor in the model
both1=step(res.null,scope = list(upper=res.full),
           direction="both",data=data2000)


res2000 = lm(Life.expectancy ~ HIV.AIDS + Schooling + GDP + Diphtheria + thinness.5.9.years + Hepatitis.B + Measles, data=data2000)
summary(res2000)
vif(res2000)
par(mfrow=c(2,2))
plot(res2000)

predictor2000.fx = function(year) {
  year.data = subset(data, data$Year == year)
  
  year.data = na.omit(year.data)
  
  year.data = subset(year.data , select = - c(Country, Adult.Mortality, infant.deaths, under.five.deaths, Income.composition.of.resources))
  
  predictions = predict(res2000, year.data)
  plot(year.data$Life.expectancy, predictions, xlab = "Life Expectancy", ylab="Model Predictions", main=year)
  abline(a = 0, b = 1, col = "red", lty = "dashed", lwd = 2)
  
  return
}

par(mfrow = c(3,5))
years = c("2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014")
for (y in years) {
  predictor2000.fx(y) 
}

