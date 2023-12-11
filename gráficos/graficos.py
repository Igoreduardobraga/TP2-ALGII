import pandas as pd
import matplotlib.pyplot as plt

try:
    data_christofides = pd.read_csv("resultados/resultados_christofides_oficial.csv", encoding='ISO-8859-1')
except Exception as e:
    error_christofides = str(e)
else:
    error_christofides = None

try:
    data_twice = pd.read_csv("resultados/resultados_twice_oficial.csv", encoding='ISO-8859-1')
except Exception as e:
    error_twice = str(e)
else:
    error_twice = None

# Verificando se os dados foram carregados corretamente ou se houve erros
data_christofides_head = data_christofides.head() if error_christofides is None else error_christofides
data_twice_head = data_twice.head() if error_twice is None else error_twice

# print(data_twice_head)

# Preparando os dados para a comparação
merged_data = pd.merge(data_christofides, data_twice, on="Nome do Teste", suffixes=('_christofides', '_twice'))

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 10))

# Custo
merged_data.plot(x='Nome do Teste', y=['Custo_christofides', 'Custo_twice'], kind='line', marker='o', ax=axes[0])
axes[0].set_title('Comparação de Custo')
axes[0].set_ylabel('Custo')
axes[0].set_xlabel(' ')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(True)

# Tempo de Execução
merged_data.plot(x='Nome do Teste', y=['Tempo de Execução_christofides', 'Tempo de Execução_twice'], kind='line', marker='o', ax=axes[1])
axes[1].set_title('Comparação de Tempo de Execução')
axes[1].set_ylabel('Tempo de Execução (segundos)')
axes[1].set_xlabel(' ')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(True)

# Memória
merged_data.plot(x='Nome do Teste', y=['Memória_christofides', 'Memória_twice'], kind='line', marker='o', ax=axes[2])
axes[2].set_title('Comparação de Uso de Memória')
axes[2].set_ylabel('Memória (MB)')
axes[2].set_xlabel(' ')
axes[2].tick_params(axis='x', rotation=45)
axes[2].grid(True)

# Ajustando layout
plt.tight_layout()

# Mostrando os gráficos
plt.show()