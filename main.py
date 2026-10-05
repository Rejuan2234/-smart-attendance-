from tkinter import *
from tkinter import messagebox

import register
import train
import attendance
import view_attendance



def open_main():

    global root

    root = Tk()

    root.title("Smart Attendance System")


    # Screen Size Detect

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    root.geometry(
        f"{screen_width}x{screen_height}"
    )


    root.resizable(True, True)

    root.configure(
        bg="#f2f6fc"
    )



    # Header

    header = Frame(
        root,
        bg="#1e88e5",
        height=100
    )

    header.pack(
        fill=X
    )



    Label(

        header,

        text="SMART ATTENDANCE SYSTEM",

        font=(
            "Arial",
            28,
            "bold"
        ),

        fg="white",

        bg="#1e88e5"

    ).pack(
        pady=25
    )




    # Main Center Frame

    center = Frame(

        root,

        bg="#f2f6fc"

    )


    center.pack(
        expand=True
    )




    # Button Style

    button_style = {

        "font":(
            "Arial",
            14,
            "bold"
        ),

        "width":25,

        "height":2,

        "bg":"white",

        "fg":"#333",

        "relief":"raised",

        "bd":2

    }



    Button(

        center,

        text="👨‍🎓 Register Student",

        command=register.register_student,

        **button_style

    ).pack(
        pady=12
    )



    Button(

        center,

        text="🧠 Train Faces",

        command=start_training,

        **button_style

    ).pack(
        pady=12
    )



    Button(

        center,

        text="📷 Take Attendance",

        command=attendance.take_attendance,

        **button_style

    ).pack(
        pady=12
    )



    Button(

        center,

        text="📋 View Attendance",

        command=view_attendance.show_attendance,

        **button_style

    ).pack(
        pady=12
    )




    Button(

        center,

        text="Exit",

        command=root.destroy,

        font=(
            "Arial",
            14,
            "bold"
        ),

        width=25,

        height=2,

        bg="#e53935",

        fg="white"

    ).pack(

        pady=12

    )




    # Footer

    footer = Frame(

        root,

        bg="#1e88e5",

        height=50

    )


    footer.pack(

        fill=X,

        side=BOTTOM

    )



    Label(

        footer,

        text="Python + OpenCV Face Recognition System",

        font=(
            "Arial",
            12
        ),

        fg="white",

        bg="#1e88e5"

    ).pack(

        pady=15

    )



    root.mainloop()





def start_training():

    train.train_faces()


    messagebox.showinfo(

        "Success",

        "Face Training Completed!"

    )





# Run Directly

if __name__ == "__main__":

    open_main()