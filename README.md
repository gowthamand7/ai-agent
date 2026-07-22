# AI Systems Engineering Journey

This repository tracks my learning path and projects to become a Principal/Senior Principal **AI Systems Engineer & AI Architect**. The focus is on building real, production-grade AI systems, leveraging my background in distributed systems, microservices, and backend engineering.

## Projects Built

* [Hello World](./hello-world/) - Initial project and setup
* [Search Agent](./search-agent/) - A LangChain agent implementing a Tavily search tool and Pydantic schemas
* [E-Commerce Agent with Loop](./ecommerce-agent-with-loop/) - A custom tool-calling agent loop implementation featuring 5 custom tools (`searchitems`, `getitems`, `available_discounts`, `getreviews`, `calculate_final_price`). It operates over a generated JSON mock inventory and demonstrates structured Pydantic outputs alongside interactive chain-of-thought reasoning.
* [E-Commerce Agent with Classic ReAct](./ecommerce-agent-with-reactprompt/) - An implementation of the ReAct agent using the modern LangGraph `create_react_agent` architecture.

---

## Learning Roadmap

Below is the targeted curriculum and current progress. Topics are marked as completed (`[x]`) as they are explored and implemented in this repository.

### Phase 1: Foundations for Building Real AI Systems
- [ ] **Embeddings**
  - [ ] Dense vs sparse embeddings, Cosine similarity, Semantic search, Chunking, Cross-encoder vs bi-encoder, Reranking
- [ ] **Vector Databases**
  - [ ] Indexing, ANN search, HNSW, IVF, PQ, Metadata filtering (Pinecone, Qdrant, Milvus, pgvector)
- [ ] **RAG (Retrieval-Augmented Generation)**
  - [ ] Ingestion pipeline, Chunking strategies (Parent-child, Semantic), Hybrid search, Context window management

### Phase 2: LLM Internals
- [ ] **Transformers**
  - [ ] Tokens, Tokenization, Attention, Self-attention, Multi-head attention, Positional encoding, Context window
- [ ] **Context Engineering**
  - [ ] Prompt architecture, System prompts, Context compression, Dynamic context loading, Retrieval injection

### Phase 3: Advanced Retrieval Systems
- [ ] **Advanced RAG**
  - [ ] Hybrid retrieval, Multi-query retrieval, Query rewriting, Graph RAG, Agentic RAG, CRAG, Self-RAG, Adaptive RAG

### Phase 4: Agents
- **Agents**
  - [x] Tool calling
  - [x] Function calling
  - [x] ReAct
  - [ ] Planning
  - [ ] Reflection
- [ ] **Memory**
  - [ ] Short-term memory (Conversation history, Session memory)
  - [ ] Long-term memory (Vector, Episodic, Semantic memory)
  - [ ] Memory architectures (Retrieval, summarization, pruning)

### Phase 5: Multi-Agent Systems
- [ ] **Multi-Agent**
  - [ ] Agent orchestration, communication, shared memory, Supervisor pattern
  - [ ] Architectures: Swarm, Crew, Hierarchical, Blackboard

### Phase 6: Evaluation & Production AI
- [ ] **Evals**
  - [ ] LLM evaluation, Retrieval evaluation, Hallucination scoring, Groundedness, Faithfulness, Relevance
  - [ ] Metrics: Precision, Recall, Hit Rate, MRR, NDCG
  - [ ] LLM-as-a-judge & Human evaluation

### Parallel Topics (Continuous Learning)
- [ ] **LLM APIs & Inference** (Model selection, latency, cost optimization, tokens)
- [ ] **AI System Design** (AI gateway, prompt versioning, model routing, fallback models, caching, observability, cost controls)
- [ ] **MCP (Model Context Protocol)** (Architecture, servers, tool discovery, resource providers)
- [ ] **AI Security** (Prompt injection, data leakage, jailbreaks, tool abuse, RAG poisoning)
