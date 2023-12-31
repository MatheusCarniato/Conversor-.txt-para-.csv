import csv
from customtkinter import *
from tkinter import messagebox

class ConverterCSV():
    """Creates the canvas and elements"""
    def __init__(self):
        self.root = CTk()
        self.root.geometry("700x280")
        self.root.iconbitmap('convertCSV-PY\img\logo (1).ico')
        self.root.resizable(False, False)
        self.root.title("Conversor TXT > CSV")
        self.label = CTkLabel(master=self.root, text = "Insira Abaixo os Dados para Converção:", font=('Arial',16 ,"bold") ).pack(padx = 15, pady = 5, anchor= "sw")
        self.textbox = CTkTextbox(master=self.root, width = 500, height = 220)
        self.textbox.pack(side= LEFT, padx = 10, pady = 10)
        self.buttonupload = CTkButton(master=self.root, text="Carregue arquivo(.txt)", command = self.upload).pack(padx = 5, pady = 5)
        self.buttonconvert = CTkButton(master=self.root, text="Converter(.csv)", command = self.convert).pack(padx = 5, pady = 5)
        self.buttonexit = CTkButton(master=self.root, text="Sair", command = self.root.destroy).pack(padx = 5, pady = 15, side = BOTTOM )
        self.root.mainloop()

    def convert(self):
        """Convert the content"""
        date = self.textbox.get("1.0",END)
        if len(date) > 5:
            filesave = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("Arquivos de texto", "*.csv"), ("Todos os arquivos", "*.csv*")))
            with open(filesave, 'w', newline='', encoding='utf-8') as file_csv:
                writer_csv = csv.writer(file_csv)
                lines = date.split('\n')
                for line in lines:
                    colus = line.strip().split('\t')
                    writer_csv.writerow(colus)
            self.textbox.delete("1.0",END)

            messagebox.showinfo('Concluído',f'Arquivo CSV {filesave} CRIADO COM SUCESSO.')

        else:
            messagebox.showerror('ERRO', 'INSIRA DADOS NO CAMPO OU CARREGUE UM ARQUIVO')
        
    def upload(self):
        """Collects the .txt file and throws it into the text box"""
        file = filedialog.askopenfilename(initialdir="/", filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.txt*")))
        with open(file, 'r',encoding='utf-8') as arquiv_text:
            text = arquiv_text.read()
            self.textbox.insert(END, text)



if __name__ == '__main__':   
    application = ConverterCSV()
    