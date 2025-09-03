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
element = soup.select(".special")[0] # returns a list, by [0] returns the 1st item
print(element)
print(element.get_text())  # get_text() return what's inside
print(element.name)  # name returns a tag such as div / li / h3 etc
print(element.attrs) # returns a dictionary of all attributesprint(element.get_text())  # get_text() return what's inside
