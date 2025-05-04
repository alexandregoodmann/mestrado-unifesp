import pandas

df = pandas.read_csv('linguagemprogramacao/Aula5_Pandas/sport-activity.csv')
# pandas.options.display.max_rows = 1000
print(df.head())
print(df.info())
print(df.describe())