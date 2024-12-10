import wikipediaapi

# Initialize the Wikipedia API with a user-agent
wiki = wikipediaapi.Wikipedia(
    language="en", 
    user_agent="YourAppName/1.0 (your-email@example.com)"
)

# Fetch the article
topic = "Machine Learning"
article = wiki.page(topic)

if article.exists():
    print(f"Title: {article.title}\n")
    print(article.text) 
    
    with open(f"{topic.replace(' ', '_')}.txt", "w", encoding="utf-8") as file:
        file.write(article.text)
    
else:
    print(f"The article '{topic}' does not exist.")
