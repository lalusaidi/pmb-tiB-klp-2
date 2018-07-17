from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired

class DaftarSave(FlaskForm):
    msg = 'data tidak boleh kosong'
#data pribadi
    nama = StringField('Nama', validators=[DataRequired(message=msg)])
    ttl = StringField('Ttl', validators=[DataRequired(message=msg)])
    jenis_kelamin = SelectField('Jenis Kelamin', choices=[('','--jenis kelamin--'),('Laki-laki','Laki-laki'),('perempuan','perempuan')], validators=[DataRequired(message=msg)])
    agama = SelectField('Agama', choices=[('Islam','Islam'),('Kristen','Kristen'),('Hindu','Hindu'),('Budha','Budha')], validators=[DataRequired(message=msg)])
    status = StringField('Status', validators=[DataRequired(message=msg)])
    no_telpon = StringField('No. Telpon', validators=[DataRequired(message=msg)])
    email = StringField('E-Mail', validators=[DataRequired(message=msg)])
    alamat = StringField('Alamat', validators=[DataRequired(message=msg)])
    prodi = SelectField('Pilihan Prodi', choices=[('','--pilihan prodi--'),('S1 TEKNIK INFORMATIKA','S1 TEKNIK INFORMATIKA'),('S1 SISTEM INFORMASI','S1 SISTEM INFORMASI'),('S1 MANAJEMEN INFORMATIKA','S1 MANAJEMEN INFORMATIKA')],validators=[DataRequired(message=msg)])
#data akademik
    sekolah_asal = StringField('Sekolah Asal', validators=[DataRequired(message=msg)])
    alamat_sekolah = StringField('Alamat Sekolah', validators=[DataRequired(message=msg)])
    thn_lulus = StringField('Tahun Lulus', validators=[DataRequired(message=msg)])
    jurusan = StringField('Jurusan', validators=[DataRequired(message=msg)])
    nilairata = StringField('Nilai Rata-Rata Ujian', validators=[DataRequired(message=msg)])
    no_ijazah = StringField('No. Ijazah', validators=[DataRequired(message=msg)])
#data wali
    nama_wali = StringField('Nama Wali', validators=[DataRequired(message=msg)])
    profesi = StringField('Profesi Wali', validators=[DataRequired(message=msg)])
    alamat_wali = StringField('Alamat Wali', validators=[DataRequired(message=msg)])
    pendidikan = StringField('Pendidikan Terakhir', validators=[DataRequired(message=msg)])
    no_hp = StringField('No. Telpon', validators=[DataRequired(message=msg)])
    submit = SubmitField('Daftar')