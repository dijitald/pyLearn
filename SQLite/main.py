from flask import Flask, render_template, request, redirect, url_for
from editBookForm import BookForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.secret_key = "gobbledygook"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
bootstrap = Bootstrap5(app)
# all_books = []

class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.rating.desc()))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    myForm = BookForm()
    if myForm.validate_on_submit():
        book = Book(title=myForm.title.data, author=myForm.author.data, rating=myForm.rating.data)
        db.session.add(book) 
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("add.html", form=myForm)

@app.route("/delete/<int:id>")
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit", methods=["GET", "POST"])
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id = -1):
    if id == -1:
        myForm = BookForm()
        myForm.submit.label.text = "Add"
    else:
        book = db.get_or_404(Book, id)
        myForm = BookForm(title=book.title, author=book.author, rating=book.rating)
        myForm.submit.label.text = "Update"

    if myForm.validate_on_submit():
        if id == -1:
            book = Book(title=myForm.title.data, author=myForm.author.data, rating=myForm.rating.data)
            db.session.add(book)
        else:
            book.title = myForm.title.data
            book.author = myForm.author.data
            book.rating = myForm.rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=myForm)

if __name__ == "__main__":
    app.run(debug=True)

