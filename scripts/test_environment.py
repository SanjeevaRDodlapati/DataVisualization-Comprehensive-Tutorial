#!/usr/bin/env python3
"""
Environment Test Script for Data Visualization Comprehensive Series
==================================================================

This script tests the installation of all required packages and provides
a comprehensive environment verification report.

Usage:
    python scripts/test_environment.py
    python scripts/test_environment.py --verbose
"""

import sys
import importlib
import platform
import subprocess
from pathlib import Path
import argparse

def test_package_import(package_name, import_name=None, description=""):
    """Test if a package can be imported and return version info."""
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        return {'status': '✅', 'version': version, 'error': None}
    except ImportError as e:
        return {'status': '❌', 'version': None, 'error': str(e)}
    except Exception as e:
        return {'status': '⚠️', 'version': None, 'error': str(e)}

def test_environment():
    """Test the complete environment setup."""
    
    print("🔍 Data Visualization Environment Test")
    print("=" * 50)
    
    # System information
    print(f"🐍 Python Version: {platform.python_version()}")
    print(f"💻 Platform: {platform.platform()}")
    print(f"🏗️ Architecture: {platform.architecture()[0]}")
    print()
    
    # Test packages
    packages_to_test = [
        # Core data manipulation
        ('pandas', 'pandas', 'Data manipulation and analysis'),
        ('numpy', 'numpy', 'Numerical computing'),
        ('scipy', 'scipy', 'Scientific computing'),
        ('scikit-learn', 'sklearn', 'Machine learning'),
        
        # Static visualization
        ('matplotlib', 'matplotlib', 'Static plotting library'),
        ('seaborn', 'seaborn', 'Statistical visualization'),
        
        # Interactive visualization
        ('plotly', 'plotly', 'Interactive plotting'),
        ('altair', 'altair', 'Declarative visualization'),
        ('bokeh', 'bokeh', 'Interactive web plots'),
        
        # Geospatial core
        ('geopandas', 'geopandas', 'Geospatial data manipulation'),
        ('shapely', 'shapely', 'Geometric operations'),
        ('fiona', 'fiona', 'Geospatial data I/O'),
        ('rasterio', 'rasterio', 'Raster data I/O'),
        ('pyproj', 'pyproj', 'Cartographic projections'),
        
        # Geospatial visualization
        ('folium', 'folium', 'Interactive mapping'),
        ('contextily', 'contextily', 'Map tiles and contexts'),
        
        # Big data and performance
        ('datashader', 'datashader', 'Large dataset visualization'),
        ('dask', 'dask', 'Parallel computing'),
        ('numba', 'numba', 'JIT compilation'),
        
        # Dashboard frameworks
        ('streamlit', 'streamlit', 'Web app framework'),
        ('panel', 'panel', 'Dashboard framework'),
        
        # Jupyter ecosystem
        ('notebook', 'notebook', 'Jupyter notebooks'),
        ('jupyterlab', 'jupyterlab', 'JupyterLab interface'),
        ('ipywidgets', 'ipywidgets', 'Interactive widgets'),
        
        # Additional packages
        ('requests', 'requests', 'HTTP library'),
        ('tqdm', 'tqdm', 'Progress bars'),
    ]
    
    print("📦 Package Installation Status:")
    print("-" * 70)
    print(f"{'Package':<20} {'Status':<8} {'Version':<15} {'Description'}")
    print("-" * 70)
    
    all_passed = True
    failed_packages = []
    
    for package_name, import_name, description in packages_to_test:
        result = test_package_import(package_name, import_name, description)
        status = result['status']
        version = result['version'] or 'N/A'
        
        print(f"{package_name:<20} {status:<8} {version:<15} {description}")
        
        if result['status'] == '❌':
            all_passed = False
            failed_packages.append((package_name, result['error']))
    
    print("-" * 70)
    
    # Test optional pip packages
    pip_packages = [
        ('leafmap', 'leafmap', 'Interactive geospatial analysis'),
        ('pydeck', 'pydeck', 'GPU-accelerated visualization'),
        ('keplergl', 'keplergl', 'Geospatial data exploration'),
    ]
    
    print("\n🌟 Optional Packages (pip-installed):")
    print("-" * 70)
    print(f"{'Package':<20} {'Status':<8} {'Version':<15} {'Description'}")
    print("-" * 70)
    
    for package_name, import_name, description in pip_packages:
        result = test_package_import(package_name, import_name, description)
        status = result['status']
        version = result['version'] or 'N/A'
        
        print(f"{package_name:<20} {status:<8} {version:<15} {description}")
    
    print("-" * 70)
    
    # Test Jupyter kernel
    print("\n🔬 Jupyter Environment Test:")
    try:
        import IPython
        print(f"✅ IPython version: {IPython.__version__}")
        
        # Test if we're in a Jupyter environment
        try:
            from IPython import get_ipython
            ipython = get_ipython()
            if ipython is not None:
                print("✅ Running in Jupyter environment")
            else:
                print("ℹ️ Not currently in Jupyter environment (this is normal for terminal)")
        except:
            print("ℹ️ IPython available but not in interactive mode")
            
    except ImportError:
        print("❌ IPython not available")
        all_passed = False
    
    # Test data directory
    print("\n📁 Data Directory Test:")
    data_dir = Path(__file__).parent.parent / "data"
    if data_dir.exists():
        data_files = list(data_dir.rglob("*.csv")) + list(data_dir.rglob("*.geojson"))
        print(f"✅ Data directory exists: {data_dir}")
        print(f"📊 Found {len(data_files)} data files")
    else:
        print(f"⚠️ Data directory not found: {data_dir}")
        print("ℹ️ Run 'python scripts/download_sample_data.py' to download sample data")
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 Environment Test: PASSED")
        print("✅ All core packages are installed and working!")
        print("🚀 You're ready to start the Data Visualization Tutorial Series!")
    else:
        print("⚠️ Environment Test: ISSUES DETECTED")
        print(f"❌ {len(failed_packages)} package(s) failed to import:")
        for pkg, error in failed_packages:
            print(f"   • {pkg}: {error}")
        print("\n💡 Installation suggestions:")
        print("   1. Recreate the conda environment:")
        print("      conda env remove -n dataviz_comprehensive")
        print("      conda env create -f environment_dataviz.yml")
        print("   2. Activate the environment:")
        print("      conda activate dataviz_comprehensive")
        print("   3. Install missing packages individually:")
        for pkg, _ in failed_packages:
            print(f"      conda install {pkg}")
    
    return all_passed

