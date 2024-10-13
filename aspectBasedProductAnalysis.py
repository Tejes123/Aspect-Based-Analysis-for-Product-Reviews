from langchain_community.llms import Ollama
import json


ollama = Ollama(base_url = "http://localhost:11434", model = "phi3.5")

def aspectBasedProductAnalysis():

    # open negative review file
    negativeReviews = {}
    existingDict = {}
    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\negative.json", 'r') as file:
        negativeReviews = json.load(file)

    items = list(negativeReviews.items())

    # Step 2: Process the dictionary in batches of 10
    batch_size = 20
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]  # Get a batch of 10 items
        print(f"Processing batch {i//batch_size + 1}:")
        # print(batch)
        
        newDictionary = {}
        # You can now process the batch
        for key, value in batch:
            newDictionary[key] = value



        prompt = """ 
                    Recognize all aspect terms of products with their corresponding sentiment polarity in the given 10 reviews of various products enclosed within ''' '''. The aspect terms are nouns or phrases appearing in the review that indicate specific aspects or features of the product/service. Determine the problem specified with the aspect of product in one line. Answer in a single JSON object for 10 reviews as
                        {
                            {\"Product1 aspect\" : \"problemInproduct1\"}, 
                            {\"Product2 aspect\" : \"problemInproduct 2\"},
                            so on...
                        } 
                    without any explanation. You should not add any extra characters in the JSON data. The JSON should be valid to parse.  If no aspect term exists, then only answer {}.
                    
                    Reviews: '''
                    {{newDictionary}}
                    '''

                    example output
                    {
                        "camera quality" : "blurry in night",
                        "sauce" : "very sour in taste",
                        "book" : "low quality pages"
                    }
                    """

        prompt.replace('{{newDictionary}}', str(newDictionary))
        response = ollama(prompt)
        # print(response)


        start_idx = response.find('{')
        end_idx = response.rfind('}')

        # Step 2: Extract the JSON portion
        response = response[start_idx:end_idx+1]  # +1 to include the last '}
        try:
            response = json.loads(response.strip())
        except:
            response = {"batch : " + str(batch) : "error"}
            print("error Processing Batch : " + str(batch) + ". format of LLM generated content may not be correct")
        for key in response:
            existingDict[key] = response[key]

    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\topicExtractedNew.json", 'w') as file:
        json.dump(existingDict, file)


if __name__ == "__main__":
    aspectBasedProductAnalysis()
