# Instalações globais

## Curl

```commandline
sudo snap install curl
```

## Pyenv
* Pré-requisito: Curl instalado

```commandline
curl https://pyenv.run | bash
```

```commandline
nano .bashrc
```


* Cole a seguintes linhas no arquivo e salve:

```
# Load pyenv automatically by appending
# the following to 
# ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
# and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"

# Restart your shell for the changes to take effect.

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"
```
* Feche e abre o terminal novamente ou use o comando:
```commandline
source ~/.bashrc
```

## Observação

* Caso dê erro na instalação do python, instale as seguintes libs:

```commandline
sudo apt update
sudo apt install build-essential curl libbz2-dev libffi-dev liblzma-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev libxml2-dev libxmlsec1-dev llvm make tk-dev wget xz-utils zlib1g-dev
```
# Pipx

```commandline
pip install pipx
pipx ensurepath
```

# Poetry

* Após rodar o seguinte comando, reabra o terminal.
```commandline
pipx install poetry
```
```commandline
poetry new code_problems
```
```commandline
pyenv local 3.12.9
```


# Ignr (opcional)

```commandline
pipx install ignr
```

## Gerenciando múltiplas versões do python com pyenv

* Pré-requisito: Pyenv instalado.
* Instalando uma versão específica do python
```commandline
pyenv update
pyenv install 3.12:latest
```

## Criando o ambiente virtual

* O comando a seguir precisa ser executado na pasta onde contém o arquivo pyproject.toml

```commandline
poetry install
```
Exibe o comando para ativar o ambiente virtual
```commandline
poetry env activate
```
Para ativar, você pode digitar o comando printado pelo comando logo acima ou então pode usar em conjunto com o comando eval para já ativá-lo:
```commandline
eval $(poetry env activate)
```

## Configurando o pycharm

```
Add new interpreter... > Add local interpreter
Type: Poetry
Base python: ~/.pyenv/versions/3.12.9/bin/python
Path to poetry: {YOUR_HOME}/.local/bin/poetry
```

## Instalando ruff, taskipy, pytest
```commandline
poetry add --group dev ruff
```
```commandline
poetry add --group dev pytest pytest-cov
```
```commandline
poetry add --group dev taskipy
```

### Fonte

* [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)