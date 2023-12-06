def multilevel_index(documents, keys):
    dicci = {}

    for doc in documents:
        dic_actu = dicci
        for key in keys:
            nuevo_dic = dicci[key]

    return dicci


objects = [
    {"age": 16, "name": "Mateo", "last_name": "González", },
    {"age": 23, "name": "Arturo", "last_name": "González", },
    {"age": 16, "name": "Julián", "last_name": "Fernández", },
    {"age": 16, "name": "Diego", "last_name": "González"},
    {"age": 30, "name": "santiago", "last_name": "Diaz"},
]


resultado = multilevel_index(objects,  ["age", "last_name"])
print(resultado)
