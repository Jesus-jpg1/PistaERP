# PistaERP — Sistema de Gestão para Oficinas Mecânicas

O **PistaERP** é um sistema ERP voltado para **oficinas mecânicas e lojas de autopeças**, com foco em ser uma **alternativa acessível** para negócios que ainda não utilizam uma ferramenta digital para organização, controle de estoque e atendimento ao cliente.

**Aviso:** Este projeto é um **trabalho acadêmico** da disciplina de **Engenharia de Software II** e não deve ser utilizado em ambientes de produção sem as devidas validações técnicas.

---

##  Funcionalidades previstas

- Cadastro de clientes, veículos, mecânicos, fornecedores e peças
- Controle de estoque de peças
- Gestão de ordens de serviço
- Relatórios simples
- Painel administrativo
- API REST com autenticação e filtros de busca

---

##  Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- SQLite

---

##  Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/Jesus-jpg1/PistaERP.git
```

2. Acesse o diretório do projeto:

```bash
cd PistaERP
```

3. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Realize as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crie um superusuário:

```bash
python manage.py createsuperuser
```

7. Inicie o servidor:

```bash
python manage.py runserver
```

8. Acesse no navegador:

```
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/api/
```

---

##  Estrutura do Projeto

```
PistaERP/
│
├── config/              # Configurações do projeto Django
├── apps/                # Aplicações do sistema
│   ├── cliente/
│   ├── veiculo/
│   ├── peca/
│   ├── fornecedor/
│   └── core/
│
├── media/               # Arquivos enviados (uploads)
├── static/              # Arquivos estáticos (css, js)
├── venv/                # Ambiente virtual
├── manage.py
├── requirements.txt
└── README.md
```

---

##  Status do Projeto

* [x] API de Cliente
* [x] API de Veículo
* [x] API de Fornecedor
* [x] API de Peça
* [ ] API de Ordem de Serviço
* [ ] Relacionamentos completos (Ex: OS x Peça)
* [ ] Documentação da API (ex: Swagger)