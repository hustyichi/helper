from helper.search import search
from helper.search import web_request
from helper.search import web_selenium


def test_search_content():
    ret = search.duckduckgo_search("四岁女孩童书推荐")
    for d in ret:
        print(f"---------> search {d['href']}: ")

        content = web_request.scrape_text(d["href"])
        if content.startswith("Error"):
            print(f"web request got err: {content}")
            content = web_selenium.scrape_text_with_selenium(d["href"])

        print(content)

if __name__ == "__main__":
    test_search_content()