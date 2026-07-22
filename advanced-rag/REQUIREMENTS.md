# Advanced RAG: Azure DevOps Wiki Search Bot

## Overview
This project aims to build an Advanced RAG-powered search bot that operates over a large-scale Azure DevOps (ADO) Wiki repository. ADO wikis are markdown-heavy and can contain thousands of interconnected documents featuring code blocks, Mermaid diagrams, images, and internal links.

## Key Challenges & Requirements
1. **Scale**: Handling 1000s of markdown documents efficiently.
2. **Rich Markdown**: Processing documents that contain:
   - Code blocks (requires structural preservation for copy/pasting)
   - Mermaid diagrams (text-based visual representations)
   - Images (requires multimodal handling or alt-text extraction)
   - Cross-links (requires metadata retention for citations and traversal)

---

## High-Level Implementation Strategy

### 1. Ingestion & Parsing Pipeline
- **ADO Repo Sync**: Pull the raw markdown files directly from the Azure DevOps git repository backing the wiki.
- **Markdown Parsing**: Use a markdown-aware parser (e.g., Unstructured or LangChain's `MarkdownHeaderTextSplitter`).
- **Special Elements Handling**:
  - **Code Blocks**: Extract and chunk code separately, keeping the programming language as metadata to aid in syntax-specific searches.
  - **Mermaid Diagrams**: Extract the raw Mermaid syntax. Optionally, pass the Mermaid text to a lightweight LLM during ingestion to generate a natural language summary of the diagram, indexing both the syntax and the summary.
  - **Images**: Extract image URLs and alt-text. If high fidelity is needed, use a multimodal model to generate descriptions of the images during ingestion.
  - **Links**: Preserve relative paths and convert them to absolute ADO Wiki URLs for proper citation in the final bot response.

### 2. Chunking Strategy
- **Semantic & Parent-Child Chunking (Zero Context Loss)**: Split documents based on markdown headers (`#`, `##`, `###`) rather than naive character counts. To guarantee zero context loss, use a Parent-Child architecture: index small, highly-specific chunks (children) in the vector database for precise matching, but retrieve the entire surrounding section or document (parent) to provide the LLM with complete context.

### 3. Embedding & Storage
- **Hybrid Search (Bi-Encoder + BM25)**: Use a Bi-Encoder model to generate Dense embeddings (for deep semantic meaning), combined with Sparse embeddings/BM25 (for exact-match keyword search). Keyword search is crucial for retrieving specific error codes, repository names, and code snippets that dense vectors often miss.
- **Vector Database**: Use a scalable vector DB (like Qdrant, Milvus, or Pinecone) that natively supports metadata filtering (filtering by wiki folder, tags, or authors).

### 4. Retrieval & Generation (The Bot)
- **Query Rewriting**: When a user asks a question, use a fast LLM to rewrite the query into multiple variations (e.g., translating a vague user question into specific technical keywords) to improve the retrieval hit rate.
- **Cross-Encoder Reranking**: The initial hybrid search will return many candidate chunks. We will pass these candidates through a Cross-Encoder model (e.g., Cohere Rerank, BGE-Reranker) to score and highly optimize their order based on deep query-document interaction, ensuring the generation LLM only sees the absolute best context.
- **Grounded Generation**: Prompt the LLM to answer the question using *only* the retrieved context, and mandate that it appends exact source URLs (clickable ADO wiki links) for every claim it makes.

---

## Next Steps
- [ ] Refine this architecture based on specific Azure DevOps access patterns and team requirements.
- [ ] Setup the initial markdown ingestion script to test parsing logic on a small subset of the Wiki.
- [ ] Evaluate embedding models that perform well on technical/code-heavy text.
