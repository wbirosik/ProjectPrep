import os
from pyspark.sql import SQLContext
from pyspark import SparkContext



sc = SparkContext(appName="TestPySparkJDBC")
sqlContext = SQLContext(sc)

source_df = sqlContext.read.format('jdbc').options(
         url='jdbc:mysql://localhost/Car_Accidents',
         driver='com.mysql.jdbc.Driver',
         dbtable='NY',
         user='Bill',
         password='Bill').load()
df = sqlContext.sql("SELECT * FROM NY")
df.show()















#import os
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /home/consultant/mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar pyspark-shell'
#sc = SparkContext(appName="TestPySparkJDBC")
#sqlConext = SQLContext(sc)

#hostname = "localhost"
#dbname= "Car_Accidents"
#jdbcPort = "3306"
#username = "Bill"
#password = "Bill"
#jdbc_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}"\
 #  .format(hostname,jdbcPort, dbname,username,password)
#query = "(select BOROUGH FROM NY LIMIT 20) t1_alias"
#df1 = sqlConext.read.format('jdbc')\
 #  .options(driver = 'com.mysql.jdbc.Driver',url=jdbc_url, dbtable=query).load()
#df1.show()


