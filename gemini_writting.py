from google import genai

client = genai.Client(api_key="AIzaSyAWLADt_GLIbUly7Y62Tsn4cwhlZMzK24Y")

response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25", contents="写一个操作系统的书籍目录，输出为markdown格式"
)
print(response.text)

