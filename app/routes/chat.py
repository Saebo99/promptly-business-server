from quart import Blueprint, request, jsonify
from openai import AzureOpenAI

chat = Blueprint('chat', __name__)

def get_openai_client():
    return AzureOpenAI(
        azure_endpoint="https://promptly-ai-sweden.openai.azure.com/openai/deployments/test/chat/completions?api-version=2023-07-01-preview",
        api_key="ecea7819c5734105980b052809d63b58",
        api_version="2023-05-15"
    )

@chat.route('/chat', methods=['POST'])
async def chat_route():
    try:
        data = await request.get_json()
        question = data.get("question")
        print(f"Question: {question}")

        client = get_openai_client()
        print("Creating completion...")
        response = client.chat.completions.create(
            model="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        print(f"Answer: {answer}")
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500