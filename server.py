from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

app = FastAPI()

# قراءة التوكن من Environment Variable
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN", "")

# تحميل النموذج والتوكنيزر
model_name = "ibrahimlasfar/elasfar-AI"
tokenizer = AutoTokenizer.from_pretrained(model_name, token=HUGGING_FACE_TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_name, token=HUGGING_FACE_TOKEN)

class Query(BaseModel):
    question: str

class Conversation(BaseModel):
    messages: list[dict]  # قائمة من الرسائل، كل رسالة فيها {'role': 'user'|'assistant', 'content': str}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/ask")
async def ask_question(query: Query):
    try:
        # إنشاء السياق
        context = f"""
        Website: Ibrahim Al-Asfar's personal portfolio.
        Description: A full-stack web developer portfolio showcasing projects, skills, and contact information.
        Question: {query.question}
        """
        inputs = tokenizer(context, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(**inputs, max_length=150, num_return_sequences=1, temperature=0.7)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@app.post("/api/converse")
async def converse(conversation: Conversation):
    try:
        # بناء سلسلة المحادثة
        conversation_text = ""
        for msg in conversation.messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation_text += f"{role}: {msg['content']}\n"
        context = f"""
        Website: Ibrahim Al-Asfar's personal portfolio.
        Description: A full-stack web developer portfolio showcasing projects, skills, and contact information.
        Conversation:
        {conversation_text}
        Assistant: """
        inputs = tokenizer(context, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(**inputs, max_length=150, num_return_sequences=1, temperature=0.7)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # إزالة السياق من الرد لإرجاع إجابة الـ Assistant فقط
        response = response.replace(context, "").strip()
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing conversation: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
