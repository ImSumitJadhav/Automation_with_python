import camelot

tables = camelot.read_pdf('try.pdf', pages='2', flavor='lattice')
print(tables)

tables.export('try.csv', f='csv', compress=True)
tables[0].to_csv('try.csv')  # to a csv file
print(tables[0].df)  # to a df


#1.download ghostscript from https://ghostscript.com/releases/gsdnld.html
#2.create path in environmental variable
#3.restrt PC
#4.create virtual environment in project folder
#5.pip install tk
#6.pip install goshtscript
#7.pip install camelot-py
#8.Run code
#9.get csv 