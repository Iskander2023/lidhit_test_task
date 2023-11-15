from tinydb import TinyDB

def create_a_database():
    db = TinyDB('templates.json')

    if not db.all():
        initial_templates = [
            {
                "name": "MyForm",
                "user_name": "text",
                "date": "date",
                "email": "email"
            },
            {
                "name": "AnotherForm",
                "user_name": "text",
                "phone_number": "phone"
            }
        ]

        db.insert_multiple(initial_templates)

    return db