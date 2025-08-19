import tkinter as tk
from PIL import ImageTk
import qrcode

def generate_qr_code(event=None):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    data = input_entry.get()    
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill="black", back_color="Yellow")
    qr_image.save("qr_code.png")

    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=qr_photo)
    qr_label.photo = qr_photo



####################################################################
root = tk.Tk()
root.title("QR Code Generator")
root.geometry('500x520')
root.configure(bg='lightblue')
root.resizable(False,False)


l_label1=tk.Label(root,text="QRCode Generator",bg='lightblue',fg='Blue',font=('Helvetica',18)).pack()

l_label=tk.Label(root,text='Enter the link or data to generate Qrcode : ',bg='lightblue',font=('Helvetica',16),fg='red')
l_label.pack(pady=30,padx=10)

input_entry = tk.Entry(root,font=('arial',12),borderwidth=(4),bg='Turquoise')
input_entry.pack(padx=10,pady=5,ipady=6,ipadx=100)
input_entry.focus_set()

generate_button = tk.Button(root, text="Generate QR Code",font=('arial',12), command=generate_qr_code,bg='Turquoise')
generate_button.pack(padx=10,pady=10)


qr_label = tk.Label(root,bg='lightblue')
qr_label.pack(padx=10,pady=10)

root.bind("<Return>",generate_qr_code)

root.mainloop()