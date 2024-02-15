from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document


CHROMA_PATH = "chroma"
DATA_PATH = "data"
GLOB_PATTERN = "*.md"


def main():
    print("Testing from database main ")
    generate_data_store()


def generate_data_store():
    print('Testing from database generate data story ')
    documents = load_documents()


def load_documents():
    print('Testing from database Load documents ')
    loader = DirectoryLoader(DATA_PATH, glob=GLOB_PATTERN)
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    print("Split text")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )

    chunks = splitter.split_documents(documents)
    # log.info(f"Split {len(documents)} documents into {len(chunks)} chunks")
    document = chunks[10]
    print(document)
    print(document.page_content)
    print(document.metadata)

    return chunks


# def save_to_chroma(chunks: list[Document]):
#     db = Chroma.from_documents(
#     chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
#     )


# def save_to_chroma(chunks: list[Document]):
#     if(utils.check_openai_api_key):
#         collection = chroma_client.get_or_create_collection(name="Alice")
#         collection.add(embeddings=OpenAIEmbeddings(openai_api_type=utils.open_ai_api_key),
#                        documents= chunks)


#     # checks if a directory exsists at 'CHROMA_PATH' if it doesnt it deletes it and its contents.
#     if os.path.exists(CHROMA_PATH):
#         shutil.rmtree(CHROMA_PATH)
#     #creates a new 'Chroma' db from the list of chunks using OpenAIEmbeddings()
#     db = Chroma.from_documents(
#         chunks,
#         OpenAIEmbeddings(api_key='u0aa5FFP2tV13ySWHwzoT3BlbkFJhmexOQ9irExWhsLVPCEK'),
#         persist_directory=CHROMA_PATH
#     )
#     #saves db
#     db.persist()
#     print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

# Checks if the script is being run directly


if __name__ == "__main__":
    main()
