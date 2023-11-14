from dotenv import load_dotenv
import spacy
def main():
    """
    :see https://spacy.io/api/large-language-models
    :return:
    """
    load_dotenv()
    nlp = spacy.blank("en")
    llm = nlp.add_pipe("llm_textcat")
    llm.add_label("INSULT")
    llm.add_label("COMPLIMENT")
    doc = nlp("You look gorgeous!")
    print(doc.cats)
    # {"COMPLIMENT": 1.0, "INSULT": 0.0}


if __name__ == '__main__':
    main()


