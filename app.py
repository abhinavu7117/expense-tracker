from flask import Flask, render_template
import expense_tracker  # Import your expense tracker

app = Flask(__name__)

@app.route('/')
def show_output():
    try:
        # Run your expense tracker and get the output
        result = expense tracker.main()  # Adjust based on your main function
        
        # If your function returns text/string
        return f"""
        <html>
            <head>
                <title>Expense Tracker Results</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .result {{ background: #f5f5f5; padding: 20px; border-radius: 5px; }}
                </style>
            </head>
            <body>
                <h1>Expense Tracker Output</h1>
                <div class="result">
                    <pre>{result}</pre>
                </div>
            </body>
        </html>
        """
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
