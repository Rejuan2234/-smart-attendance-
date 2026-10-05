import cv2
import os
import numpy as np



def train_faces():


    base = os.path.dirname(
        os.path.abspath(__file__)
    )


    dataset_path = os.path.join(
        base,
        "dataset"
    )


    trainer_path = os.path.join(
        base,
        "trainer"
    )


    os.makedirs(
        trainer_path,
        exist_ok=True
    )



    recognizer = cv2.face.LBPHFaceRecognizer_create()



    faces = []

    ids = []



    if not os.path.exists(dataset_path):

        print("Dataset folder not found")

        return



    # Read Student Folder

    for student_id in os.listdir(dataset_path):


        student_folder = os.path.join(
            dataset_path,
            student_id
        )



        if not os.path.isdir(student_folder):

            continue



        # Read Images

        for image_name in os.listdir(student_folder):


            image_path = os.path.join(
                student_folder,
                image_name
            )



            img = cv2.imread(
                image_path,
                cv2.IMREAD_GRAYSCALE
            )



            if img is None:

                continue



            faces.append(img)



            ids.append(
                int(student_id)
            )



    if len(faces)==0:


        print(
            "No Face Data Found"
        )

        return



    # Training

    recognizer.train(
        faces,
        np.array(ids)
    )



    # Save Model

    recognizer.save(

        os.path.join(
            trainer_path,
            "trainer.yml"
        )

    )



    print(
        "Training Completed Successfully"
    )