import pandas as pd

# Bước 1: Đọc dữ liệu từ file CSV
df = pd.read_csv('Customer_Table.csv')

# Bước 2: Kiểm tra dữ liệu trống
print("Số lượng dữ liệu trống trong mỗi cột:")
print(df.isnull().sum())

# Bước 3: Xử lý dữ liệu trống
df.fillna({
    'CustomerID': 'Unknown',
    'FirstName': 'Unknown',
    'LastName': 'Unknown',
    'DateOfBirth': '1900-01-01',
    'Email': 'noemail@example.com',
    'Phone': '000-000-0000',
    'Address': 'Unknown',
    'City': 'Unknown',
    'State': 'Unknown',
    'Country': 'Unknown'
}, inplace=True)

# Bước 4: Xử lý dữ liệu lỗi
# Kiểm tra kiểu dữ liệu
print("\nKiểu dữ liệu của từng cột:")
print(df.dtypes)

# Chuyển đổi cột DateOfBirth sang định dạng ngày tháng
df['DateOfBirth'] = pd.to_datetime(df['DateOfBirth'], errors='coerce')  # Chuyển đổi thành datetime

# Chuyển đổi ngày tháng sang định dạng YYYY-MM-DD
df['DateOfBirth'] = df['DateOfBirth'].dt.strftime('%Y-%m-%d')

# Xử lý dữ liệu lỗi trong số điện thoại
df['Phone'] = df['Phone'].astype(str).str.replace(r'\D', '', regex=True)

# Bước 5: Kiểm tra lại dữ liệu sau khi xử lý
print("\nDữ liệu sau khi xử lý:")
print(df.head())

# Bước 6: Lưu dữ liệu đã xử lý vào file mới
df.to_csv('cleaned_file.csv', index=False)

print("\nDữ liệu đã được lưu vào 'cleaned_file.csv'")
