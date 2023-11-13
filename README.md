# Conversor de Horas para Horas Decimais em Planilha Excel

Este é um aplicativo em Python que lê uma planilha Excel, converte horas e minutos em horas decimais e, em seguida, adiciona esses valores de volta à planilha em uma coluna chamada "valor". O script usa a biblioteca `openpyxl` para manipular a planilha.

## Como Usar

1. Certifique-se de ter as bibliotecas `openpyxl` e `tkinter` instaladas. Você pode instalá-las usando os seguintes comandos:

    ```bash
    pip install openpyxl
    pip install tk
    ```

2. Execute o script Python.

3. Uma interface gráfica será exibida, permitindo que você selecione a planilha Excel de entrada e escolha o local para salvar a planilha atualizada.

4. Clique no botão "Converter Horas" para processar a planilha.

5. O script lerá a planilha, calculará as horas decimais usando a função `horas_decimais()`, adicionará os valores calculados à planilha na coluna "valores" e salvará a planilha atualizada no local escolhido.

6. Um executável autônomo também está disponível na pasta 'CONVERSAO-DE-HORAS-PARA-HORAS-DECIMAIS.zip'.

## Observações

- Certifique-se de que a planilha de entrada tenha colunas chamadas 'Horas' e 'Minutos' para que o script possa ler os valores corretamente.

- Personalize os nomes dos arquivos conforme necessário para sua planilha específica.

- O script agora inclui uma interface gráfica que facilita a seleção da planilha de entrada e o local de saída.

# Autores

| [<img src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/marcosserra1)
