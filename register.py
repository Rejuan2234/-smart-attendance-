from tkinter import *
from tkinter import messagebox
import cv2
import os
import csv



def register_student():

    window = Toplevel()

    window.title("Register Student")
    window.geometry("350x300")
    window.resizable(False, False)



    Label(
        window,
        text="Student ID"
    ).pack(pady=5)


    id_entry = Entry(
        window,
        width=30
    )

    id_entry.pack()



    Label(
        window,
        text="Student Name"
    ).pack(pady=5)


    name_entry = Entry(
        window,
        width=30
    )

    name_entry.pack()



    def capture_face():


        student_id = id_entry.get().strip()
        student_name = name_entry.get().strip()



        if student_id == "" or student_name == "":

            messagebox.showerror(
                "Error",
                "Please fill all information"
            )

            return



        base = os.path.dirname(
            os.path.abspath(__file__)
        )



        # Create Dataset Folder

        dataset_path = os.path.join(
            base,
            "dataset"
        )

        os.makedirs(
            dataset_path,
            exist_ok=True
        )



        student_folder = os.path.join(
            dataset_path,
            student_id
        )


        os.makedirs(
            student_folder,
            exist_ok=True
        )



        # Save Student Information

        csv_file = os.path.join(
            base,
            "students.csv"
        )



        already = False


        if os.path.exists(csv_file):

            with open(
                csv_file,
                "r",
                encoding="utf-8"
            ) as file:


                reader = csv.reader(file)


                for row in reader:

                    if len(row)>0 and row[0]==student_id:

                        already=True
                        break



        if not already:


            with open(
                csv_file,
                "a",
                newline="",
                encoding="utf-8"
            ) as file:


                writer = csv.writer(file)


                writer.writerow(
                    [
                        student_id,
                        student_name
                    ]
                )



        # Face Detector

        cascade_path = os.path.join(
            base,
            "haarcascade_frontalface_default.xml"
        )


        detector = cv2.CascadeClassifier(
            cascade_path
        )


        if detector.empty():

            messagebox.showerror(
                "Error",
                "Haar Cascade File Missing"
            )

            return



        camera = cv2.VideoCapture(
            0,
            cv2.CAP_DSHOW
        )


        if not camera.isOpened():

            messagebox.showerror(
                "Error",
                "Camera Not Found"
            )

            return



        count = 0



        while True:


            ret, frame = camera.read()


            if not ret:

                break



            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )



            faces = detector.detectMultiScale(
                gray,
                1.3,
                5
            )



            for (x,y,w,h) in faces:


                count += 1



                face = gray[
                    y:y+h,
                    x:x+w
                ]



                cv2.imwrite(

                    os.path.join(
                        student_folder,
                        str(count)+".jpg"
                    ),

                    face
                )



                cv2.rectangle(

                    frame,

                    (x,y),

                    (x+w,y+h),

                    (0,255,0),

                    2
                )



                cv2.putText(

                    frame,

                    f"Image {count}/20",

                    (10,30),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.8,

                    (0,255,0),

                    2
                )



            cv2.imshow(
                "Capture Face",
                frame
            )



            if cv2.waitKey(1)==27:

                break



            if count>=20:

                break




        camera.release()

        cv2.destroyAllWindows()



        messagebox.showinfo(
            "Success",
            "Student Registered Successfully"
        )


        window.destroy()



    Button(

        window,

        text="Capture Face",

        width=20,

        height=2,

        command=capture_face

    ).pack(pady=30)