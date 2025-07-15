# 🤖 AI Error Explainer

Una herramienta web que analiza errores técnicos usando inteligencia artificial (OpenAI) y te proporciona explicaciones simples, causas probables y soluciones prácticas.

## 🚀 Funcionalidades

- Análisis de errores técnicos.
- Explicación simple.
- Causas comunes.
- Soluciones recomendadas.
- (Opcional) Enlaces a StackOverflow.

## ⚙️ Tecnologías

- Django
- OpenAI GPT-4
- BeautifulSoup (para scraping de StackOverflow)
- Bootstrap (Frontend)

## 🧪 Instalación

```bash
git clone https://github.com/guillermopayllon/aplicaciones/ai-error-explainer.git
cd ai-error-explainer
pip install -r requirements.txt
cp .env.example .env
# Añade tu clave de OpenAI en .env
python manage.py runserver
