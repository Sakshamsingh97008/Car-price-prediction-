import json

filename = "car price prediction.ipynb"

with open(filename, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        # Don't add if already there
        if not any("import pandas" in line for line in cell['source']):
            cell['source'].insert(0, "import pandas as pd\n")
        break

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
