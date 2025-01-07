"""
This python file contains code for NER and dependency parsing.
"""

import spacy
import networkx as nx
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")  # Load small English model; try "en_core_web_lg" for better results

# Named Entity Recognition (NER)
def extract_ner(text):
    if not text:
      return []
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Usage of Named Entity Recognition (NER)

file = open("SampleLGBTTransformerCode/PDFParser/LGBTQmicroaggressions-webinar-transcript.txt", "r")
preprocessed_text = file.read()
file.close()

if preprocessed_text:
  ner_entities = extract_ner(preprocessed_text)
  if ner_entities:
    print("Named entities:")
    for entity, label in ner_entities:
      print(f"{entity}: {label}")
  else:
    print("No named entities found.")

# Dependency Parsing
def create_dependency_graph(text):
  if not text:
    return None
  doc = nlp(text)
  G = nx.DiGraph()
  for token in doc:
       G.add_node(token.text, pos = token.pos_)
       for child in token.children:
           G.add_edge(token.text, child.text, label=child.dep_)
  return G

def visualize_dependency_graph(graph, filename="SampleLGBTTransformerCode/NER&DepedencyGraph/dependency_graph.png"):
   if not graph:
       print("No dependency graph to visualize.")
       return
   pos = nx.spring_layout(graph, seed = 70)
   nx.draw(graph, pos, with_labels = True, node_size = 3000, node_color = 'skyblue', font_size = 10)

   edge_labels = nx.get_edge_attributes(graph, 'label')
   nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size = 8)
   plt.savefig(filename)
   print("Dependency graph saved as {filename}")

# Usage of Dependency Parsing
if preprocessed_text:
  dependency_graph = create_dependency_graph(preprocessed_text)
  visualize_dependency_graph(dependency_graph)


