import streamlit as st
from recognition import FaceRecognition, MarkAttendance

# Inisialisasi objek FaceRecognition
fr = FaceRecognition()

# Variabel untuk mengontrol status kamera
camera_running = False

# Fungsi untuk menjalankan pengenalan wajah
def run_face_recognition():
    global camera_running
    camera_running = True
    fr.run_recognition()

# Fungsi untuk menghentikan kamera
def stop_camera():
    global camera_running
    camera_running = False

def mark_attendance(name, status):
    MarkAttendance(name, status)
    st.success(f"{name} Sukses melakukan Absensi dengan status: {status}!")


# Tampilan desktop menggunakan Streamlit
def main():
    st.title("Sistem Absensi Face Recognition")
    st.write("Selamat datang di Sistem Absensi SMAN CIMANGGUNG!")

    # Jalankan pengenalan wajah dalam mode penuh
    if st.button("Start Face Recognition"):
        run_face_recognition()

    # Input nama untuk menandai kehadiran
    name = st.text_input("Masukan Nama Siswa:")
    status = st.selectbox("Status Kehadiran:", ("Hadir", "Tidak Hadir"))
    if st.button("Absen"):
        mark_attendance(name, status)
        st.success(f"{name} Sukses melakukan Absensi!")

    # Tombol untuk menghentikan kamera
    if st.button("Stop Camera"):
        stop_camera()


if __name__ == '__main__':
    main()
