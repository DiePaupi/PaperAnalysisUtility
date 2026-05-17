###############################################################################
# Imports
###############################################################################
from dotenv import load_dotenv, find_dotenv
import json
from openai import OpenAI
import os
from pathlib import Path
import urllib.request



###############################################################################
# INFO
###############################################################################

# LLM is called in
#  1) RankingChecker.py -> check_with_llm()
#  2) RefIntextChecker.py -> check_with_llm()



###############################################################################
# Gloal Variables
###############################################################################
USE_CAMPUS_KI = True

call_counter = 0

cwd = os.getcwd()
path_to_env = Path(os.path.join(cwd, "Libs",".env"))



###############################################################################
# Helper functions
###############################################################################

def get_llm_call_counter():
    """
    get_llm_call_counter returns the number of times an LLM has been called 
    since the server was started.
    """

    global call_counter
    return call_counter


def call_campuski(user_message):
    global call_counter
    call_counter += 1
    print(f"  // LLM calling counter = {call_counter}")

    load_dotenv(path_to_env)
    CKI_API_KEY = os.getenv("CKI_API_KEY")

    URL = "https://chat.kiconnect.nrw/api/v1/chat/completions"

    # CampusKI model examples: "GPT5-Mitarbeitende" (100m/h),
    #                          "GPT5-mini-Mitarbeitende" (1000m/h),
    #                          "OpenAI GPT OSS 120B" (unlimited)
    data = {
        "model": "GPT5-mini-Mitarbeitende",
        "messages": [
                        {
                            "role": "user",
                            "content": f"{user_message}"
                        }
                    ]
    }
    
    if not CKI_API_KEY:
        raise RuntimeError("CKI_API_KEY not set in the loaded environment. Set it or load your .env before starting server.")


    try:
        request = urllib.request.Request(URL, data=json.dumps(data).encode("utf-8"),
                                        headers={"Authorization": f"Bearer {CKI_API_KEY}",
                                                "Content-Type": "application/json"},
                                        method="POST")

        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  => ERROR while trying to reach CampusKI: {e}")
        return ""


def call_openai(user_message):
    global call_counter
    call_counter += 1
    print(f"  // LLM calling counter = {call_counter}")

    load_dotenv(path_to_env)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # OpenAI model examples: "gpt-4o-mini", "gpt-3.5-turbo-0125"
    model = "gpt-4o-mini"
    temp = 0.0

    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set in the loaded environment. Set it or load your .env before starting server.")

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=model,
            temperature=temp,
            messages=user_message
        )
        # return just the text response
        return response.choices[0].message.content
    except Exception as e:
        print(f"  => ERROR while trying to reach ChatGPT: {e}")
        return ""


###############################################################################
# Main code
###############################################################################

def call_llm(user_message):
    if USE_CAMPUS_KI:
        return call_campuski(user_message)
    else:
        return call_openai(user_message)
    



# TESTING
if __name__ == "__main__":
    user_message = input("Enter prompt: ").strip()
    llm_answer = call_llm(user_message)
    print(llm_answer)