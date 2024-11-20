from django.contrib import admin

from Dosen.models import Dosen
from Evaluasi.models import Evaluasi
from Feedback.models import Feedback
from Mahasiswa.models import Mahasiswa
from Mata_kuliah.models import MataKuliah

from Pengajaran.models import Pengajaran
from Pengambilan_mata_kuliah.models import PengambilanMataKuliah
from Penilaian_kinerja.models import PenilaianKinerja
from Semester.models import Semester


# Dosen (Lecturer) Admin

class DosenAdmin(admin.ModelAdmin):
    list_display = ('id_dosen', 'nama_dosen', 'departemen', 'email', 'jabatan')
    search_fields = ('nama_dosen', 'departemen', 'jabatan')
    list_filter = ('departemen', 'jabatan')
admin.site.register(Dosen,DosenAdmin)

# Mata Kuliah (Course) Admin
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ('id_mata_kuliah', 'nama_mata_kuliah', 'sks', 'semester', 'dosen')
    search_fields = ('nama_mata_kuliah', 'semester')
    list_filter = ('semester',)
    raw_id_fields = ('dosen',)
admin.site.register(MataKuliah,MataKuliahAdmin)

# Mahasiswa (Student) Admin
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('id_mahasiswa', 'nama_mahasiswa', 'program_studi', 'email', 'tahun_masuk')
    search_fields = ('nama_mahasiswa', 'program_studi')
    list_filter = ('program_studi', 'tahun_masuk')
admin.site.register(Mahasiswa,MahasiswaAdmin)

# Pengambilan Mata Kuliah (Course Enrollment) Admin
class PengambilanMataKuliahAdmin(admin.ModelAdmin):
    list_display = ('id_pengambilan', 'mahasiswa', 'mata_kuliah', 'tahun_akademik')
    search_fields = ('tahun_akademik',)
    list_filter = ('tahun_akademik',)
    raw_id_fields = ('mahasiswa', 'mata_kuliah')
admin.site.register(PengambilanMataKuliah,PengambilanMataKuliahAdmin)

# Penilaian Kinerja (Performance Evaluation) Admin
class PenilaianKinerjaAdmin(admin.ModelAdmin):
    list_display = ('id_penilaian', 'dosen', 'mahasiswa', 'mata_kuliah', 'nilai_kinerja', 'tanggal_penilaian')
    search_fields = ('komentar',)
    list_filter = ('tanggal_penilaian', 'dosen')
    raw_id_fields = ('dosen', 'mahasiswa', 'mata_kuliah')
admin.site.register(PenilaianKinerja,PenilaianKinerjaAdmin)

# Evaluasi (Evaluation) Admin
class EvaluasiAdmin(admin.ModelAdmin):
    list_display = ('id_evaluasi', 'dosen', 'mata_kuliah', 'nilai_evaluasi', 'tanggal_evaluasi')
    search_fields = ('komentar',)
    list_filter = ('tanggal_evaluasi', 'dosen')
    raw_id_fields = ('dosen', 'mata_kuliah')
admin.site.register(Evaluasi,EvaluasiAdmin)

# Semester Admin
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id_semester', 'tahun_ajaran', 'nama_semester')
    search_fields = ('tahun_ajaran', 'nama_semester')
    list_filter = ('tahun_ajaran', 'nama_semester')
admin.site.register(Semester,SemesterAdmin)

# Pengajaran (Teaching) Admin
class PengajaranAdmin(admin.ModelAdmin):
    list_display = ('dosen', 'kelas', 'mata_kuliah')
    search_fields = ('kelas',)
    raw_id_fields = ('dosen', 'mata_kuliah')
admin.site.register(Pengajaran,PengajaranAdmin)

# Feedback Admin
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id_feedback', 'evaluasi', 'komentar', 'tanggal_feedback')
    search_fields = ('komentar',)
    list_filter = ('tanggal_feedback',)
    raw_id_fields = ('evaluasi',)
admin.site.register(Feedback,FeedbackAdmin)