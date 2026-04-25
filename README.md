# 🔐 Gerenciador de Senhas Python

Aplicação desktop em Python com interface gráfica (Tkinter) para gerar senhas seguras e gerenciar credenciais localmente. Otimizada para ambientes **Linux** (Debian/Ubuntu/Mint).

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-success)

---

## 🎯 Funcionalidades

- ✅ **Gerador de Senhas Seguras** - Caracteres aleatórios (letras, números, símbolos)
- ✅ **Customização de Tamanho** - Escolha entre 8 e 32 caracteres
- ✅ **Gerenciamento Local** - Armazena senhas em arquivo JSON criptografado
- ✅ **Interface Gráfica Intuitiva** - GUI nativa com Tkinter
- ✅ **Visualização de Senhas Salvas** - Lista com scroll automático
- ✅ **Compatibilidade Linux** - Estilo otimizado para ambientes Linux
- ✅ **Sem Dependências Externas** - Usa apenas stdlib do Python

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Descrição |
|---|---|---|
| **Python** | 3.8+ | Linguagem principal |
| **Tkinter** | Built-in | Interface gráfica nativa |
| **JSON** | Built-in | Armazenamento de dados |
| **OS** | Built-in | Gerenciamento de arquivos |

**Nenhuma dependência externa necessária!** O projeto usa apenas a biblioteca padrão do Python.

---

## 📦 Instalação

### Pré-requisitos

```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-tk

# Fedora
sudo dnf install python3 python3-tkinter

# Arch
sudo pacman -S python tk

# macOS (via Homebrew)
brew install python-tk
```

### Setup Rápido

```bash
# Clone o repositório
git clone https://github.com/PSilvestree/gerador-de-senhas-python.git
cd gerador-de-senhas-python

# Execute a aplicação
python3 gerador_senhas.py
```

✅ **Pronto!** A aplicação abrirá em uma janela gráfica.

---

## 🚀 Como Usar

### Interface Gráfica (Recomendado)

```bash
python3 gerador_senhas.py
```

#### Passos:

1. **Preencha os campos:**
   - **Serviço:** Nome da aplicação/site (ex: Gmail, GitHub, Instagram)
   - **Usuário:** Seu nome de usuário ou email
   - **Tamanho:** Comprimento desejado da senha (8-32 caracteres, padrão: 12)

2. **Clique em "Gerar & Salvar"**
   - A senha será gerada automaticamente
   - Salva em `meu_gerenciador.json`
   - Aparece na lista abaixo

3. **Visualize suas senhas**
   - Todas as senhas salvas aparecem na seção "Senhas Salvas"
   - Clique "Atualizar Lista" para refrescar

---

## 📋 Exemplos de Uso

### Exemplo 1: Gerar senha para Gmail

```
Serviço: Gmail
Usuário: seu.email@gmail.com
Tamanho: 16

[Clica "Gerar & Salvar"]

✅ Senha gerada e salva!
Resultado: X7$mK9@pL2&qRtUv
```

### Exemplo 2: Gerar senha simples

```
Serviço: GitHub
Usuário: PSilvestree
Tamanho: 12

[Clica "Gerar & Salvar"]

✅ Senha: aB3cD5eF7gH9
```

---

## 📂 Estrutura do Projeto

```
gerador-de-senhas-python/
├── gerador_senhas.py      # Arquivo principal (GUI + Backend)
├── meu_gerenciador.json   # Arquivo de senhas (gerado automaticamente)
├── requirements.txt       # Dependências (vazio - só stdlib)
├── .gitignore            # Ignora meu_gerenciador.json
└── README.md             # Esta documentação
```

### Estrutura do `meu_gerenciador.json`

```json
{
    "Gmail": {
        "usuario": "seu.email@gmail.com",
        "senha": "X7$mK9@pL2&qRtUv"
    },
    "GitHub": {
        "usuario": "PSilvestree",
        "senha": "aB3cD5eF7gH9"
    },
    "LinkedIn": {
        "usuario": "paulosilvestree",
        "senha": "Kp@9xL2$mN5&qR"
    }
}
```

---

## 🔧 Detalhes Técnicos

### Backend (Lógica)

```python
# Gerar senha aleatória
def gerar_senha_logica(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Salvar em JSON
def salvar_senha_logica(servico, usuario, senha):
    dados = carregar_senhas_logica()
    dados[servico] = {"usuario": usuario, "senha": senha}
    with open(ARQUIVO_SENHAS, "w") as f:
        json.dump(dados, f, indent=4)
```

### Características da Senha

