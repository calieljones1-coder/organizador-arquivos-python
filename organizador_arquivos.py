import os
import shutil

Downloads_folden_path = os.path.join(os.path.expanduser("~"), "Downloads")
print(Downloads_folden_path)

categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audios": [".mp3", ".wav", ".ogg"]
}

Arquivos = os.listdir(Downloads_folden_path)

for item in Arquivos:
    caminho_completo = os.path.join(Downloads_folden_path, item)

    if os.path.isdir(caminho_completo):
        continue

    nome, extensao = os.path.splitext(item)
    extensao = extensao.lower()

    print(f"arquivo: {item}, Extensao: {extensao}")

    pasta_escolhida = "Outros"

    for nome_pasta, lista_extensoes in categorias.items():
        if extensao in lista_extensoes:
            pasta_escolhida = nome_pasta
            break

    pasta_destino = os.path.join(Downloads_folden_path, pasta_escolhida)
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_destino = os.path.join(pasta_destino, item)

    contador = 1
    while os.path.exists(caminho_destino):
        novo_nome = f"{nome} ({contador}){extensao}"
        caminho_destino = os.path.join(pasta_destino, novo_nome)
        contador += 1

    shutil.move(caminho_completo, caminho_destino)
    print(f"movido: {item} para {pasta_escolhida}/")