from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import StateGraph, END
from schema import AnswerQuestion, ReviseAnswer
from chains import revisor_chain, first_responder_chain
from execute_tools import execute_tools


# --- 1. State Şeması: Revize Edilen Cevap + Iteration Sayısı ---
from langchain_core.messages import BaseMessage


class IterationState(ReviseAnswer):
    iterations: int = 0
    messages: List[BaseMessage] = []


# --- 2. StateGraph Oluştur ve Düğümleri Tanımla ---
graph = StateGraph(state_schema=IterationState)
MAX_ITERATIONS = 2

# Ajan zinciri düğümleri
graph.add_node("draft", first_responder_chain)
graph.add_node("execute_tools", execute_tools)
graph.add_node("revisor", revisor_chain)

# Düğümler arasındaki akış yönlendirmeleri
graph.add_edge("draft", "execute_tools")
graph.add_edge("execute_tools", "revisor")


# --- 3. Durum Kontrolü: Kaç Kez Execute Tools'a Gidildiğini Yönet ---
def event_loop(state: IterationState) -> str:
    if state.iterations >= MAX_ITERATIONS:
        return END
    state.iterations += 1
    return "execute_tools"

graph.add_conditional_edges("revisor", event_loop)

# Başlangıç düğümü
graph.set_entry_point("draft")

# --- 4. Graph’u Derle ve Mermaid ile Görselleştir ---
app = graph.compile()
print(app.get_graph().draw_mermaid())

# --- 5. Workflow’u Başlat ---
initial_state = IterationState(
    answer="",
    search_queries=[],
    reflection={"missing": "", "superfluous": ""},
    references=[],
    iterations=0,
)

response = app.invoke(initial_state)

# --- 6. Sonucu Yazdır ---
print("### Final Cevap ###")
print(response.answer, "\n")
print("### Reflection (Eleştiri) ###")
print("Missing:", response.reflection.missing)
print("Superfluous:", response.reflection.superfluous, "\n")
print("### Kaynaklar ###")
print(response.references)
