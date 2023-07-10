from vertexai.preview.language_models import ChatModel
import vertexai
import json  
from google.oauth2 import service_account
import google.cloud.aiplatform as aiplatform
from vertexai.preview.language_models import InputOutputTextPair
# Load the service account json file
# Update the values in the json file with your own
with open(
    "service_account.json"
) as f:  # replace 'service_account.json' with the path to your file if necessary
    service_account_info = json.load(f)

my_credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

# Initialize Google AI Platform with project details and credentials
aiplatform.init(
    credentials=my_credentials,
)

with open("service_account.json", encoding="utf-8") as f:
    project_json = json.load(f)
    project_id = project_json["project_id"]


# Initialize Vertex AI with project and location
vertexai.init(project=project_id, location="us-central1")

def vertexAI(human_msg="Hi"):
    """
    Receives a message from the user, processes it, and returns a response from the model.
    """
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat(  # Initialize the chat with model
        context = """You are a personal trainer. I will provide you with all the information needed about an individual looking to become fitter, stronger and healthier through physical training, and your role is to devise the best plan for that person depending on their current fitness level, goals and lifestyle habits. You should use your knowledge of exercise science, nutrition advice, and other relevant factors in order to create a plan suitable for them. My first request is "I need help designing an exercise program for someone who wants to lose weight. You should be able to provide suggestions to users regarding their exercise routines, diet plans, etc. according to the users’ fitness goals.""",
        examples = [InputOutputTextPair(input_text="Can you help me design an exercise program to improve my overall fitness?",output_text="Sure, I'd be happy to help. Can you tell me a little bit about your current fitness level and your fitness goals?"),
                    InputOutputTextPair(input_text="I need help designing a workout plan for weight loss.", output_text="Absolutely! Monday: Warm-up: 5 minutes of brisk walking Cardiovascular exercise: 30 minutes of moderate-intensity cycling or jogging Strength training: 3 sets of 12 reps of squats, lunges, push-ups, and bicep curls Cool-down: 5 minutes of stretching Tuesday: Rest day Wednesday: Warm-up: 5 minutes of jumping jacks or rope jumping Cardiovascular exercise: 30 minutes of high-intensity interval training (HIIT) on the treadmill or elliptical machine Strength training: 3 sets of 12 reps of deadlifts, bench press, tricep dips, and lateral raises Cool-down: 5 minutes of stretching Thursday: Rest day Friday: Warm-up: 5 minutes of jumping jacks or rope jumping Cardiovascular exercise: 30 minutes of moderate-intensity swimming or rowing Strength training: 3 sets of 12 reps of step-ups, pull-ups, shoulder presses, and planks Cool-down: 5 minutes of stretching Saturday: Rest day Sunday: Warm-up: 5 minutes of brisk walking Cardiovascular exercise: 30 minutes of low-impact aerobics or yoga Strength training: 3 sets of 12 reps of calf raises, leg curls, crunches, and reverse flies Cool-down: 5 minutes of stretching")], 
        temperature= 0.8,
        max_output_tokens= 1024,
        top_p= 0.8,
        top_k= 40
    )
   
    # Send the human message to the model and get a response
    response = chat.send_message(human_msg)
    # Return the model's response
    return response.text