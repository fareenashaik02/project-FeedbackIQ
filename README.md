# 📊 FeedbackIQ

FeedbackIQ is an AI-powered customer feedback analysis web application built using **Streamlit**, **Groq LLM**, **Pandas**, and **Plotly**. It helps businesses analyze customer reviews by generating meaningful insights, identifying common issues, and providing improvement recommendations.

## 🚀 Features

- Upload any customer feedback CSV
- Automatically detects review and rating columns
- Displays dashboard metrics
- Interactive rating distribution chart
- Interactive sentiment distribution chart
- AI-generated review summary
- Positive highlights
- Common issues
- Business recommendations
- User-friendly interface built with Streamlit

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Groq API
- python-dotenv

## 📂 Project Structure

```
FeedbackIQ/
│── app.py
│── ai.py
│── dashboard.py
│── utils.py
│── sample_feedback.csv
│── requirements.txt
│── README.md
│── .gitignore
│── .env (not uploaded)
```

## ▶️ Installation

1. Clone the repository:

```bash
git clone https://github.com/fareenashaik02/FeedbackQI.git
```

2. Navigate to the project folder:

```bash
cd FeedbackQI
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

5. Run the application:

```bash
streamlit run app.py
```

## 📈 Future Improvements

- PDF report download
- Word cloud visualization
- Advanced sentiment analysis
- Support for Excel files
- Interactive filters
- Enhanced dashboard design

## 👩‍💻 Developed By

**Fareena Shaik**

As part of an AIML Internship Project.