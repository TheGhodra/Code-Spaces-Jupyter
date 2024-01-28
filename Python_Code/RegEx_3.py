import re

def extract_html_tags(html_content):
    tag_pattern = r'<.*?>'
    tags = re.findall(tag_pattern, html_content)
    return tags

if __name__ == "__main__":
    html_content = """
    <html>
        <head>
            <title>Beispiel HTML</title>
        </head>
        <body>
            <h1>Willkommen!</h1>
            <p>Dies ist ein Beispieltext.</p>
            <a href="https://www.example.com">Besuchen Sie unsere Website</a>
        </body>
    </html>
    """

    extracted_tags = extract_html_tags(html_content)

    if extracted_tags:
        print("Extrahierte HTML-Tags:")
        for tag in extracted_tags:
            print(tag)
    else:
        print("Keine HTML-Tags gefunden.")