from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def check_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    issues = []

    # Check for broken <a> links
    for link in soup.find_all('a', href=True):
        url = link['href']
        if url.startswith('https'):
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                if response.status_code >= 400:
                    issues.append(f"Broken link: {url} (Status: {response.status_code})")
            except Exception as e:
                issues.append(f"Error checking link: {url} ({str(e)})")

    # Check for missing images
    for img in soup.find_all('img', src=True):
        url = img['src']
        if url.startswith('https'):
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                if response.status_code >= 400:
                    issues.append(f"Broken image: {url} (Status: {response.status_code})")
            except Exception as e:
                issues.append(f"Error checking image: {url} ({str(e)})")

    return issues

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    html = request.form['html_content']
    issues = check_links(html)
    return render_template('report.html', issues=issues)

if __name__ == '__main__':
    app.run(debug=True)