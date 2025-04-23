from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Mock questions data
mcq_questions = [
    {
        "id": 1,
        "question": "What is the output of print(type(1/2)) in Python 3?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'number'>"],
        "correct_answer": "<class 'float'>"
    },
    {
        "id": 2,
        "question": "Which of the following is not a valid variable name in Python?",
        "options": ["my_var", "_variable", "2variable", "variable2"],
        "correct_answer": "2variable"
    },
    {
        "id": 3,
        "question": "What is the output of print(list(range(3)))?",
        "options": ["[0, 1, 2]", "[1, 2, 3]", "[0, 1, 2, 3]", "[1, 2]"],
        "correct_answer": "[0, 1, 2]"
    },
    {
        "id": 4,
        "question": "Which method is used to remove the last element from a list?",
        "options": ["remove()", "pop()", "del()", "discard()"],
        "correct_answer": "pop()"
    },
    {
        "id": 5,
        "question": "What is the result of 3 * '7'?",
        "options": ["21", "777", "37", "Error"],
        "correct_answer": "777"
    },
    {
        "id": 6,
        "question": "Which of these is not a Python built-in data type?",
        "options": ["list", "tuple", "array", "dictionary"],
        "correct_answer": "array"
    },
    {
        "id": 7,
        "question": "What is the correct way to create an empty set in Python?",
        "options": ["set()", "{}", "[]", "()"],
        "correct_answer": "set()"
    },
    {
        "id": 8,
        "question": "What does the 'is' operator check for?",
        "options": ["Value equality", "Type equality", "Identity/Memory location", "Reference equality"],
        "correct_answer": "Identity/Memory location"
    },
    {
        "id": 9,
        "question": "Which of these is not a valid way to comment in Python?",
        "options": ["# comment", "''' comment '''", "// comment", "\"\"\" comment \"\"\""],
        "correct_answer": "// comment"
    },
    {
        "id": 10,
        "question": "What is the output of print(bool([]))?",
        "options": ["True", "False", "None", "Error"],
        "correct_answer": "False"
    }
]

coding_questions = [
    {
        "id": 1,
        "title": "Two Sum",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers that add up to target.",
        "example_input": "nums = [2,7,11,15], target = 9",
        "example_output": "[0,1] # Because nums[0] + nums[1] == 9"
    },
    {
        "id": 2,
        "title": "Reverse String",
        "description": "Write a function that reverses a string without using any built-in reverse functions.",
        "example_input": "'hello'",
        "example_output": "'olleh'"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mcq')
def mcq():
    return render_template('mcq.html', questions=mcq_questions)

@app.route('/coding')
def coding():
    return render_template('coding.html', questions=coding_questions)

if __name__ == '__main__':
    app.run(debug=True)