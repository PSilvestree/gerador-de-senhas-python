import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import json
import os

# --- LÓGICA DE BACKEND ---
ARQUIVO_SENHAS = "meu_gerenciador.json"

def gerar_senha_logica(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def salvar_senha_logica(servico, usuario, senha):
    dados = carregar_senhas_logica()
    dados[servico] = {"usuario": usuario, "senha": senha}
    with open(ARQUIVO_SENHAS, "w") as f:
        json.dump(dados, f, indent=4)

def carregar_senhas_logica():
    if not os.path.exists(ARQUIVO_SENHAS): return {}
    try:
        with open(ARQUIVO_SENHAS, "r") as f:
            return json.load(f)
    except: return {}

# --- INTERFACE VISUAL (TKINTER NATIVO) ---
class GerenciadorSenhas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Senhas Linux-Friendly")
        self.root.geometry("450x550")
        
        # Estilo para melhorar a aparência no Linux
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10, "bold"))

        # --- Seção de Cadastro ---
        frame_topo = ttk.LabelFrame(root, text=" Gerar Nova Senha ", padding=15)
        frame_topo.pack(pady=10, padx=10, fill="x")

        # Configurar pesos das colunas para o sticky funcionar
        frame_topo.columnconfigure(1, weight=1)

        ttk.Label(frame_topo, text="Serviço:").grid(row=0, column=0, sticky="w")
        self.ent_servico = ttk.Entry(frame_topo)
        self.ent_servico.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(frame_topo, text="Usuário:").grid(row=1, column=0, sticky="w")
        self.ent_usuario = ttk.Entry(frame_topo)
        self.ent_usuario.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(frame_topo, text="Tamanho:").grid(row=2, column=0, sticky="w")
        self.spin_tam = tk.Spinbox(frame_topo, from_=8, to=32, width=5)
        self.spin_tam.delete(0, "end")
        self.spin_tam.insert(0, "12")
        self.spin_tam.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        # --- CORREÇÃO AQUI: Trocado fill="x" por sticky="ew" ---
        self.btn_gerar = ttk.Button(frame_topo, text="Gerar & Salvar", command=self.processar)
        self.btn_gerar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # --- Seção de Visualização ---
        frame_lista = ttk.LabelFrame(root, text=" Senhas Salvas ", padding=15)
        frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        # Barra de rolagem e Lista
        self.texto_exibicao = tk.Text(frame_lista, font=("Monospace", 10), bg="#f0f0f0")
        scroll = ttk.Scrollbar(frame_lista, command=self.texto_exibicao.yview)
        self.texto_exibicao.configure(yscrollcommand=scroll.set)
        
        self.texto_exibicao.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.btn_atualizar = ttk.Button(root, text="Atualizar Lista", command=self.atualizar_lista)
        self.btn_atualizar.pack(pady=5)

        # Iniciar carregando as senhas
        self.atualizar_lista()

    def processar(self):
        serv = self.ent_servico.get()
        user = self.ent_usuario.get()
        
        try:
            tam = int(self.spin_tam.get())
        except ValueError:
            messagebox.showwarning("Erro", "Tamanho deve ser um número!")
            return

        if not serv or not user:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        senha = gerar_senha_logica(tam)
        salvar_senha_logica(serv, user, senha)
        
        messagebox.showinfo("Sucesso", f"Senha para {serv} salva!")
        self.ent_servico.delete(0, tk.END)
        self.ent_usuario.delete(0, tk.END)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.texto_exibicao.config(state="normal")
        self.texto_exibicao.delete("1.0", tk.END)
        dados = carregar_senhas_logica()
        
        if not dados:
            self.texto_exibicao.insert(tk.END, "Nenhuma senha salva ainda.")
        else:
            for s, info in dados.items():
                bloco = f"Srv: {s}\nUsu: {info['usuario']}\nPwd: {info['senha']}\n{'-'*25}\n"
                self.texto_exibicao.insert(tk.END, bloco)
        
        self.texto_exibicao.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorSenhas(root)
    root.mainloop()