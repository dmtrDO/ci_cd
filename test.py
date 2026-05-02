
from bs4 import BeautifulSoup
from crawler import Crawler

def test_simple_word_filter():
    html = "<html>" \
                "<body>" \
                    "<h1>Привіт!</h1>" \
                    "<p>Це КРАУЛЕР і він працює.</p>" \
                "</body>" \
            "</html>"
    
    soup = BeautifulSoup(html, "lxml")
    
    result = Crawler._Crawler__filter_page(soup)

    assert "привіт" in result
    assert "краулер" in result
    assert "і" not in result
    assert "це" in result
    assert "працює" in result

