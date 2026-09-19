# 🤖 AI Customer Support System

Sistema de suporte ao cliente dirigido por **agentes de IA**, construído com Django. A ideia central é a criação de três agentes que colaboram entre si em uma esteira de atendimento, cada um responsável por uma etapa específica do processo:

| Agente | Papel |
|---|---|
| **Support (Maya)** | Realiza o atendimento inicial ao cliente. Quando a solicitação exige uma decisão mais complexa, repassa o caso para o Manager |
| **Manager** | Possui privilégios de decisão. Antes de decidir, envia o contexto do pedido para o Risk avaliar possíveis fraudes |
| **Risk** | Analisa os dados do atendimento (dados do pedido, por exemplo) e nega solicitações infundadas |

> 📚 Anotações de estudo sobre os conceitos de AI Agents, Agentic AI, Tools e Agent Loop utilizados neste projeto estão documentadas em [`annotations.md`](./annotations.md).

---

## 🧱 Stack

- **Python 3.12**
- **Django 6.1**
- **MySQL 8** (via Docker)
- **PyMySQL** como driver de conexão com o MySQL
- **python-dotenv** para gerenciamento de variáveis de ambiente

## 📂 Estrutura do projeto

```text
.
├── core/                # Configurações do projeto Django (settings, urls, wsgi/asgi)
├── annotations.md        # Anotações de estudo sobre AI Agents
├── docker-compose.yaml   # Sobe o banco MySQL em container
├── .env.exemple          # Modelo das variáveis de ambiente
├── manage.py
└── requirements.txt
```

---

## 🚀 Modo de usar

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd ai-customer-support-system
```

### 2. Configurar o `.env`

Copie o arquivo de exemplo e preencha com seus próprios valores:

```bash
cp .env.exemple .env
```

```text
# Django configurations
SECRET_KEY=YOUR_KEY
DEBUG=False
ALLOWED_HOSTS=localhost

# Database configuration
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=curso_django
MYSQL_USER=django
MYSQL_PASSWORD=django
```

### 3. Criar o ambiente virtual e instalar as dependências

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 4. Subir o banco de dados

Este projeto utiliza Docker para o MySQL. Com o Docker instalado, na raiz do repositório:

```bash
docker compose up -d
```

Verifique se o container subiu corretamente com `docker ps`.

Para confirmar a conexão via terminal:

```bash
python manage.py dbshell
```

Se aparecer o prompt `mysql>`, deu tudo certo. Esse comando exige o client do MySQL instalado:

```bash
sudo apt install mysql-client
```

Alternativamente, você pode usar o **DBeaver** (ou outro client gráfico) para visualizar o banco criado pelo Docker. Ao configurar a conexão, escolha **MySQL** e preencha:

- **Server Host:** `localhost`
- **Database:** valor de `MYSQL_DATABASE` no seu `.env`
- **User / Password:** utilize o usuário **root** com a senha de `MYSQL_ROOT_PASSWORD` para acesso administrativo via client gráfico

> ℹ️ **Por que `localhost` no client gráfico e `127.0.0.1` no Django?** Ambos resolvem para o mesmo host local; a diferença é apenas de convenção, o Django está configurado explicitamente com `127.0.0.1` para evitar ambiguidades de resolução de DNS/socket em alguns ambientes.
>
> ℹ️ **Por que o Django usa o usuário `django` e não o `root`?** Por segurança, o usuário da aplicação tem apenas os privilégios necessários para operar o banco, reduzindo o impacto de um eventual incidente.

### 5. Aplicar as migrations e rodar o servidor

```bash
python manage.py migrate
python manage.py runserver
```

O projeto estará disponível em `http://127.0.0.1:8000/`.

---

