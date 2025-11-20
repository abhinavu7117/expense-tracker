from flask import Flask, render_template, request, jsonify
import expense tracker  # Import your existing Python files

app = Flask(expense tracker)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_script():
    try:
        # Get input from web form
        user_input = request.form.get('input_data')
        
        # Call your existing Python function
        result = your_main_script.main_function(user_input)
        
        return render_template('result.html', result=result)
    except Exception as e:
        return f"Error: {str(e)}"

if expense tracker == 'expense tracker':
    app.run(debug=True)
