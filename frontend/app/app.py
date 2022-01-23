from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import connect, Error
# db_params = {
#     "host": "192.168.0.105",
#     "database": "postgres",
#     "user": "postgres",
#     "password": "password",
#     "port": "5432"
# }

app = Flask(__name__)
#для подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1@192.168.0.105/postgres'
db = SQLAlchemy(app)
class Pink_Floyd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #wrappertype = db.Column(db.String)
    kind = db.Column(db.String)
    # artistid = db.Column(db.String)
    # collectionid = db.Column(db.String)
    # trackid = db.Column(db.String)
    # artistname = db.Column(db.String)
    collectionname = db.Column(db.String)
    trackname = db.Column(db.String)
    # collectioncensoredname = db.Column(db.String)
    # trackviewurl = db.Column(db.String)
    # previewurl = db.Column(db.String)
    # artworkurl30 = db.Column(db.String)
    # artworkurl60 = db.Column(db.String)
    # trackcensoredname = db.Column(db.String)
    # artistviewurl = db.Column(db.String)
    # collectionviewurl = db.Column(db.String)
    # artworkurl100 = db.Column(db.String)
    collectionprice = db.Column(db.String)
    trackprice = db.Column(db.String)
    releasedate = db.Column(db.Date)
    # collectionexplicitness = db.Column(db.String)
    # trackexplicitness = db.Column(db.String)
    # disccount = db.Column(db.String)
    # discnumber = db.Column(db.String)
    trackcount = db.Column(db.String)
    tracknumber = db.Column(db.String)
    # tracktimemillis = db.Column(db.String)
    # country = db.Column(db.String)
    # currency = db.Column(db.String)
    primarygenrename = db.Column(db.String)
    # isstreamable = db.Column(db.String)

    # class Tag(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     wrappertype = db.Column(db.String)
    #     kind = db.Column(db.String)
    #     artistid = db.Column(db.String)
    #     collectionid = db.Column(db.String)
    #     trackid = db.Column(db.String)
    #     artistname = db.Column(db.String)
    #     collectionname = db.Column(db.String)
    #     trackname = db.Column(db.String)
    #     collectioncensoredname = db.Column(db.String)
    #     trackviewurl = db.Column(db.String)
    #     previewurl = db.Column(db.String)
    #     artworkurl30 = db.Column(db.String)
    #     artworkurl60 = db.Column(db.String)
    #     trackcensoredname = db.Column(db.String)
    #     artistviewurl = db.Column(db.String)
    #     collectionviewurl = db.Column(db.String)
    #     artworkurl100 = db.Column(db.String)
    #     collectionprice = db.Column(db.String)
    #     trackprice = db.Column(db.String)
    #     releasedate = db.Column(db.String)
    #     collectionexplicitness = db.Column(db.String)
    #     trackexplicitness = db.Column(db.String)
    #     disccount = db.Column(db.String)
    #     discnumber = db.Column(db.String)
    #     trackcount = db.Column(db.String)
    #     tracknumber = db.Column(db.String)
    #     tracktimemillis = db.Column(db.String)
    #     country = db.Column(db.String)
    #     currency = db.Column(db.String)
    #     primarygenrename = db.Column(db.String)
    #     isstreamable = db.Column(db.String)
    #
    #     Article_id = db.Column(db.Integer, db.ForeignKey('Article_id'), nullable=False)
    #     Article = db.relationship('Article', backref=db.backref('tags', lazy=True))

    #def __repr__(self):
   #     return  '<Article %r>' % self.id


@app.route('/kud')
def kud():
    con = connect("dbname='postgres' user='postgres' password='Password1' host='192.168.0.105' port='5432' ")
#    con = connect('db_params')
    cur = con.cursor()
#    cur.execute("SELECT * FROM pink_floyd")
    cur.execute("SELECT id, kind, collectionName, trackName, collectionPrice, trackPrice, primaryGenreName, trackCount, trackNumber, releaseDate FROM pink_floyd")
    data = cur.fetchall()

    return render_template('kud.html', data=data)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)

if __name__ == "__main__":
    app.run(debug=True)
