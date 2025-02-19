
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Correct homepage route
@app.route('/')
def home():
    return render_template("index.html")  # Flask serves index.html when visiting "/"

# Dynamic route for other pages
@app.route('/<page_name>')
def html_page(page_name):
    valid_pages = ["about", "work", "works", "contact", "thankyou", "components"]
    
    if page_name in valid_pages:
        return render_template(f"{page_name}.html")
    else:
        return "Page not found", 404  # Return 404 for invalid pages

@app.route('/works')
def works():
    return render_template("works.html") 
  # Define the route explicitly
@app.route('/work.html')
def work():
    return render_template("work.html")

      # Handle form submissions

def writ_toME(data):
    with open('Smalldata.csv',mode='a',newline='') as database:
        Email=data['email']
        subj=data['subject']
        message=data['message']
        file=csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([Email,subj,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
      if request.method == 'POST':
        data = request.form.to_dict()
        writ_toME(data)
        return redirect('/thankyou')  # Use /thankyou instead of /thankyou.html
    except:
     return'do not save anything'
    else:
        return 'Something went wrong, try again.'
if __name__ == "__main__":
    app.run(debug=True)