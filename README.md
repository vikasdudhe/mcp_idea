# VikasMock - Mock Interview Platform

A Flask-based web application for practicing coding interviews with multiple-choice questions (MCQs) and Python coding challenges.

## Features

- 10 Python-focused MCQ questions covering fundamental concepts
- 2 coding challenges with example inputs/outputs
- Real-time MCQ scoring
- Clean, responsive interface using Bootstrap
- Mock coding environment for Python practice

## Technologies Used

- Python 3.x
- Flask 3.0.0
- Bootstrap 5.1.3
- HTML/CSS/JavaScript

## Project Structure

```
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── static/              # Static files
│   └── style.css        # Custom CSS styles
└── templates/           # HTML templates
    ├── base.html        # Base template with common layout
    ├── index.html       # Home page
    ├── mcq.html         # MCQ questions page
    └── coding.html      # Coding challenges page
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/VikasMock.git
cd VikasMock
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://127.0.0.1:5000`

## MCQ Questions

The application includes 10 carefully selected multiple-choice questions covering Python concepts such as:
- Data types
- Variable naming conventions
- Built-in functions
- List operations
- String operations
- Type checking
- Python syntax
- Basic operators
- Data structures
- Boolean operations

## Coding Challenges

Two coding challenges are included:
1. Two Sum - Find indices of numbers that add up to a target
2. Reverse String - Implement string reversal without built-in functions

## Development

This is a development version. For production deployment:
- Use a production WSGI server
- Implement proper code execution sandboxing
- Add user authentication
- Add more questions and features

## Contributing

Feel free to contribute by:
- Adding more questions
- Implementing code execution
- Improving the UI
- Adding new features

## License

MIT License - feel free to use and modify the code as needed.