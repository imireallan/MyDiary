import re


def validate_user_data(user):
    """ this funtion validates the user data """

    if user['username'] == '':
        return {'warning': 'username is a required field'}, 400

    # Check for empty email
    elif user['email'] == '':
        return {'warning': 'email is a required field'}, 400

    # Check for empty password
    elif user['password'] == '':
        return {'warning': 'password is a required field'}, 400

    elif user['password'] != user['confirm']:
        return {'warning': 'password mismatch!'}, 400

    # Check for a valid user name
    if not re.match(r'^[a-zA-Z0-9_.+-]+$', user['username'].strip(' ')):
        return {'warning': 'Enter a valid username'}, 400

    if user['username'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit username'}, 400

    # Check for a valid email
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            user['email'].strip(' ')):
        return {'warning': 'Enter a valid email address'}, 400

    # check for a valid password
    if not user["password"].strip():
        return {"warning": "Enter a valid password"}, 400

    # Check for large/long inputs
    if len(user['username']) > 15:
        return {'warning': 'username is too long'}, 400

    elif len(user['email']) > 50:
        return {'warning': 'email is too long'}, 400

    elif len(user['password']) < 6:
        return {'warning': 'password requires atlest 6 characters'}, 400

def validate_entry_data(entry):
    """ this funtion validates the entry data """

    # Check for empty title
    if entry['title'] == '':
        return {'warning': 'title is a required field'}, 400

    # Check for empty contents
    elif entry['contents'] == '':
        return {'warning': 'contents is a required field'}, 400
    
    # check for a valid title
    if entry['title'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit title'}, 400

    if not entry["title"].strip():
        return {"warning": "Enter a valid title"}, 400
    
    # check for valid contents
    if entry['contents'].strip(' ').isdigit():
        return {'warning': 'Enter non digit contents'}, 400

    if not entry["contents"].strip():
        return {"warning": "Enter valid contents"}, 400

    # Check for large/long inputs
    if len(entry['title']) > 50:
        return {'warning': 'title is too long'}, 400
