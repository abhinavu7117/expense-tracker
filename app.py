from flask import Flask, render_template
import expense_tracker
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/output')
def show_output():
    try:
        # Run your expense tracker
        result = expense_tracker.main()  # Adjust function name as needed
        
        return render_template('output.html', 
                             result=result,
                             last_updated=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        return render_template('output.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
