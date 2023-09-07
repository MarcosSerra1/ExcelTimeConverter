# Conversor de Horas para Horas Decimais em Planilha Excel

Este é um script em Python que lê uma planilha Excel, converte horas e minutos em horas decimais e, em seguida, adiciona esses valores de volta à planilha em uma coluna chamada "Horas Decimais". O script usa a biblioteca `openpyxl` para manipular a planilha.

## Como Usar

1. Certifique-se de ter a biblioteca `openpyxl` instalada. Você pode instalá-la usando o seguinte comando:

    ```bash
    pip install openpyxl
    ```

2. Coloque a planilha Excel que deseja processar no mesmo diretório do script ou forneça o caminho correto para a planilha na linha `planilha = openpyxl.load_workbook('CONVERSAO_HORAS_DECIMAIS.xlsx')`.

3. Execute o script Python.

4. O script lerá a planilha, calculará as horas decimais usando a função `horasDecimais()`, adicionará os valores calculados à planilha na coluna "Horas Decimais" e salvará a planilha atualizada com um nome diferente (no exemplo, 'CONVERSAO_HORAS_DECIMAIS_atualizado.xlsx').

5. O cabeçalho "Horas Decimais" será adicionado à primeira linha da coluna.

## Observações

- Certifique-se de que a planilha de entrada ('CONVERSAO_HORAS_DECIMAIS.xlsx' no exemplo) tenha colunas chamadas 'Horas' e 'Minutos' para que o script possa ler os valores corretamente.

- Este código assume que a planilha de saída será salva com um nome diferente ('CONVERSAO_HORAS_DECIMAIS_atualizado.xlsx' no exemplo) para evitar a sobregravação da planilha original.

- Personalize os nomes dos arquivos e as colunas conforme necessário para sua planilha específica.

# Autores

| [<img src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/marcosserra1)
