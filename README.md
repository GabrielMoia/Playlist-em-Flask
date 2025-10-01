### 🎵 Playlist com Flask

Este é um pequeno projeto em Python utilizando o Flask, que cria uma API simples para retornar uma lista de músicas.

---

### 🚀 Tecnologias usadas

Python 3

Flask

---

### 📌 Funcionalidades

Retorna uma playlist com músicas em formato JSON

Mostra também o total de músicas cadastradas

---

### ▶️ Como executar

Clone este repositório:

git clone https://github.com/seu-usuario/playlist-flask.git


´Acesse a pasta do projeto:´

cd playlist-flask


´Instale as dependências:´

pip install flask


´Execute o projeto:´

python app.py

📍 Endpoints

GET /playlist → Retorna a lista de músicas e o total.


```Json 

Exemplo de resposta:

{
  "playlist": [
    {
      "id": 1,
      "titulo": "Rumo a Goiania",
      "artista": "Leonardo"
    },
    {
      "id": 2,
      "titulo": "É o amor",
      "artista": "Zezé di Camargo e Luciano"
    }
  ],
  "total": 2
}
