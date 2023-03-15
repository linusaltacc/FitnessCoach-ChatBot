import openai
from apikey import openai_api_key


def chatgpt(query="Hey"):
    prompt=f"""I want you to act as a personal trainer. I will provide you with all the information needed about an individual looking to become fitter, stronger and healthier through physical training, and your role is to devise the best plan for that person depending on their current fitness level, goals and lifestyle habits. You should use your knowledge of exercise science, nutrition advice, and other relevant factors in order to create a plan suitable for them. My first request is "I need help designing an exercise program for someone who wants to lose weight. You should be able to provide suggestions to users regarding their exercise routines, diet plans, etc. according to the users’ fitness goals. Human: """ + query + " AI: """[0]
    openai.api_key = openai_api_key
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content    
