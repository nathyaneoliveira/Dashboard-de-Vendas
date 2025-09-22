import pandas as pd
import matplotlib.pyplot as plt

# Dados de vendas (exemplo)
dados = {
    "Produto": ["Produto A", "Produto B", "Produto C", "Produto A", "Produto B", "Produto C"],
    "Data": ["2025-09-01", "2025-09-01", "2025-09-01", "2025-09-02", "2025-09-02", "2025-09-02"],
    "Quantidade": [10, 5, 8, 7, 3, 12],
    "Preço Unitário": [50, 30, 20, 50, 30, 20]
}

# Criar DataFrame
df = pd.DataFrame(dados)
df["Data"] = pd.to_datetime(df["Data"])
df["Total"] = df["Quantidade"] * df["Preço Unitário"]

# Total de vendas por produto
vendas_produto = df.groupby("Produto")["Total"].sum()
print("💰 Total de Vendas por Produto:")
print(vendas_produto)

# Total de vendas por data
vendas_data = df.groupby("Data")["Total"].sum()
print("\n📅 Total de Vendas por Data:")
print(vendas_data)

# Gráfico: Vendas por Produto
plt.figure(figsize=(8,5))
vendas_produto.plot(kind="bar", color="skyblue")
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Total Vendido (R$)")
plt.xticks(rotation=0)
plt.show()

# Gráfico: Vendas por Data
plt.figure(figsize=(8,5))
vendas_data.plot(kind="line", marker="o", color="green")
plt.title("Vendas ao Longo do Tempo")
plt.xlabel("Data")
plt.ylabel("Total Vendido (R$)")
plt.grid(True)
plt.show()
