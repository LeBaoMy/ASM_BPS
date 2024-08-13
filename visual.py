import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('sales.csv')

# Hiển thị thông tin cơ bản về dữ liệu
print(df.head())
print(df.info())

# Chuyển đổi SaleDate thành kiểu dữ liệu datetime
df['SaleDate'] = pd.to_datetime(df['SaleDate'])


# 2. Biểu đồ số lượng bán theo kênh bán hàng
channel_sales = df.groupby('SaleChannel')['Quantity'].sum()
plt.figure(figsize=(8, 6))
channel_sales.plot(kind='bar')
plt.title('Số lượng bán theo kênh bán hàng')
plt.xlabel('Kênh bán hàng')
plt.ylabel('Số lượng bán')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 3. Biểu đồ phân phối phương thức thanh toán
payment_method_sales = df['PaymentMethod'].value_counts()
plt.figure(figsize=(8, 6))
payment_method_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Phân phối phương thức thanh toán')
plt.ylabel('')
plt.show()
