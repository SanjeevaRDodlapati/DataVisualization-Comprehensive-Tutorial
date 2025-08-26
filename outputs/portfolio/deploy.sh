#!/bin/bash
# Portfolio Deployment Script

echo "🚀 Deploying Data Visualization Portfolio..."

# Check if required files exist
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found"
    exit 1
fi

if [ ! -d "dashboards" ]; then
    echo "❌ Error: dashboards directory not found"
    exit 1
fi

echo "✅ Portfolio files verified"

# Option 1: Local server for testing
echo "🌐 Starting local server for testing..."
echo "📂 Portfolio available at: http://localhost:8000"
echo "🛑 Press Ctrl+C to stop the server"

python3 -m http.server 8000

# Option 2: Deploy to GitHub Pages (uncomment to use)
# echo "📤 Deploying to GitHub Pages..."
# git add .
# git commit -m "Deploy portfolio update"
# git push origin main

echo "🎉 Deployment complete!"
