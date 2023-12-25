import tkinter as tk
root = tk.Tk()
root.geometry('500x400')
root.title('TKinter Hub')

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='home page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    home_frame.pack(pady=20)

def indicate(lb):
    lb.config(bg='#158aff')

options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15),fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_btn))

home_btn.place(x=10,y=50)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3').place(x=3,y=50,width=5, height=40)

menu_btn = tk.Button(options_frame, text='Menu', font=('bold', 15),fg='#158aff', bd=0, bg='#c3c3c3',command=lambda: indicate(home_btn))

menu_btn.place(x=10, y=100)

menu_indicate = tk.Label(options_frame, text='', bg='#c3c3c3').place(x=3,y=100,width=5, height=40)

Contact_btn = tk.Button(options_frame, text='Contact', font=('bold', 15),fg='#158aff', bd=0, bg='#c3c3c3',command=lambda: indicate(home_btn))

Contact_btn.place(x=10, y=150)

contact_indicate = tk.Label(options_frame, text='', bg='#c3c3c3').place(x=3,y=150,width=5, height=40)

about_btn = tk.Button(options_frame, text='About', font=('bold', 15),fg='#158aff', bd=0, bg='#c3c3c3',command=lambda: indicate(home_btn))

about_btn.place(x=10, y=200)

about_indicate = tk.Label(options_frame, text='', bg='#c3c3c3').place(x=3,y=200,width=5, height=40)


options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100,height=400)

main_frame = tk.Frame(root,highlightthickness=2,highlightbackground='black')

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

root.mainloop()
