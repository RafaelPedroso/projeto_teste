# Análise estatística de base de dados diabetes

Verificação da relação de casos de diabates com outros fatores.

![imagem](imagens/img_diabetes.jpg)

## Organização do projeto

```
├── .env               <- Arquivo de variáveis de ambiente (não versionar)
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto (MIT)
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── notebooks          <- Cadernos Jupyter.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── estatistica.py  <- Funções criados espeficicamente para esse projeto
|
├── referencias        <- Dicionários de dados
|
├── imagens
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone git@github.com:RafaelPedroso/projeto_teste.git
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o 'conda'

      ```bash
      conda env create -f > ambiente.yml --name estatistica
      ```

## Um pouco mais sobre a base

[Clique aqui](referencias/01_dicionario_de_dados.md) para ver o dicionario de dados da base utilizada.

## Resumo os principais resultados

Durante o estudos foi identificado que há relação de diabetes entre N fatores