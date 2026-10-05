# Smart Attendance System

**Smart Attendance System** is a Python-based desktop application designed to simplify student attendance management using face recognition technology.

The system provides a graphical user interface for registering students, training face recognition data, recording attendance, and viewing attendance records.

## ✨ Features

* 👨‍🎓 Register students with their ID and name
* 📸 Capture student face images
* 🧠 Train a face recognition model
* 📋 Take attendance using face recognition
* 🕒 Record attendance date and time
* 📊 View attendance records in a table
* 🗑️ Delete attendance records
* 🖥️ User-friendly desktop interface

## 🛠️ Technologies Used

* Python
* Tkinter
* OpenCV
* NumPy
* CSV for data storage
* Haar Cascade for face detection
* LBPH Face Recognizer for face recognition

## 📁 Project Structure

```text
smart-attendance-system/
├── main.py
├── register.py
├── train.py
├── attendance.py
├── view_attendance.py
├── students.csv
├── dataset/
├── trainer/
│   └── trainer.yml
└── README.md
```

*The file structure may vary depending on the project version.*

## 🚀 Getting Started

### 1. Install Python

Install a compatible version of Python on your computer.

### 2. Install Dependencies

Open the terminal in the project folder and run:

```bash
pip install opencv-contrib-python numpy
```

Tkinter is included with many standard Python installations. On some systems, it may need to be installed separately.

### 3. Run the Application

Run the main application file:

```bash
python main.py
```

## 📸 How It Works

1. Register a student using their ID and name.
2. Capture face images for the registered student.
3. Train the face recognition model.
4. Start the attendance process.
5. View the recorded attendance with date and time.

## 🎯 Project Objectives

* Reduce manual attendance-taking effort.
* Explore face detection and recognition using OpenCV.
* Practice Python desktop application development.
* Organize student attendance records digitally.

## 🔮 Future Improvements

* Database integration
* Attendance reports and export options
* Date-wise attendance filtering
* Improved recognition accuracy
* Secure administrator login
* Automatic backup of attendance records

## 👨‍💻 Developer

**Rejuan Ahmed Suvan**

Diploma in Computer Science student from Bangladesh.

GitHub: https://github.com/Rejuan2234

---

*Developed as a Python learning and academic project.*

