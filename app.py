from datetime import datetime
import re
from flask import Flask, request, jsonify
from tiny_database import create_a_database

app = Flask(__name__)
db = create_a_database()


def validate_phone(phone):
    phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(re.match(phone_pattern, phone))

def validate_date(date):
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for format_str in date_formats:
        try:
            datetime.strptime(date, format_str)
            return True
        except ValueError:
            pass
    return False

def validate_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(re.match(email_pattern, email))

def get_field_type(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"

def find_matching_template(fields):
    for template in db.all():
        template_fields = {key: value for key, value in template.items() if key != "name"}
        if all(field in fields and get_field_type(fields[field]) == template_fields[field] for field in template_fields):
            return template["name"]
    return None

@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    matching_template = find_matching_template(data)

    if matching_template:
        return jsonify({"template_name": matching_template})
    else:
        field_types = {field: get_field_type(value) for field, value in data.items()}
        return jsonify(field_types)

if __name__ == '__main__':
    app.run(debug=True)


