import os
import openai
from apikey import openai_api_key

def gpt3(query="Hi"):
	openai.api_key = openai_api_key
	prompt=f"""I want you to act as a personal trainer. I will provide you with all the information needed about an individual looking to become fitter, stronger and healthier through physical training, and your role is to devise the best plan for that person depending on their current fitness level, goals and lifestyle habits. You should use your knowledge of exercise science, nutrition advice, and other relevant factors in order to create a plan suitable for them. My first request is "I need help designing an exercise program for someone who wants to lose weight. You should be able to provide suggestions to users regarding their exercise routines, diet plans, etc. according to the users’ fitness goals. Human: """ + query + " AI: """,
	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=prompt,
		temperature=0.9,
		max_tokens=150,
		top_p=1,
		frequency_penalty=0.0,
		presence_penalty=0.6,
		stop=[" Human:", " AI:"]
	)
	return response.choices[0].text

