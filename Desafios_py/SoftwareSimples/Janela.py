import tkinter as tk

def salvar_arquivo():
    texto = texto_box.get("1.0", tk.END)
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write(texto)

janela = tk.Tk()

janela.title("Bloco de Notas")

tb = tk.Text(janela)
tb.pack()

bs = tk.Button(janela, text="Salvar", command=salvar_arquivo)
bs.pack()

janela.mainloop()
