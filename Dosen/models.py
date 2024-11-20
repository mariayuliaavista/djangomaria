from django.db import models

# Create your models here.


class Dosen(models.Model):
    id_dosen = models.AutoField(primary_key=True)
    nama_dosen = models.CharField(max_length=100)
    departemen = models.CharField(max_length=100)
    email = models.EmailField()
    jabatan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_dosen

class MataKuliah(models.Model):
    id_mata_kuliah = models.AutoField(primary_key=True)
    nama_mata_kuliah = models.CharField(max_length=100)
    sks = models.IntegerField()
    semester = models.CharField(max_length=20)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_mata_kuliah

class Mahasiswa(models.Model):
    id_mahasiswa = models.AutoField(primary_key=True)
    nama_mahasiswa = models.CharField(max_length=100)
    program_studi = models.CharField(max_length=100)
    email = models.EmailField()
    tahun_masuk = models.IntegerField()

    def __str__(self):
        return self.nama_mahasiswa


class PenilaianKinerja(models.Model):
    id_penilaian = models.AutoField(primary_key=True)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    nilai_kinerja = models.DecimalField(max_digits=5, decimal_places=2)
    komentar = models.TextField()
    tanggal_penilaian = models.DateField()

    def __str__(self):
        return f"Penilaian {self.id_penilaian}"


class PengambilanMataKuliah(models.Model):
    id_pengambilan = models.AutoField(primary_key=True)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    tahun_akademik = models.CharField(max_length=9)

    def __str__(self):
        return f"Pengambilan {self.id_pengambilan}"


class Semester(models.Model):
    id_semester = models.AutoField(primary_key=True)
    tahun_ajaran = models.CharField(max_length=9)
    nama_semester = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_semester


class Pengajaran(models.Model):
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    id_kelas = models.CharField(max_length=50)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pengajaran {self.id_kelas}"
from django.db import models


# Dosen (Lecturer)
class Dosen(models.Model):
    id_dosen = models.AutoField(primary_key=True)
    nama_dosen = models.CharField(max_length=255)
    departemen = models.CharField(max_length=255)
    email = models.EmailField()
    jabatan = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_dosen


# Mata Kuliah (Course)
class MataKuliah(models.Model):
    id_mata_kuliah = models.AutoField(primary_key=True)
    nama_mata_kuliah = models.CharField(max_length=255)
    sks = models.IntegerField()  # Credit units
    semester = models.CharField(max_length=50)  # Example: Genap, Ganjil
    dosen = models.ForeignKey (Dosen, on_delete=models.CASCADE, related_name="mata_kuliah")

    def __str__(self):
        return self.nama_mata_kuliah


# Mahasiswa (Student)
class Mahasiswa(models.Model):
    id_mahasiswa = models.AutoField(primary_key=True)
    nama_mahasiswa = models.CharField(max_length=255)
    program_studi = models.CharField(max_length=255)
    email = models.EmailField()
    tahun_masuk = models.IntegerField()

    def __str__(self):
        return self.nama_mahasiswa
        

# Pengambilan Mata Kuliah (Course Enrollment)
class PengambilanMataKuliah(models.Model):
    id_pengambilan = models.AutoField(primary_key=True)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name="mata_kuliah_diambil")
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="pengambilan")
    tahun_akademik = models.CharField(max_length=9)  # Example: 2023/2024

# Penilaian Kinerja (Performance Evaluation)
class PenilaianKinerja(models.Model):
    id_penilaian = models.AutoField(primary_key=True)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name="penilaian_kinerja")
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name="penilaian_terima")
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="penilaian_kinerja")
    nilai_kinerja = models.DecimalField(max_digits=4, decimal_places=2)
    komentar = models.TextField()
    tanggal_penilaian = models.DateField()

# Evaluasi (Evaluation)
class Evaluasi(models.Model):
    id_evaluasi = models.AutoField(primary_key=True)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name="evaluasi")
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="evaluasi")
    nilai_evaluasi = models.DecimalField(max_digits=4, decimal_places=2)
    komentar = models.TextField()
    tanggal_evaluasi = models.DateField()

# Semester
class Semester(models.Model):
    id_semester = models.AutoField(primary_key=True)
    tahun_ajaran = models.CharField(max_length=9)  # Example: 2023/2024
    nama_semester = models.CharField(max_length=50)  # Example: Genap, Ganjil

# Pengajaran (Teaching)
class Pengajaran(models.Model):
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name="pengajaran")
    kelas = models.CharField(max_length=50)  # Class or section
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="pengajaran")

# Feedback
class Feedback(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    evaluasi = models.ForeignKey(Evaluasi, on_delete=models.CASCADE, related_name="feedback")
    komentar = models.TextField()
    tanggal_feedback = models.DateField()

class Feedback(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    evaluasi = models.ForeignKey(PenilaianKinerja, on_delete=models.CASCADE)
    komentar = models.TextField()
    tanggal_feedback = models.DateField()

    def __str__(self):
        return f"Feedback {self.id_feedback}" 