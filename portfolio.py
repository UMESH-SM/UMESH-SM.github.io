from flask import Flask, render_template, request
import csv, passchecker, news

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/topnews.html')
def news_page():
    return news.req_news_data()

@app.route('/topnews.html/news_search', methods=['POST', 'GET'])
def news_search():
    if request.method == 'POST':
        search_input = request.form['search_input']
    return news.req_news_search(search_input)

@app.route('/<string:page_name>')
def other_pages(page_name):
    return render_template(page_name)

@app.route('/passwordchecker.html/passcheck', methods=['POST', 'GET'])
def pass_check():
    if request.method == 'POST':
        password = request.form['password']
    count = passchecker.pass_input(password)
    if count:
        return render_template("passwordchecker.html", msg1 = f'The Password has been hacked {count} times!')
    else:
        return render_template("passwordchecker.html", msg2 = 'The Password is Safe to Use.') 

@app.route('/index.html/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        name, email, subject, message = request.form['name'], request.form['email'], request.form['subject'], request.form['message']
    with open('database.csv', mode='a', newline='') as db:
        writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([name,email,subject,message])
    return render_template('index.html', msg = 'Form Submitted Successfully.') 

        