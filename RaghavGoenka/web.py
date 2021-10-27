import requests
from flask import Flask
from urllib.request import urlopen,Request
import urllib.parse,urllib.error
from flask_bootstrap import Bootstrap
from bs4 import BeautifulSoup
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
# from flask_mysqldb import MySQL

app=Flask(__name__)
# mysql=MySQL(app)
app.config['SECRET_KEY']='mysecterkey'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'quote'


class Country(FlaskForm):
	quote=StringField("", validators=[DataRequired()])
	submit=SubmitField("Submit")

@app.route('/test',methods=['GET','POST'])	
	
# def index():
	
def result():
	quote_list=[]
	author_list=[]
	form=Country()
	quote=form.quote.data
	# result(quote)
	

	if(quote!=None):
		rank_page = 'https://www.brainyquote.com/search_results?q='+str(quote)
		print(rank_page)
		request = Request(rank_page, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'})
		page = urlopen(request)
		soup = BeautifulSoup(page, 'html.parser')
		# cur = mysql.connection.cursor()
		
		for tagg in soup.find_all('div',attrs={'class':'clearfix'}):
			for tag1 in tagg.find_all('a',attrs={'title' : 'view quote'}):
				
				quote_list.append(tag1.get_text())
		# 		cur.execute("INSERT INTO data(type, quotes) VALUES (%s, %s)", (str(quote), tag1.get_text()))
		# 		mysql.connection.commit()
		# cur.close()
		print("\n\n")
		print(quote_list)
		
		for tag11 in soup.find_all('a',attrs={'title' : 'view author'}):
				
				author_list.append(tag11.get_text())
			
		
		print(author_list)




	else:
		print("Nothing has been added!!")	
	return render_template('view.html',form=form,quote_list=quote_list,author_list=author_list)	


if __name__ == '__main__':
		app.run(debug=True)	