def test_plotting_functionality():
    """Test basic plotting functionality."""
    print("\n🎨 Plotting Functionality Test:")
    print("-" * 30)
    
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Test matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))
        x = np.linspace(0, 10, 100)
        ax.plot(x, np.sin(x))
        ax.set_title("Test Plot")
        plt.close(fig)  # Close to avoid display in terminal
        print("✅ Matplotlib: Basic plotting works")
        
    except Exception as e:
        print(f"❌ Matplotlib: {e}")
        return False
    
    try:
        import seaborn as sns
        import pandas as pd
        
        # Test seaborn
        df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 4, 2]})
        fig = plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x='x', y='y')
        plt.close(fig)
        print("✅ Seaborn: Statistical plotting works")
        
    except Exception as e:
        print(f"❌ Seaborn: {e}")
        return False
    
    try:
        import plotly.graph_objects as go
        
        # Test plotly
        fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[1, 4, 2]))
        fig.update_layout(title="Test Interactive Plot")
        # Don't show the plot in terminal
        print("✅ Plotly: Interactive plotting works")
        
    except Exception as e:
        print(f"❌ Plotly: {e}")
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Test Data Visualization Tutorial environment")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--plot-test", action="store_true", help="Test plotting functionality")
    
    args = parser.parse_args()
    
    # Run main environment test
    env_passed = test_environment()
    
    # Run plotting test if requested
    if args.plot_test:
        plot_passed = test_plotting_functionality()
        if not plot_passed:
            env_passed = False
    
    # Exit with appropriate code
    sys.exit(0 if env_passed else 1)

if __name__ == "__main__":
    main()
