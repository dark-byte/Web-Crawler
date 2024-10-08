<h1 align="center" id="title">Distributed Web Link Crawling Tool</h1>

<p align="center"><img src="https://socialify.git.ci/dark-byte/Web-Crawler/image?language=1&amp;owner=1&amp;name=1&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">This project implements a recursive web crawler that estimates the number of links on a specified domain and retrieves those links efficiently. Leveraging Python's requests and BeautifulSoup libraries it traverses web pages to gather link data up to a specified depth. The tool features a spinner animation to enhance user experience during link estimation and integrates a progress bar to visualize the crawling process. Ideal for web scraping enthusiasts and developers looking to analyze web structures or build data aggregation tools.</p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Repository:</p>

```
git clone https://github.com/dark-byte/Web-Crawler
```

<p>2. Create a Virtual Environment (Optional but recommended):</p>

```
python -m venv venv
```

```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

<p>4. Install Required Packages: Ensure you have pip installed then run:</p>

```
pip install -r requirements.txt
```

<p>5. Run the Crawler: After installation you can run the web crawler using:</p>

```
python your_script_name.py
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python: The primary programming language for implementing the web crawler.
*   Requests: A library for making HTTP requests to fetch web page content.
*   BeautifulSoup: A library for parsing HTML and extracting data from web pages.
*   Threading: Python's threading module for handling concurrent operations such as spinner animation during link estimation
*   TQDM: A library for displaying progress bars in the console enhancing user experience during crawling.