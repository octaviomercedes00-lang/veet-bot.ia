'use client'
import { useState } from 'react'

export default function Home(){
 const [text,setText]=useState('')
 const [out,setOut]=useState('')

 async function send(){
  const res = await fetch('/api/generate/stream',{method:'POST',body:text})
  const reader = res.body.getReader()
  while(true){
    const {done,value}=await reader.read()
    if(done) break
    setOut(o=>o+new TextDecoder().decode(value))
  }
 }

 return (<div>
   <textarea onChange={e=>setText(e.target.value)} />
   <button onClick={send}>Enviar</button>
   <pre>{out}</pre>
 </div>)
}