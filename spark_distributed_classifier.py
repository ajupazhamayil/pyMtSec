


from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()


from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
dataset = spark.read.csv('BostonHousing.csv',inferSchema=True, header =True)

dataset.printSchema()

#Input all the features in one vector column
assembler = VectorAssembler(inputCols=['crim', 'zn', 'chas', 'nox', 'age', 'dis', 'rad', 'tax','indus', 'ptratio', 'b', 'lstat'], outputCol = 'Attributes')
output = assembler.transform(dataset)
#Input vs Output
finalized_data1 = output.select("Attributes","crim")
finalized_data2 = output.select("Attributes","zn")
finalized_data3 = output.select("Attributes","indus")
finalized_data4 = output.select("Attributes","chas")
finalized_data5 = output.select("Attributes","nox")
finalized_data6 = output.select("Attributes","rm")
finalized_data7 = output.select("Attributes","age")
finalized_data8 = output.select("Attributes","dis")
finalized_data9 = output.select("Attributes","rad")
finalized_data10 = output.select("Attributes","tax")
finalized_data11 = output.select("Attributes","ptratio")
finalized_data12 = output.select("Attributes","b")
finalized_data13 = output.select("Attributes","lstat")
finalized_data14 = output.select("Attributes","medv")
output.show()

#Split training and testing data
train_data,test_data =finalized_data6.randomSplit([0.8,0.2])
regressor = LinearRegression(featuresCol = 'Attributes', labelCol = 'rm')

#Learn to fit the model from training set
regressor = regressor.fit(train_data)
#To predict the prices on testing set
pred = regressor.evaluate(test_data)
#Predict the model
pred.predictions.show()

#coefficient of the regression model
coeff = regressor.coefficients
#X and Y intercept
intr = regressor.intercept
print ("The coefficient of the model is : %a" %coeff)
print ("The Intercept of the model is : %f" %intr)
from pyspark.ml.evaluation import RegressionEvaluator
eval = RegressionEvaluator(labelCol="rm", predictionCol="prediction", metricName="rmse")

# Mean Square Error
mse = eval.evaluate(pred.predictions, {eval.metricName: "mse"})
print("MSE: %.3f" % mse)

"""
#Split training and testing data
train_data,test_data =finalized_data3.randomSplit([0.8,0.2])
regressor = LinearRegression(featuresCol = 'Attributes', labelCol = 'indus')

#Learn to fit the model from training set
regressor = regressor.fit(train_data)
#To predict the prices on testing set
pred = regressor.evaluate(test_data)
#Predict the model
pred.predictions.show()

#coefficient of the regression model
coeff = regressor.coefficients
#X and Y intercept
intr = regressor.intercept
print ("The coefficient of the model is : %a" %coeff)
print ("The Intercept of the model is : %f" %intr)
from pyspark.ml.evaluation import RegressionEvaluator
eval = RegressionEvaluator(labelCol="indus", predictionCol="prediction", metricName="rmse")

# Mean Square Error
mse = eval.evaluate(pred.predictions, {eval.metricName: "mse"})
print("MSE: %.3f" % mse)

#Split training and testing data
train_data,test_data =finalized_data14.randomSplit([0.8,0.2])
regressor = LinearRegression(featuresCol = 'Attributes', labelCol = 'medv')

#Learn to fit the model from training set
regressor = regressor.fit(train_data)
#To predict the prices on testing set
pred = regressor.evaluate(test_data)
#Predict the model
pred.predictions.show()

#coefficient of the regression model
coeff = regressor.coefficients
#X and Y intercept
intr = regressor.intercept
print ("The coefficient of the model is : %a" %coeff)
print ("The Intercept of the model is : %f" %intr)
from pyspark.ml.evaluation import RegressionEvaluator
eval = RegressionEvaluator(labelCol="medv", predictionCol="prediction", metricName="rmse")

# Mean Square Error
mse = eval.evaluate(pred.predictions, {eval.metricName: "mse"})
print("MSE: %.3f" % mse)

"""