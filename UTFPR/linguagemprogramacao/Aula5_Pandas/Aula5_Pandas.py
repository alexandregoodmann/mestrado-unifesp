import pandas

dados = {
'cliente': ["Jonas", "Kim", "Lucas"],
'idade': [15, 39, 68]
}

df = pandas.DataFrame(dados, index=["Jonas", "pessoa2", "pessoa3"])
print(df.loc["Jonas"])
