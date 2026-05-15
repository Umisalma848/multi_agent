from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient   ## we can fetch data using tavily client 
import os
from dotenv import load_dotenv
from rich import print  
load_dotenv()


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")) ## initialize tavily client with api key from environment variable

## 1st tool :- To fetch real-time data from tavily
@tool
def web_search(query: str) -> str:
    """
    searches for the given query using the Tavily API and returns the response as a string, titles, urls, snippets.
    """
    results = tavily.search(query=query, num_results=5)  ## we can specify the number of results we want to fetch
    
    out=[]
    for r in results ['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    return "\n----\n".join(out)  ## we can join the results with new lines for better readability   

##2nd tool :- To scrape the content of a webpage given its URL

@tool
def scrape_url(url: str) -> str:
    """
    Scrapes the clean text content of the given URL and returns the text content.
    """
    try:
        response = requests.get(url,timeout=8 , headers={'User-Agent': 'Mozilla/5.0'})  ## make a GET request to the URL
        soup = BeautifulSoup(response.text, 'html.parser')  ## parse the HTML content using BeautifulSoup
        for tag in soup(['script', 'style','nav', 'footer']):  ## remove script and style tags
            tag.decompose()
        return soup.get_text(separator="",strip= True)[:3000]  ## return the text content of the page
    except Exception as e:
        return f"could not fetch the content from the URL. Error: {str(e)}"
    