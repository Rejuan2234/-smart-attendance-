import cv2
import os
import csv
import time
from datetime import datetime



def take_attendance():


    base = os.path.dirname(
        os.path.abspath(__file__)
    )



    trainer_file = os.path.join(
        base,
        "trainer",
        "trainer.yml"
    )


    student_file = os.path.join(
        base,
        "students.csv"
    )


    attendance_folder = os.path.join(
        base,
        "attendance"
    )


    os.makedirs(
        attendance_folder,
        exist_ok=True
    )



    if not os.path.exists(trainer_file):

        print(
            "Please Train Faces First"
        )

        return



    # Load Recognizer

    recognizer = cv2.face.LBPHFaceRecognizer_create()


    recognizer.read(
        trainer_file
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

        print(
            "Haar Cascade Missing"
        )

        return



    # Load Student Data

    students = {}



    if os.path.exists(student_file):


        with open(
            student_file,
            "r",
            encoding="utf-8"
        ) as file:


            reader = csv.reader(file)


            for row in reader:


                if len(row)>=2:


                    students[int(row[0])] = row[1]



    # Camera Start

    camera = cv2.VideoCapture(
        0,
        cv2.CAP_DSHOW
    )



    if not camera.isOpened():

        print(
            "Camera Not Found"
        )

        return



    marked = set()
    AUTO_CLOSE_SECONDS = 10
    last_attendance_time = time.time()


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



            face = gray[
                y:y+h,
                x:x+w
            ]



            student_id, confidence = recognizer.predict(
                face
            )



            # Confidence কম হলে Match

            if confidence < 70:


                name = students.get(
                    student_id,
                    "Unknown"
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

                    name,

                    (x,y-10),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.8,

                    (0,255,0),

                    2
                )



                # Attendance Save

                if student_id not in marked:

                    marked.add(
                        student_id
                    )

                    # Reset timer after new attendance
                    last_attendance_time = time.time()

                    today = datetime.now().strftime(
                        "%Y-%m-%d"
                    )

                    current_time = datetime.now().strftime(
                        "%H:%M:%S"
                    )

                    file_name = os.path.join(

                        attendance_folder,

                        today + ".csv"

                    )

                    file_exist = os.path.exists(
                        file_name
                    )

                    with open(

                        file_name,

                        "a",

                        newline="",

                        encoding="utf-8"

                    ) as file:

                        writer = csv.writer(file)

                        if not file_exist:

                            writer.writerow(

                                [
                                    "ID",
                                    "Name",
                                    "Date",
                                    "Time"
                                ]

                            )

                        writer.writerow(

                            [
                                student_id,
                                name,
                                today,
                                current_time
                            ]

                        )

            else:

                cv2.rectangle(

                    frame,

                    (x,y),

                    (x+w,y+h),

                    (0,0,255),

                    2
                )

                cv2.putText(

                    frame,

                    "Unknown",

                    (x,y-10),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.8,

                    (0,0,255),

                    2

                )

        cv2.imshow(
            "Take Attendance",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        # Press ESC or Q to close
        if key == 27 or key == ord("q"):
            break

        # Close if window is closed
        try:
            if cv2.getWindowProperty(
                "Take Attendance",
                cv2.WND_PROP_VISIBLE
            ) < 1:
                break
        except:
            break

        # Auto close after 10 seconds without new attendance
        if len(marked) > 0:

            if time.time() - last_attendance_time >= AUTO_CLOSE_SECONDS:

                print("Auto Closing Camera...")

                break

    camera.release()

    cv2.destroyAllWindows()