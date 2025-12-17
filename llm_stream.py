from vllm import LLM, SamplingParams

llm = LLM(model="/models/llama3-70b")

params = SamplingParams(temperature=0.2, max_tokens=1200, stream=True)

def stream_bdfd(prompt):
    for out in llm.generate(prompt, params):
        yield out.outputs[0].text