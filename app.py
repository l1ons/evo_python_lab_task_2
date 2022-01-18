from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import Main_form


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY = 'c51bdcd68a2bd21c3dbaf992a2b6df48',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
))
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.name}')"



@app.route('/', methods=['GET', 'POST'])
def index():
    form = Main_form()
    if form.validate_on_submit():
        try:
            user = User(name=form.name.data)
            db.session.add(user)
            db.session.commit()
            flash('Привіт, {}'.format(form.name.data), 'success')
        except:
            flash('Вже бачилися, {}'.format(form.name.data), 'success')
        return render_template('one.html', form=form)

    return render_template('one.html', form=form)

@app.route('/list')
def list():
    users = User.query.all()
    return render_template('list.html',users=users)

if __name__ == '__main__':
    app.run()