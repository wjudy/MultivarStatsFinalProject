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

res = lm(Life.expectancy ~ Schooling + HIV.AIDS + percentage.expenditure + BMI + Total.expenditure + Status, data=data2014FINAL)
summary(res)
vif(res)
par(mfrow=c(2,2))
plot(res)

#################################
# Predictions on other countries using our model

data2000 = subset(data, data$Year == '2000')

data2000 = na.omit(data2000) # len 131

data2000 = subset(data2014, select = - c(Country, Adult.Mortality, infant.deaths, under.five.deaths, Income.composition.of.resources))

data2000 = within(data2000,{
  Status = as.factor(Status)
  Status = relevel(Status, ref="Developing")
})

predictions = predict(res, data2000)
plot(predictions, data2000$Life.expectancy)
