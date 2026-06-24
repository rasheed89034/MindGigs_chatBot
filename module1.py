# import os
# import warnings
# warnings.filterwarnings("ignore")

# import uuid
# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# # Paths define kar rahe hain
# FILE_PATH = "data/mindgigs_data.txt"
# DB_DIR = "./vector_store"

# def build_vector_database():
#     print("🚀 Module 1 & 2: Building the Memory Bank...\n")

#     # Step 1: Load & Chunk Data
#     print("-> 📄 Data load aur chunking ho rahi hai...")
#     loader = TextLoader(FILE_PATH)
#     documents = loader.load()
    
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     chunks = text_splitter.split_documents(documents)
#     print(f"-> ✅ Total {len(chunks)} text chunks ban gaye.\n")

#     # Step 2: Embeddings (Text to Numbers)
#     print("-> 🧠 AI Embeddings model load ho raha hai...")
#     # Pehli baar run hone par model download hoga (lagbhag 80MB)
#     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#     # Step 3: Vector Database (ChromaDB) Setup
#     print("\n-> 💾 ChromaDB initialize ho raha hai...")
#     vectorstore = Chroma(
#         collection_name="mindgigs_collection",
#         embedding_function=embeddings,
#         persist_directory=DB_DIR
#     )

#     # Step 4: Upsert (Save Data to DB)
#     print("-> 📥 Data database mein save (upsert) kiya ja raha hai...")
#     chunk_ids = [str(uuid.uuid4()) for _ in chunks]
#     vectorstore.add_documents(documents=chunks, ids=chunk_ids)

#     print("\n🎉 MUBARAK HO! Aapka Memory Bank successfully ban gaya hai.")
#     print("Aap apne VS Code mein dekh sakte hain ke 'vector_store' naam ka ek naya folder ban gaya hoga.")

# if __name__ == "__main__":
#     if not os.path.exists(FILE_PATH):
#         print(f"❌ Error: File '{FILE_PATH}' nahi mili.")
#     else:
#         build_vector_database()

import os
import warnings
warnings.filterwarnings("ignore")

import uuid
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Paths define kar rahe hain
FILE_PATH = "data/mindgigs_data.txt"
DB_DIR = "./vector_store"

def build_vector_database():
    print("🚀 Module 1 & 2: Building the Memory Bank...\n")

    # Step 1: Load & Chunk Data
    print("-> 📄 Data loading")
    loader = TextLoader(FILE_PATH)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"-> ✅ Total {len(chunks)} text chunks.\n")

    # Step 2: Embeddings (Text to Numbers)
    print("-> 🧠 AI Embeddings model loading.....")
    # loading the model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Step 3: Vector Database (ChromaDB) Setup
    print("\n-> 💾 ChromaDB initializing...")
    vectorstore = Chroma(
        collection_name="mindgigs_collection",
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )

    # Step 4: Upsert (Save Data to DB)
    print("-> 📥 Data database...")
    chunk_ids = [str(uuid.uuid4()) for _ in chunks]
    vectorstore.add_documents(documents=chunks, ids=chunk_ids)

    print("\n🎉 Done")


if __name__ == "__main__":
    if not os.path.exists(FILE_PATH):
        print(f"❌ Error: File '{FILE_PATH}' Not Found")
    else:
        build_vector_database()
