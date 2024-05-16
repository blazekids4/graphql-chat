# GraphQL Chatbot

This project is a chatbot that uses OpenAI's GPT-4 model to convert natural language queries into GraphQL queries, execute them, and return the results.

## Code Overview

The `app.py` file contains the main logic of the chatbot. Here's a breakdown of what each part of the code does:

### Sample Data

The `sample_data` dictionary contains mock data that simulates the responses from a GraphQL API. It includes details about a user, a project, and a list of tasks.

### OpenAI Client Initialization

The OpenAI client is initialized with an API key, which is retrieved from an environment variable.

### Construct Query Function

The `construct_query` function takes a user's input in natural language and uses the OpenAI client to generate a corresponding GraphQL query. The function uses a chat model (`gpt-4o`) and provides a system message to set the context for the assistant.

### Mock Query GraphQL API Function

The `mock_query_graphql_api` function simulates the execution of a GraphQL query. It checks the query string to determine which part of the `sample_data` to return.

### Process Response Function

The `process_response` function processes the response from the `mock_query_graphql_api` function. It checks for errors and extracts the data from the response.

### Format for Chatbot Function

The `format_for_chatbot` function formats the data from the `process_response` function into a string that can be returned by the chatbot.

### Handle Chatbot Interaction Function

The `handle_chatbot_interaction` function is the main function that handles the chatbot interaction. It takes the user's input, constructs a GraphQL query, executes the query, processes the response, and formats the data for the chatbot.

### Test Cases

At the end of the file, there are some example test cases that demonstrate how to use the `handle_chatbot_interaction` function.

## Running the Code

To run the code, simply execute the `app.py` file. The test cases will be run and the chatbot's responses will be printed to the console.

## Future Work

This is a basic implementation of a chatbot that uses OpenAI to generate GraphQL queries. In a real-world application, you would replace the `mock_query_graphql_api` function with a function that makes actual requests to a GraphQL API.