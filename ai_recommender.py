import google.generativeai as genai

def get_recommendation(user_taste, catalogue_titles):
    titles_text = ", ".join(catalogue_titles)
    prompt = ("A library has these books: " + titles_text + ". "
              "A member likes " + user_taste + ". "
              "Recommend ONE book from this exact list and give a one-sentence reason.")
    try:
        genai.configure(api_key="AQ.Ab8RN6K7Dfl8Re5dgQ6c_UwufxIXFSzcOuUunvbMtYuGOta5rA")
        model = genai.GenerativeModel("gemini-3.8-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Error fetching recommendation: " + str(e))
        return "Sorry, recommendations are unavailable right now."