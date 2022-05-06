from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser") 
print("\ntype(soup):\n" + str(type(soup)))
d = soup.select("[data-example]")
print("\nbody:\n" + str(soup.body))
print("\n d data-example:\n" + str(d))

d = soup.find_all("li")
print("\n d  li :\n" + str(d))

d = soup.find(id="first")
print("\n d  id=first :\n" + str(d))

d = soup.select("#first")
print("\n d  id=#first :\n" + str(d))

d = soup.select(".special")
print("\n d  .special :\n" + str(d))


# CSS selectors
# Select id of foo:
# #foo

# Class of bar:
# .bar

# Children:
# Div  > p

# Descendents:
# Div p
