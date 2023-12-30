import json
import requests
from openai import OpenAI

client = OpenAI(
  api_key='api-key'
)

targetUrl = 'https://books.toscrape.com/' # Target URL will always changes
response = requests.get(targetUrl)
html_text = response.text


completion = client.chat.completions.create(
  model="gpt-4-1106-preview", # Feel free to change the model to gpt-3.5-turbo-1106
  messages=[
    {"role": "system", "content": "You are a master at scraping and parsing raw HTML with beautiful soup and python."},
    {"role": "user", "content": html_text}
  ]
# completion = client.chat.completions.create(
#   model="gpt-4-1106-preview", # Feel free to change the model to gpt-3.5-turbo-1106
#   messages=[
#     {"role": "system", "content": "You are a master at scraping and parsing raw HTML."},
#     {"role": "user", "content": html_text}
#   ],
#   tools=[
#           {
#             "type": "function",
#             "function": {
#               "name": "parse_data",
#               "description": "Parse raw HTML data nicely",
#               "parameters": {
#                 'type': 'object',
#                 'properties': {
#                     'data': {
#                         'type': 'array',
#                         'items': {
#                             'type': 'object',
#                             'properties': {
#                                 'title': {'type': 'string'},
#                                 'rating': {'type': 'number'},
#                                 'price': {'type': 'number'}
#                             }
#                         }
#                     }
#                 }
#               }
#           }
#         }
#     ],
#    tool_choice={
#        "type": "function",
#        "function": {"name": "parse_data"}
#    }
# )

# # Calling the data results
# argument_str = completion.choices[0].message.tool_calls[0].function.arguments
# argument_dict = json.loads(argument_str)
# data = argument_dict['data']

# # Print in a nice format
# for book in data:
#     print(book['title'], book['rating'], book['price']) 
