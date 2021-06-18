#! /usr/bin/env python3
from PIL import Image
from pathlib import Path

# image1 = Image.open(r'path where the image is stored\file name.png')
# im1 = image1.convert('RGB')
# im1.save(r'path where the pdf will be stored\new file name.pdf')

certificado = Path("certificado.png")
certificado_pdf = Path("certificado.pdf")

histoirco_verso = Path("histoirco verso.png")
histoirco_verso_pdf = Path("histoirco verso.pdf")

histoirco_frente = Path("hostorico frente.png")
histoirco_frente_pdf = Path("hostorico frente.pdf")

with Image.open(certificado) as img_file:
	conv = img_file.convert('RGB')
	conv.save(certificado_pdf)

with Image.open(histoirco_frente) as img_file:
	conv = img_file.convert('RGB')
	conv.save(histoirco_frente_pdf)

with Image.open(histoirco_verso) as img_file:
	conv = img_file.convert('RGB')
	conv.save(histoirco_verso_pdf)
