
import json


inv = 'MXL121548'
# Your JSON data
json_data = {
    "doctoRelacionados": [
        {                    "IdDocumento": "74b37550-bff2-41c7-99a2-074f8230c93b",
                    "MonedaDR": "MXN",
                    "folio_facura": inv,
                    "NumParcialidad": "1",
                    "ImpSaldoAnt": "504.6",
                    "ImpPagado": "504.6",
                    "ImpSaldoInsoluto": "0",
                    "ObjetoImpDR": "02",
                    "EquivalenciaDR": "1"
        }
    ]
}

# Save the updated dictionary to a JSON file
file_path = "data.json"

with open(file_path, 'w') as json_file:
    json.dump(json_data, json_file)

print(f"Data appended and saved to {file_path}")




