from app import db
from app import login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Daftar(db.Model):
    id= db.Column(db.Integer, primary_key=True, nullable=False)
#data pribadi
    nama= db.Column(db.String(30), nullable=False)
    ttl= db.Column(db.String(60), nullable=False)
    jenis_kelamin= db.Column(db.String(30), nullable=False)
    agama= db.Column(db.String(10), nullable=False)
    status= db.Column(db.String(15), nullable=False)
    no_telpon= db.Column(db.String(20), nullable=False)
    email=  db.Column(db.String(25), nullable=False)
    alamat= db.Column(db.String(30), nullable=False)
    prodi= db.Column(db.String(20), nullable=False)
#data akademik
    sekolah_asal= db.Column(db.String(20), nullable=False)
    alamat_sekolah= db.Column(db.String(20), nullable=False)
    thn_lulus= db.Column(db.Integer, nullable=False)
    jurusan= db.Column(db.String(20), nullable=False)
    nilairata= db.Column(db.String(7), nullable=False)
    no_ijazah= db.Column(db.String(50), nullable=False)
#data wali
    nama_wali=  db.Column(db.String(20), nullable=False)
    profesi=  db.Column(db.String(20), nullable=False)
    alamat_wali=  db.Column(db.String(60), nullable=False)
    pendidikan= db.Column(db.String(10), nullable=False)
    no_hp= db.Column(db.String(15), nullable=False)

    created_at= db.Column(db.DATETIME, default=datetime.now())
    updated_at= db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def getAll(self):
        return Daftar.query.all()

    def getOne(self, id):
        return Daftar.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<id:{}>'.format(self.id)

class User(db.Model):
    id=  db.Column(db.Integer, primary_key=True, nullable=False)
    username=  db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(128))
    created_at= db.Column(db.DATETIME, default=datetime.now())
    updated_at= db.Column(db.DATETIME, default=datetime.now())
#view edit delete admin
    def save(self):
        db.session.add(self)
        db.session.commit()

    def getAll(self):
        return User.query.all()

    def getOne(self, id):
        return User.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return '<id:{}>'.format(self.user)