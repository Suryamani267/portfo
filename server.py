from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<page_name>")
def about(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("data.txt", mode = 'a') as data1:
        for key in data.keys():
            data1.write(f'{key} = {data[key]}\n')
        data1.write('\n')

def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open("database.csv", mode = 'a', newline = '') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit.html', methods=['POST'])
def submit_form():
    data = request.form.to_dict()
    write_to_csv(data)
    #error = None
    #if request.method == 'POST':
    #    if valid_login(request.form['username'],
    #                   request.form['password']):
    #        return log_the_user_in(request.form['username'])
    #    else:
    #        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return redirect('submit.html')







