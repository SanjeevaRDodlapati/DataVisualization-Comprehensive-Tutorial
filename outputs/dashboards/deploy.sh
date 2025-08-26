#!/bin/bash
# Streamlit Dashboard Deployment Script

echo "🚀 Starting Streamlit Dashboard Deployment"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Set environment variables
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

echo "✅ Setup complete!"
echo "🌐 Available dashboards:"
echo "   • streamlit run sales_dashboard.py"
echo "   • streamlit run scientific_explorer.py"
echo "   • streamlit run multipage_dashboard.py"
echo "   • streamlit run optimized_dashboard.py"
