#adicionando a biblioteca tkinter para poder desenvolver uma interface gráfica
import tkinter as tk

#define a classe Livro que é usada para criar objetos que vão representar os livros dentro do catálogo
#aqui também são apresentadas as instâncias  da classe livro e a definição dos atributos (título, autor, exemplares disponíveis)

class Livro:
    def __init__(self, titulo, autor, exemplares_disponiveis): #esse é o construtor da classe livro, ele vai receber os parâmetros título, autor e exemplares disponíveis
        self.titulo = titulo
        self.autor = autor
        if exemplares_disponiveis > 0: #o bloco de if vai verificar se o número de exemplares é maior que 0
            self.exemplares_disponiveis = exemplares_disponiveis
        else:
            raise ValueError("O número de exemplares disponiveis deve ser maior que zero.")

    def __str__(self): #essa linha permite que possamos converter um objeto livro em string que vai ser apresentada no return abaixo
        return f'Título: {self.titulo}, Autor: {self.autor}, Exemplares Disponíveis: {self.exemplares_disponiveis}'


#define a classe Catalogo que é usada para gerenciar o catálogo de livros, permite adicionar livros, listar e pesquisar as informações sobre os livros no sistema
class Catalogo:
    def __init__(self): #construtor da classe Catalogo, ele vai iniciar um atributo catalogo como uma lista vazia
        self.catalogo = []

    def adicionar_livro(self, livro): #permite adicionar itens a lista catalogo
        self.catalogo.append(livro)

    def listar_livros(self): #retorna a lista dos livros presentes no catalogo
        return self.catalogo

    def pesquisar_livros(self, termo): #permite consultar os livros no catalogo com base em um termo de pesquisa
        resultados = []
        for livro in self.catalogo:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                resultados.append(livro)
        return resultados

def adicionar_livro():
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    exemplares = exemplares_entry.get()
    try:
        exemplares = int(exemplares)
        livro = Livro(titulo, autor, exemplares)
        catalogo.adicionar_livro(livro)
        resultado_label.config(text="Livro adicionado com sucesso!")
    except ValueError:
        resultado_label.config(text="Número de exemplares inválido!")

def pesquisar_livros():
    termo = pesquisa_entry.get()
    resultados = catalogo.pesquisar_livros(termo)
    resultado_listbox.delete(0, tk.END)
    if resultados:
        for livro in resultados:
            resultado_listbox.insert(tk.END, str(livro))
    else:
        resultado_listbox.insert(tk.END, "Nenhum livro encontrado para o termo de pesquisa.")

# Criar um catálogo vazio
catalogo = Catalogo()

# Configurar a interface gráfica
root = tk.Tk()
root.title("Catálogo de Livros")

frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)
frame_pesquisar = tk.Frame(root)
frame_pesquisar.pack(pady=10)

titulo_label = tk.Label(frame_adicionar, text="Título:")
autor_label = tk.Label(frame_adicionar, text="Autor:")
exemplares_label = tk.Label(frame_adicionar, text="Exemplares:")
titulo_entry = tk.Entry(frame_adicionar)
autor_entry = tk.Entry(frame_adicionar)
exemplares_entry = tk.Entry(frame_adicionar)
adicionar_button = tk.Button(frame_adicionar, text="Adicionar Livro", command=adicionar_livro)
resultado_label = tk.Label(frame_adicionar, text="")

pesquisa_label = tk.Label(frame_pesquisar, text="Pesquisar por Título ou Autor:")
pesquisa_entry = tk.Entry(frame_pesquisar)
pesquisar_button = tk.Button(frame_pesquisar, text="Pesquisar Livros", command=pesquisar_livros)
resultado_listbox = tk.Listbox(frame_pesquisar, width=100, height=10)

titulo_label.grid(row=0, column=0)
autor_label.grid(row=1, column=0)
exemplares_label.grid(row=2, column=0)
titulo_entry.grid(row=0, column=1)
autor_entry.grid(row=1, column=1)
exemplares_entry.grid(row=2, column=1)
adicionar_button.grid(row=3, column=0, columnspan=2)
resultado_label.grid(row=4, column=0, columnspan=2)

pesquisa_label.grid(row=0, column=0)
pesquisa_entry.grid(row=0, column=1)
pesquisar_button.grid(row=1, column=0, columnspan=2)
resultado_listbox.grid(row=2, column=0, columnspan=2)

root.mainloop()