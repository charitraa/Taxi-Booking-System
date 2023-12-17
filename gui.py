import tkinter as tk
from PIL import Image, ImageTk

class login(tk.Tk):
    
    def __init__(self,master=None):
        super().__init__()
        self.master = master
        self.title ('login')
        self.geometry('500x500')


        tk.Label(text='school').place(x=10,y=10)


        
        self.add = tk.Button(text='add',width=20,height=10,font='bold',command=self.pratik)
        self.add.place(x=1000, y=1000)

        # background_image = Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\Veiw\\ILTQq.png')
        # self.background_photo = ImageTk.PhotoImage(background_image)

        # self.canvas = tk.Canvas(self, width=500, height=500)
        # self.canvas.pack()

        # self.canvas.create_image(200, 200, image=self.background_photo)


    # def icons(self):
       


    def pratik(self):
            print('momo')

if __name__ == "__main__":
    ravi = login()
    ravi.mainloop()