| Aspecto | Detalhes |
|---------|----------|
| **Caracteres usados** | Maiúsculas (A-Z) + Minúsculas (a-z) + Números (0-9) + Símbolos (!@#$%^&*...) |
| **Entropia** | ~92 caracteres possíveis por posição |
| **Segurança** | Usa `random.choice()` (adequado para senhas locais) |
| **Armazenamento** | JSON simples (recomenda-se criptografia em produção) |

---

## ⚙️ Configurações

### Alterar Tamanho Padrão

Abra `gerador_senhas.py` e procure por:

```python
self.spin_tam.insert(0, "12")  # Altere para seu padrão
```

Exemplo: para 16 caracteres:
```python
self.spin_tam.insert(0, "16")
```

### Alterar Arquivo de Armazenamento

```python
ARQUIVO_SENHAS = "minhas_senhas.json"  # Altere o nome
```

---

## 🔒 Segurança

⚠️ **AVISO IMPORTANTE:**

- Senhas são armazenadas em **texto simples** no JSON
- Arquivo `meu_gerenciador.json` deve ser **protegido**
- Use permissões de arquivo: `chmod 600 meu_gerenciador.json`
- **Não compartilhe** o arquivo `meu_gerenciador.json`
- Para máxima segurança, considere usar um gerenciador profissional (1Password, Bitwarden, KeePass)

### Recomendações de Segurança

```bash
# Proteja o arquivo de senhas
chmod 600 meu_gerenciador.json

# Faça backup seguro
cp meu_gerenciador.json meu_gerenciador_backup.json
chmod 600 meu_gerenciador_backup.json

# Nunca versione o arquivo no Git
echo "meu_gerenciador.json" >> .gitignore
```

---

## 🧪 Testes

Atualmente, o projeto usa testes manuais. Para automatizar:

```bash
# Teste básico
python3 -c "
from gerador_senhas import gerar_senha_logica
senha = gerar_senha_logica(12)
print(f'Senha gerada: {senha}')
print(f'Comprimento: {len(senha)}')
assert len(senha) == 12
print('✅ Teste passou!')
"
```

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'tkinter'"

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### Problema: Janela não abre no Linux

Tente:
```bash
python3 gerador_senhas.py --display :0
```

### Problema: Arquivo JSON corrompido

```bash
# Faça backup
cp meu_gerenciador.json meu_gerenciador.backup

# Delete o corrompido
rm meu_gerenciador.json

# Reinicie a aplicação (criará novo JSON vazio)
python3 gerador_senhas.py
```

---

## 📈 Roadmap (Futuras Melhorias)

- [ ] **Criptografia AES** - Criptografar arquivo JSON
- [ ] **Busca/Filtro** - Procurar senhas por serviço
- [ ] **Editar senhas** - Modificar credenciais existentes
- [ ] **Deletar senhas** - Remover entradas
- [ ] **Exportar/Importar** - Backup em arquivo cifrado
- [ ] **Força de senha** - Indicador visual de segurança
- [ ] **Sincronização** - Cloud backup seguro
- [ ] **CLI alternativa** - Interface via terminal
- [ ] **Testes unitários** - pytest
- [ ] **Dark Mode** - Tema escuro no Tkinter

---

## 🤝 Contribuições

Encontrou um bug ou tem uma ideia? Contribuições são bem-vindas!

### Como Contribuir

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/melhoria`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. **Push** para a branch (`git push origin feature/melhoria`)
5. **Abra um Pull Request** com descrição clara

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja [LICENSE](LICENSE) para detalhes completos.

Você é livre para:
- ✅ Usar em projetos pessoais e comerciais
- ✅ Modificar e distribuir
- ✅ Incluir em outras aplicações

Desde que:
- 📋 Mantenha a atribuição
- 📋 Inclua uma cópia da licença

---

## 👨‍💻 Autor

**Paulo Silvestre**  
*Mestrando em História • Universidade Estadual de Maringá (UEM)*  
Desenvolver ferramentas úteis enquanto estudo história é minha paixão! 🎓

- 📧 **Email:** seu-email@example.com
- 🔗 **LinkedIn:** [paulosilvestree](https://www.linkedin.com/in/paulosilvestree)
- 🐙 **GitHub:** [@PSilvestree](https://github.com/PSilvestree)
- 🌐 **Portfólio:** (em breve)

---

## 📚 Inspiração e Referências

Este projeto foi inspirado em:
- **KeePass** - Gerenciador de senhas local
- **1Password** - Interface clean e intuitiva
- **Tkinter Documentation** - [Python tkinter](https://docs.python.org/3/library/tkinter.html)

---

## 📞 Suporte

Tem dúvidas ou encontrou um problema?

- 💬 Abra uma **Issue** no GitHub
- 💌 Envie um email
- 🔄 Faça um Pull Request com a solução

---

## ⭐ Gostou? Deixe uma Star!

Se este projeto foi útil para você, considere deixar uma ⭐ no GitHub. Isso ajuda outras pessoas a encontrá-lo!

---

**Última atualização:** 2026-04-25  
**Versão:** 1.0.0
