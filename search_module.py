import os
from openai import OpenAI
from dotenv import load_dotenv

# Main function to handle search and summarization flow
def search_and_summarize(user_query):
    """
    Determines whether a web search is necessary, performs the search,
    selects the most relevant links, downloads content, and summarizes it.

    Args:
        user_query (str): User's question in Polish.

    Returns:
        str or None: Summary of online content or None if search was unnecessary
        or failed to produce valuable content.
    """
    decision = should_search_and_generate_query(user_query)

    if decision.get("search") and decision.get("query"):
        print(f"Starting internet search for query: {decision['query']}")
        links = search_duckduckgo(decision["query"], num_links=10)

        if links:
            selected_urls = select_best_links_llm(links, user_query, top_n=3)

            if selected_urls:
                print(f"Selected {len(selected_urls)} links for content extraction.")
                combined_content = ""
                for url in selected_urls:
                    content = fetch_content_from_url(url)
                    if content:
                        combined_content += f"\n\n--- Content from {url} ---\n{content}"
                    if len(combined_content) > MAX_CONTENT_LENGTH * 1.2:
                        print("Reached maximum content length. Stopping further downloads.")
                        break

                if combined_content.strip():
                    print("Summarizing the collected content...")
                    summary = summarize_content_llm(combined_content, user_query)
                    return summary
                else:
                    print("No valuable content extracted from selected links.")
                    return None
            else:
                print("LLM did not select any promising links.")
                return None
        else:
            print("Search returned no results.")
            return None
    else:
        print("No search required for this query.")
        return None


if __name__ == "__main__":
    # Load OpenAI API key from environment file
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")

    if not key:
        print("OpenAI API key not found. Please set it in a .env file.")
    else:
        client = OpenAI(api_key=key)

        example_query = "Jakie są najnowsze wiadomości ze świata technologii?"
        result = search_and_summarize(example_query)

        if result:
            print(f"\nSummary for query '{example_query}':\n{result}")
        else:
            print(f"\nNo summary available for query '{example_query}'.")
