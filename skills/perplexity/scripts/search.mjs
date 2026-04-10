#!/usr/bin/env node
// Perplexity Search via API - returns AI-synthesized answers with citations
const query = process.argv.slice(2).join(' ');
if (!query) { console.error('Usage: node search.mjs "your query"'); process.exit(1); }

const apiKey = process.env.PERPLEXITY_API_KEY || '';
if (!apiKey) { console.error('PERPLEXITY_API_KEY not set'); process.exit(1); }

fetch('https://api.perplexity.ai/chat/completions', {
  method: 'POST',
  headers: { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({
    model: 'sonar',
    messages: [{ role: 'user', content: query }],
    max_tokens: 1000
  })
}).then(r => r.json()).then(d => {
  if (d.choices) {
    console.log(d.choices[0].message.content);
    if (d.citations?.length) {
      console.log('\n--- Sources ---');
      d.citations.forEach(c => console.log(`- ${c}`));
    }
  } else {
    console.error(JSON.stringify(d));
  }
}).catch(e => console.error(e));
