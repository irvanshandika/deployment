from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def page_not_found(error):
    return render_template('error.html', err_msg='Sepertinya Halaman Yang Anda Cari Belum Tersedia, Silahkan Kembali Ke Halaman Utama', title="404 Page Not Found"), 404


@errors.app_errorhandler(403)
def access_denied(error):
    return render_template('error.html', err_msg='403 invalid credentials', title="403 invalid credentials"), 403


@errors.app_errorhandler(500)
def internal_error(error):
    return render_template('error.html', err_msg='Oops, Sepertinya Ada Kesalahan Pada Server. Silahkan Kembali Lagi Setelah Selesai Perbaikan.', title="500 internal server error"), 500