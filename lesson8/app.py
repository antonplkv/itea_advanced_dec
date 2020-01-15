from flask import Flask, request
from flask import render_template, redirect
from db_data import STUDENTS
app = Flask(__name__)

# dict_to_buy = {
#     'milk': 2,
#     'fish': 1,
#     'meat': 2,
#     'orange': 10
# }

# @app.route('/product')
# def hello_world():
#
#     list_of_items = ['zxc', 'zxc', 'vbn']
#     return render_template('index.html',
#                            list_of_items=list_of_items,
#                            to_buy=dict_to_buy)
#
# @app.route('/product/<string:name>')
# def get_product_by_name(name):
#     return str(dict_to_buy[name])

@app.route('/students')
def get_students():

    return render_template('students.html',
                           students=STUDENTS)

@app.route('/students/<int:student_id>')
def get_student_marks(student_id):
    student = STUDENTS[student_id]

    return render_template('marks.html',
                           marks=student['marks'],
                           average=sum(student['marks']) / len(student['marks']))

@app.route('/students/create', methods=['POST'])
def create_student():

    students_dict = dict(request.form)
    print(students_dict)
    students_dict['marks'] = list(students_dict['marks'])
    STUDENTS.append(dict(students_dict))
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)
