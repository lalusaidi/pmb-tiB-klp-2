from flask import url_for, redirect, render_template
from app.forms.daftar import DaftarSave
from app.models.models import Daftar
from app import db

class DaftarController:
    def input(self):
        daftarsave =DaftarSave()
        if daftarsave.validate_on_submit():
            daftar= Daftar(nama= daftarsave.nama.data, ttl=daftarsave.ttl.data, jenis_kelamin=daftarsave.jenis_kelamin.data, agama=daftarsave.agama.data, status=daftarsave.status.data, no_telpon=daftarsave.no_telpon.data, email=daftarsave.email.data, alamat=daftarsave.alamat.data, prodi=daftarsave.prodi.data, sekolah_asal=daftarsave.sekolah_asal.data, alamat_sekolah=daftarsave.alamat_sekolah.data, thn_lulus=daftarsave.thn_lulus.data, jurusan=daftarsave.jurusan.data, nilairata=daftarsave.nilairata.data, no_ijazah= daftarsave.no_ijazah.data, nama_wali=daftarsave.nama_wali.data, profesi=daftarsave.profesi.data, alamat_wali=daftarsave.alamat_wali.data, pendidikan=daftarsave.pendidikan.data, no_hp=daftarsave.no_hp.data)
            daftar.save()
            return redirect(url_for('input_daftar'))
        return render_template('daftar/input.html', form= daftarsave, title='input pendaftaran')
    
    def index(self):
        daftarsave =DaftarSave()
        daftar=Daftar().getAll()
        return render_template('daftar/index.html', form= daftarsave, title='view pendaftaran', daftar=daftar)
    
    def edit(self, id):
        daftarsave= DaftarSave()
        daftar= Daftar().getOne(id)
        if daftarsave.validate_on_submit():
        #data pribadi
            daftar.nama= daftarsave.nama.data
            daftar.ttl=daftarsave.ttl.data
            daftar.jenis_kelamin=daftarsave.jenis_kelamin.data
            daftar.agama=daftarsave.agama.data
            daftar.status=daftarsave.status.data
            daftar.no_telpon=daftarsave.no_telpon.data
            daftar.email=daftarsave.email.data
            daftar.alamat=daftarsave.alamat.data
            daftar.prodi=daftarsave.prodi.data
        #data akademik
            daftar.sekolah_asal=daftarsave.sekolah_asal.data
            daftar.alamat_sekolah=daftarsave.alamat_sekolah.data
            daftar.thn_lulus=daftarsave.thn_lulus.data
            daftar.jurusan=daftarsave.jurusan.data
            daftar.nilai_rata=daftarsave.nilairata.data
            daftar.no_ijazah= daftarsave.no_ijazah.data
        #data wali
            daftar.nama_wali=daftarsave.nama_wali.data
            daftar.profesi=daftarsave.profesi.data
            daftar.alamat_wali=daftarsave.alamat_wali.data
            daftar.pendidikan=daftarsave.pendidikan.data
            daftar.no_hp=daftarsave.no_hp.data
            db.session.commit()
            return redirect(url_for('index_daftar'))
        return render_template('daftar/edit.html', form=daftarsave, daftar=daftar)

    def delete(self, id):
        daftar = Daftar().getOne(id)
        daftar.delete()
        return redirect(url_for('index_daftar'))