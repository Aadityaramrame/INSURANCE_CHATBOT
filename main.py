# main.py

from rag_chain import get_rag_response

def main():
    print("\n📄 Insurance Chatbot (RAG-Based)")
    print("Type your question below. Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("🧑 You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting. Have a good day!")
            break

        try:
            response = get_rag_response(user_input)
            print(f"\n🤖 Chatbot: {response}\n")
        except Exception as e:
            print(f"\n⚠️ Error: {str(e)}\n")

if __name__ == "__main__":
    main()
