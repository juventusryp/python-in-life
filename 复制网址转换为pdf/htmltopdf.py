import pdfkit
import pyperclip

a=str(pyperclip.paste())

pdfkit.from_url(a, 'out.pdf')