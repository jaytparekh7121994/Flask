from flask import Flask
ci_cd_app = Flask(__name__)


def dash():
    return "--"*40+ "<br/>"


@ci_cd_app.route('/')
def hello():
    default_string = "Hello Keanu Reeves, Hello World!<br/>"\
            "This is the default page once the WEB APPLICATION starts<br/>" \
            "Try using admin or your name in the above url after / <br/>"\
            "Example: 1. localhost:5000/admin <br/> " \
            "         2. localhost:5000/your_name <br/>" \
            "         3. localhost:5000/about_us <br/>"
    return default_string


@ci_cd_app.route('/admin')
def hello_admin():
    return "Hello Administrator!"


@ci_cd_app.route('/<user_name>')
def hello_user(user_name):
    return "Hello Guest {}!".format(user_name)


@ci_cd_app.route('/about_us')
def about_us():
    about = "This is a CI CD sample Web application <br/>"
    das = dash()
    team_details = "There are 3 Teams in CI_CD: <br/>" \
                   " 1. Development Team : Pooja Date, Sujay Metkar and Jay Parekh <br/> " \
                   " 2.Integration and Testing Team : Prajakta Kumbhar, Deepali Shingare and Sonali Jamdar <br/>" \
                   " 3.Deployment Team : Jayashri Mahale, Shubham Alok and Jay Parekh <br/>"

    return about + das + team_details + das


if __name__ == '__main__':
    ci_cd_app.run()
