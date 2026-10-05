from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import csv
from datetime import datetime, timedelta



def show_attendance():

    window = Toplevel()

    window.title("View Attendance")

    window.geometry("1100x650")



    base = os.path.dirname(
        os.path.abspath(__file__)
    )


    attendance_folder = os.path.join(
        base,
        "attendance"
    )


    dataset_folder = os.path.join(
        base,
        "dataset"
    )



    images = []



    # ================= FILTER =================


    filter_value = StringVar()

    filter_value.set("All")



    filter_frame = Frame(window)

    filter_frame.pack(
        pady=10
    )



    Label(
        filter_frame,
        text="Show Attendance:",
        font=("Arial",11,"bold")
    ).pack(
        side=LEFT,
        padx=5
    )



    filter_box = ttk.Combobox(

        filter_frame,

        textvariable=filter_value,

        values=[

            "All",
            "Today",
            "Yesterday",
            "Last 7 Days",
            "Last 30 Days"

        ],

        state="readonly",

        width=18

    )


    filter_box.pack(
        side=LEFT
    )



    # ================= MAIN FRAME =================


    main_frame = Frame(window)

    main_frame.pack(
        fill=BOTH,
        expand=True
    )



    # LEFT TABLE


    left_frame = Frame(main_frame)

    left_frame.pack(

        side=LEFT,

        fill=BOTH,

        expand=True,

        padx=10,

        pady=10

    )



    # RIGHT PHOTO


    right_frame = Frame(

        main_frame,

        width=250,

        bd=2,

        relief=RIDGE

    )


    right_frame.pack(

        side=RIGHT,

        fill=Y,

        padx=10,

        pady=10

    )



    Label(

        right_frame,

        text="Student Photo",

        font=("Arial",14,"bold")

    ).pack(
        pady=10
    )



    photo_label = Label(
        right_frame
    )


    photo_label.pack(
        pady=10
    )



    info_label = Label(

        right_frame,

        text="Select Student",

        font=("Arial",12),

        justify=LEFT

    )


    info_label.pack(
        pady=10
    )



    # TABLE SCROLL


    scroll = Scrollbar(left_frame)

    scroll.pack(

        side=RIGHT,

        fill=Y

    )



    table = ttk.Treeview(

        left_frame,

        columns=(

            "ID",

            "Name",

            "Date",

            "Time"

        ),

        show="tree headings",

        yscrollcommand=scroll.set

    )


    scroll.config(

        command=table.yview

    )



    table.heading(
        "#0",
        text="Photo"
    )

    table.heading(
        "ID",
        text="ID"
    )

    table.heading(
        "Name",
        text="Name"
    )

    table.heading(
        "Date",
        text="Date"
    )

    table.heading(
        "Time",
        text="Time"
    )



    table.column(
        "#0",
        width=70
    )

    table.column(
        "ID",
        width=100
    )

    table.column(
        "Name",
        width=180
    )

    table.column(
        "Date",
        width=120
    )

    table.column(
        "Time",
        width=100
    )



    table.pack(

        fill=BOTH,

        expand=True

    )



    row_data = {}



    # ================= LOAD FUNCTION =================


    def load_data():


        # Clear old data

        for item in table.get_children():

            table.delete(item)



        row_data.clear()

        images.clear()



        if not os.path.exists(attendance_folder):

            return



        for file_name in os.listdir(attendance_folder):


            if file_name.endswith(".csv"):


                file_path = os.path.join(

                    attendance_folder,

                    file_name

                )



                with open(

                    file_path,

                    "r",

                    encoding="utf-8"

                ) as file:



                    reader = csv.reader(file)


                    next(reader,None)



                    for row in reader:


                        if len(row) < 4:

                            continue



                        record_date = datetime.strptime(

                            row[2],

                            "%Y-%m-%d"

                        ).date()



                        today = datetime.now().date()



                        option = filter_value.get()



                        if option == "Today":

                            if record_date != today:

                                continue



                        elif option == "Yesterday":

                            if record_date != today - timedelta(days=1):

                                continue



                        elif option == "Last 7 Days":

                            if record_date < today - timedelta(days=6):

                                continue



                        elif option == "Last 30 Days":

                            if record_date < today - timedelta(days=29):

                                continue


                        # -------- LOAD PHOTO --------

                        student_id = str(row[0])


                        photo_path = os.path.join(

                            dataset_folder,

                            student_id,

                            "1.jpg"

                        )


                        photo = None


                        if os.path.exists(photo_path):

                            img = Image.open(
                                photo_path
                            )


                            img = img.resize(
                                (50,50)
                            )


                            photo = ImageTk.PhotoImage(
                                img
                            )


                            images.append(
                                photo
                            )



                        item = table.insert(

                            "",

                            END,

                            image=photo,

                            values=(

                                row[0],

                                row[1],

                                row[2],

                                row[3]

                            )

                        )


                        row_data[item] = {

                            "file": file_path,

                            "values": row

                        }





    # ================= SHOW SELECTED PHOTO =================


    def show_selected(event):


        selected = table.selection()


        if not selected:

            return



        item = selected[0]


        values = table.item(item)["values"]



        student_id = str(values[0])



        photo_path = os.path.join(

            dataset_folder,

            student_id,

            "1.jpg"

        )



        if os.path.exists(photo_path):


            img = Image.open(
                photo_path
            )


            img = img.resize(
                (160,160)
            )


            photo = ImageTk.PhotoImage(
                img
            )


            photo_label.config(
                image=photo
            )


            photo_label.image = photo



        info_label.config(

            text=f"""

ID : {values[0]}

Name : {values[1]}

Date : {values[2]}

Time : {values[3]}

"""

        )



    table.bind(

        "<<TreeviewSelect>>",

        show_selected

    )



    # ================= DELETE =================


    def delete_selected():


        selected = table.selection()


        if not selected:

            messagebox.showwarning(

                "Warning",

                "Select attendance first"

            )

            return



        if not messagebox.askyesno(

            "Confirm",

            "Delete selected attendance?"

        ):

            return



        files = {}



        for item in selected:


            data = row_data[item]


            file_path = data["file"]


            if file_path not in files:


                with open(

                    file_path,

                    "r",

                    encoding="utf-8"

                ) as f:


                    files[file_path] = list(
                        csv.reader(f)
                    )



        for item in selected:


            data = row_data[item]


            file_path = data["file"]

            remove = data["values"]



            new_rows = []



            for row in files[file_path]:


                if row == remove:

                    continue


                new_rows.append(row)



            files[file_path] = new_rows


            table.delete(item)



        for file_path, rows in files.items():


            with open(

                file_path,

                "w",

                newline="",

                encoding="utf-8"

            ) as f:


                writer = csv.writer(f)

                writer.writerows(rows)



        messagebox.showinfo(

            "Success",

            "Deleted successfully"

        )





    def delete_all():


        if not messagebox.askyesno(

            "Confirm",

            "Delete all attendance?"

        ):

            return



        for file_name in os.listdir(attendance_folder):


            if file_name.endswith(".csv"):


                file_path = os.path.join(

                    attendance_folder,

                    file_name

                )


                with open(

                    file_path,

                    "w",

                    newline="",

                    encoding="utf-8"

                ) as f:


                    writer = csv.writer(f)


                    writer.writerow(

                        [

                            "ID",

                            "Name",

                            "Date",

                            "Time"

                        ]

                    )



        load_data()



    # ================= BUTTONS =================


    button_frame = Frame(window)

    button_frame.pack(
        pady=10
    )



    Button(

        button_frame,

        text="Delete Selected",

        width=18,

        bg="red",

        fg="white",

        command=delete_selected

    ).grid(

        row=0,

        column=0,

        padx=10

    )



    Button(

        button_frame,

        text="Delete All",

        width=18,

        bg="darkred",

        fg="white",

        command=delete_all

    ).grid(

        row=0,

        column=1,

        padx=10

    )



    # Filter Change হলে আবার Load হবে

    filter_box.bind(

        "<<ComboboxSelected>>",

        lambda e: load_data()

    )



    # প্রথমবার Load

    load_data()