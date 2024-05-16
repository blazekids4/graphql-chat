from openai import OpenAI
from unittest.mock import patch
import dotenv
import os

dotenv.load_dotenv()

# Sample Data
sample_data = {
    "user_details": {
        "data": {
            "getUser": {
                "id": "12345",
                "name": "John Doe",
                "email": "john.doe@example.com",
                "role": "Admin"
            }
        }
    },
    "project_details": {
        "data": {
            "getProject": {
                "id": "54321",
                "title": "AI Development",
                "description": "Developing AI models for various applications",
                "status": "In Progress"
            }
        }
    },
    "task_list": {
        "data": {
            "getTasks": [
                {
                    "id": "1",
                    "title": "Task 1",
                    "status": "Completed"
                },
                {
                    "id": "2",
                    "title": "Task 2",
                    "status": "In Progress"
                },
                {
                    "id": "3",
                    "title": "Task 3",
                    "status": "Pending"
                }
            ]
        }
    }
}

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the function to generate GraphQL query using OpenAI
def construct_query(user_input):
    schema_details = """
    type Query {
        getUser(id: ID!): User
        getProject(id: ID!): Project
        getTasks(projectId: ID!): [Task]
    }

    type User {
        id: ID!
        name: String!
        email: String!
        role: String!
    }

    type Project {
        id: ID!
        title: String!
        description: String!
        status: String!
    }

    type Task {
        id: ID!
        title: String!
        status: String!
    }
    """
    prompt = f"Convert the following natural language request into a GraphQL query: '{user_input}'"
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant who is an expert at converting a natural language question into a GraphQL query. Here is the schema you are working with: {schema_details}"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return completion.choices[0].message.content.strip()    

# Mock the GraphQL API response for testing
def mock_query_graphql_api(graphql_query):
    if "getUser" in graphql_query:
        return sample_data["user_details"]
    elif "getProject" in graphql_query:
        return sample_data["project_details"]
    elif "getTasks" in graphql_query:
        return sample_data["task_list"]
    else:
        return {"error": "Query not recognized"}

# Process the GraphQL response
def process_response(graphql_response):
    if "error" in graphql_response:
        return {"error": graphql_response["error"]}
    
    data = graphql_response.get('data')
    if not data:
        return {"error": "No data found"}
    
    return data

# Format the response for the chatbot
def format_for_chatbot(data):
    if "error" in data:
        return f"Error: {data['error']}"

    # Customize the formatting based on the expected structure of the GraphQL response
    formatted_response = ""
    for key, value in data.items():
        formatted_response += f"{key}:\n"
        if isinstance(value, list):
            for item in value:
                formatted_response += f"  - {item}\n"
        else:
            formatted_response += f"  {value}\n"
    return formatted_response

# Main function to handle the chatbot interaction
def handle_chatbot_interaction(user_input):
    graphql_query = construct_query(user_input)
    graphql_response = mock_query_graphql_api(graphql_query)
    data = process_response(graphql_response)
    chatbot_response = format_for_chatbot(data)
    return chatbot_response

# Example test cases
test_cases = [
    "Get details of the user with ID 12345",
    "Fetch details about the latest project titled 'AI Development'",
    "List all tasks and their statuses"
]

# Run test cases
for test_case in test_cases:
    print(f"User Input: {test_case}")
    chatbot_response = handle_chatbot_interaction(test_case)
    print(f"Chatbot Response:\n{chatbot_response}\n")
