from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {users_froyo_toppings}!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_favorite_color = request.args.get('color')
    users_favorite_animal = request.args.get('animal')
    users_favorite_city = request.args.get('city')

    context = {
        'users_favorite_color': users_favorite_color,
        'users_favorite_animal': users_favorite_animal,
        'users_favorite_city': users_favorite_city
    }

    return render_template('froyo_results.html', **context)
    

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter your secret message <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    alphabetical_order = sort_letters(users_secret_message)
    return f'Here\'s your secret message! <br/> {alphabetical_order}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    int_number1 = int(request.args.get('operand1'))
    int_number2 = int(request.args.get('operand2'))
    operator = request.args.get('operation')

    result = 0
    if operator == "add":
        result = int_number1 + int_number2
    elif operator == "subtract":
        result = int_number1 - int_number2
    elif operator == "multiply":
        result = int_number1 * int_number2
    elif operator == "divide":
        result = int_number1 / int_number2

    context = {
        'int_number1': int_number1,
        'int_number2': int_number2,
        'operator': operator,
        'result': result
    }

    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    users_name = request.args.get('users_name')
    wants_compliments = request.args.get('wants_compliments')
    num_compliments = int(request.args.get('num_compliments'))
    list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
    ]
    if wants_compliments == 'no':
        compliment = 'Sorry, you chose no compliments.'
    elif wants_compliments == 'yes':
        compliment = random.sample(list_of_compliments, k=num_compliments)

    context = {
        'users_name': users_name,
        'wants_compliments': wants_compliments,
        'num_compliments': num_compliments,
        'compliment': compliment
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
