const express = require('express');
const axios = require('axios');
const app = express();
app.use(express.json());

app.get('/api/context', async (req, res) => {
  try {
    const projects = await Project.find();
    const skills = await Skill.find();
    const context = {
      skills: skills.map(s => `${s.name} (${s.percentage}%)`),
      projects: projects.map(p => `${p.title}: ${p.description} (Links: ${p.links.map(l => l.option).join(', ')})`),
    };
    res.json(context);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch context' });
  }
});

app.get('/api/github/repos', async (req, res) => {
  try {
    const response = await axios.get('https://api.github.com/users/Mark-Lasfar/repos', {
      headers: {       Authorization: `Bearer ${process.env.GITHUB_TOKEN}`, }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch GitHub repos' });
  }
});

app.post('/api/ask', async (req, res) => {
  const { question } = req.body;
  try {
    const contextResponse = await axios.get('http://localhost:3000/api/context');
    const githubResponse = await axios.get('http://localhost:3000/api/github/repos');
    const context = contextResponse.data;
    const repos = githubResponse.data.map(repo => `${repo.name}: ${repo.description || 'No description'} (Language: ${repo.language}, URL: ${repo.html_url})`);
    const prompt = `
      You are elasfar-AI, a helpful assistant for Ibrahim Al-Asfar's portfolio website.
      Skills: ${context.skills.join(', ')}
      Projects: ${context.projects.join('\n')}
      GitHub Repositories: ${repos.join('\n')}
      Question: ${question}
    `;
    const response = await axios.post(
      'https://api-inference.huggingface.co/models/ibrahimlasfar/elasfar-AI',
      {
        inputs: prompt,
        parameters: { max_length: 150, temperature: 0.7 }
      },
      {
    headers: {
      Authorization: `Bearer ${process.env.HUGGING_FACE_TOKEN}`,
      'Content-Type': 'application/json'
    }
      }
    );
    res.json({ answer: response.data[0]?.generated_text || 'Sorry, I could not generate an answer.' });
  } catch (error) {
    console.error('Error processing question:', error.response?.data || error.message);
    res.status(500).json({ error: 'Failed to process question: ' + error.message });
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));