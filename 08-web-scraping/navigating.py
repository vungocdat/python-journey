from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="URF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special</li>
    <li class="special">This list item is also special</li>
    <li>This list item is not special</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""


soup = BeautifulSoup(html, "html.parser")
# tag = soup.body.contents[1].next_sibling.next_sibling # access the OL tag
# tag = soup.find(class_="super-special").parent # different way to access the OL tag using find
tag = soup.select("[data-example]")[1].find_previous_sibling() # accessing tag IL with select
print(tag)
