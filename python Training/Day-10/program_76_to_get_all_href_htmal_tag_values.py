from bs4 import BeautifulSoup as company

html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>Welcome to brad-sol company</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Brad Contech Solutions Private Limited
We, at BRADSOL, design industry-specific technology solutions to assist our clients with their technology needs. 
With the fast changing technology trends and fast paced globalization there is a need for greater focus on core 
competencies and cutting edge technology. That’s where we assist businesses and organizations with technology solutions 
while allowing them to focus on their core competencies.We engage with our clients at various stages of the IT life 
cycle – IT Strategy formation, IT roll out, IT Support and IT revamping. We partner with them to understand their 
overall business – product/ service, unique service offerings and their end goal.
We execute the plan laid out diligently and dedicatedly until we meet our PROMISED DELIVERABLES.</p>
<p><a href="https://bradsol.com/">its all about Robotic Process Automation</a></p>
<p><a href="https://in.linkedin.com/company/bradsol">see linkedin page
w3resource.com</a></p>
</body>
</html>
"""
N = company(html_doc, 'html.parser')
print("href of the first <a> tag:")
print(N.find('a').attrs['href'])
