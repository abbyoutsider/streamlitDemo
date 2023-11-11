import streamlit as st
import spacy

nlp = spacy.load("en_core_web_md")
mapping = {
        "flower": "flower.jpg",
        "car": "car.jpg",
        "tree": "tree.jpg",
        "mountain": "mountain.jpg",
        "building":"building.jpg"
}

words = mapping.keys()

def find_N_nearest_words(input, N):
  word = nlp(input)
  similarities=[]
  for w in words:
    w=nlp(w)
    similarity = word.similarity(w)
    similarities.append((similarity, w.text))
  similarities.sort(reverse=True)
  return [w for s,w in similarities[:N]]


def main():
  st.title("Find The Nearest Image App")
  prev_input=''
  user_input = st.text_input("Enter a word:")

  if prev_input != user_input:
          prev_input = user_input
          matched_word = find_N_nearest_words(user_input, 1)[0]
          st.caption("Find the nearest image: "+matched_word)
          st.image(mapping.get(matched_word))


if __name__ == "__main__":
  main()