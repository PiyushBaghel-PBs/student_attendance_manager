# 🎓 Student Attendance Manager

A lightweight, menu-driven Python 3 console application designed to manage student records, log daily attendance, track individual attendance percentages, and generate automatic shortage reports for students falling below the 75% requirement.

---

## 🚀 Features

- 👤 **Student Registration:** Add new students with unique roll numbers.
- 📝 **Daily Attendance Logging:** Easily mark students as **Present (P)** or **Absent (A)**.
- 📊 **Percentage Tracking:** Calculate attendance percentages dynamically with zero-division error handling for newly added students.
- ⚠️ **Shortage Warning List:** Automatically filter and list students with attendance below **75%**.
- 💾 **Data Persistence:** Automatically saves all records to a local text file (`attendance.txt`) after every update and restores them on launch.

---

## 🛠️ Project Structure

```text
student-attendance-manager/
│
├── one.py   # Main Python source code
├── attendance.txt          # File storage for student records (auto-generated)
└── README.md               # Project documentation
