<h1 align="center">
codificador-alfabetico
</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Language&message=Python&color=blue&style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
  <img src="https://img.shields.io/static/v1?label=STATUS&message=COMPLETED&color=green&style=for-the-badge"/>
</p>

---

# :star2: Sumário

- [Introdução](#introdução)
- [Demonstração](#demonstração)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplos](#exemplos)
- [FAQ / Perguntas Frequentes](#faq--perguntas-frequentes)
- [Contribuição](#contribuição)
- [Boas Práticas](#boas-práticas)
- [Recursos & Links Adicionais](#recursos--links-adicionais)
- [Licença](#licença)
- [Equipe](#equipe)

---

## :books: Introdução

Este projeto é um programa em Python projetado para realizar uma forma simples de "criptografia" textual. Sua principal função é converter cada letra de uma palavra ou frase em um número que representa sua posição no alfabeto. Por exemplo, a letra 'a' se transforma em '1', 'b' em '2', e assim sucessivamente até 'z' que vira '26'.

---

## :rocket: Demonstração

| Visualização de Entrada | Visualização de Saída |
|---|---|
| ![](https://github.com/user-attachments/assets/b099a3ce-7993-451c-8b81-5c1c4bede602) | ![](https://github.com/user-attachments/assets/dce3ca60-2789-4d07-9407-d4a30ae0c0fd) |
> **Nota:**  
> Este programa foi desenvolvido para processar **apenas letras do alfabeto**.
> Caracteres que não são letras (como **espaços, números, acentos, ou símbolos** como `!, @, #`)
> serão **ignorados** e não aparecerão no texto criptografado.

---

## :zap: Funcionalidades

- **Criptografar Texto**
- **Converte cada letra de um texto em sua posição numérica correspondente no alfabeto**
- **Tratamento de Letras**
- **Ignorar Não-Letras**
- **Automaticamente ignora quaisquer caracteres que não sejam letras**
- **Interface Amigável**
- **Compatibilidade de Sistema**

---

## :computer: Instalação

### Pré-requisitos

- [Python 3](python.org)

 
### Passo a Passo

1. **Clone este repositório:**
    ```bash
    git clone https://github.com/StellaKarolinaNunes/codificador-alfabetico
    ```

2. **Abra o Terminal (ou Prompt de Comando)::**
    ```bash
     cd codificador-alfabetico
    ```

3. **Execute :**
    ```bash
    python3 criptografador.py
    ```

> **Dica:**  
> Certifique-se de ter o Python 3 instalado em seu sistema.

---

## :wrench: Uso

- Execute o Script: Basta rodar o arquivo Python no seu terminal.
- Insira o Texto: O programa vai pedir para você digitar o texto que quer "criptografar".
- Veja o Resultado: Após a entrada, o texto criptografado será exibido na tela, junto com o texto original para comparação.
 
### Principais Comandos no Script

- Entrada de texto: O usuário digita o texto que quer criptografar.
- Processamento (criptografia): O texto é convertido, letra por letra, para o número que corresponde à posição da letra no alfabeto.
- Exibição do resultado: Mostra o texto original e o texto criptografado lado a lado.
- Pausa para leitura: O programa espera alguns segundos para o usuário ver o resultado antes de encerrar.

---

## :bulb: Exemplos

**Criptografar texto:**  
Digite o texto, veja o resultado numérico.

**Resultado:**  
Ver como o texto "abc XYZ !" vira "123242526".

**Sair:**  
Finalizar o programa.

---

## :question: FAQ / Perguntas Frequentes

### 1. O que este programa faz exatamente??
Este programa converte letras do alfabeto em números correspondentes à sua posição.
Por exemplo, A = 1, B = 2, ..., Z = 26.

### 2. O programa diferencia letras maiúsculas e minúsculas?
Não. Todas as letras são tratadas igualmente (convertidas para minúsculas antes de criptografar).

### 3. Posso usar acentos ou letras como "ç"?
Não. O programa só considera letras de A a Z do alfabeto latino. Letras como "á", "ç", "ñ" são ignoradas no resultado final.

### 4. É possível descriptografar o texto depois?
Não neste projeto. O programa apenas criptografa (one-way).
Como caracteres repetidos (ex: "aa") geram o mesmo número (ex: "11"), a descriptografia exata não é possível sem contexto adicional.

### 5. O PDFTK é seguro?
Sim, é uma ferramenta open source amplamente utilizada para manipulação de PDFs.

### 6. Funciona em Windows, Linux e macOS??
Sim! A limpeza de tela (limpar_tela()) detecta automaticamente o sistema operacional.

### 7. Preciso instalar algo para rodar??
Não. Basta ter o Python 3 instalado. Nenhuma biblioteca extra é usada.

### 8. Como executo o programa?
vá até [Passo a Passo](#passo-a-passo)

### 9. Como contribuir com novas funcionalidades?
Veja a seção de contribuição abaixo!

### 10. Não encontrou sua dúvida aqui?
Abra uma [issue](https://github.com/StellaKarolinaNunes/codificador-alfabetico/issues/new) com sua dúvida ou sugestão.

---

## :handshake: Contribuição

Contribuições são bem-vindas!

1. [Leia o guia de contribuição](./CONTRIBUTING.md)
2. Faça um fork do repositório.
3. Crie uma branch:  
   `git checkout -b feature/seu-recurso`
4. Faça commits claros e objetivos.
5. Abra um Pull Request detalhado.

**Dicas para contribuir:**

- Explique sua motivação.
- Siga a organização do script.
- Teste suas alterações.

---

## :bookmark_tabs: Boas Práticas

- Código limpo e comentado.
- Mensagens de commit objetivas.
- Teste todas as funções antes de submeter PR.
- Atualize seu fork antes de abrir um PR.

---

## :link: Recursos & Links Adicionais

- [ PYTHON - Documentação](python.org/doc/)
- [Módulo os em Python](docs.python.org/3/library/os.html)
- [Módulo time em Python](docs.python.org/3/library/time.html)
- [Guia de Contribuição Open Source](opensource.guide/how-to-contribute/)
- [Tabela ASCII/Unicode](opensource.guide/how-to-contribute/)

---

## :page_facing_up: Licença

Este projeto está sob a [Licença MIT](./LICENSE).  
Sinta-se livre para usar, modificar e distribuir, sempre mantendo referência ao repositório original.

---

## :trophy: Equipe

**Desenvolvimento:**  

- [Stella Karolina Nunes Peixoto](https://github.com/StellaKarolinaNunes)

---

> _Projeto pessoal criado com o objetivo de treinar lógica de programação, manipulação de strings e interação com terminal usando Python. A aplicação simula uma criptografia simples, convertendo letras em números com base na posição no alfabeto_



