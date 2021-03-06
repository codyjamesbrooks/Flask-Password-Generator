from flask import Flask, render_template, request
from make_pass import password_generator

# Setup app
app = Flask(__name__)

# Setup index route


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        # Get form inputs. These will tell us what elements to include in the password
        password_length = int(request.form['length'])
        contain_numbers = request.form.get('numbers') == 'on'
        contain_specialchar = request.form.get('specialchar') == 'on'
        contain_uppercase = request.form.get('uppercase') == 'on'

        # pass inputs to password generator function
        password = password_generator(
            password_length, contain_numbers, contain_specialchar, contain_uppercase)

        # rerender template with the generated password included.
        return render_template('home.html', password=password)

    else:

        # Default template, form waiting for input
        return render_template('home.html')


# Spin up the app.
if __name__ == "__main__":
    app.run(debug=True)
