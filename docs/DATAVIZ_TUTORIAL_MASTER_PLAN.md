# 📊 Data Visualization Comprehensive Tutorial Series - Master Plan

**Expert-Level Data Visualization with Python: Analysis + Communication**

## 🎯 **Tutorial Series Overview**

This comprehensive tutorial series transforms intermediate Python users into expert data visualization practitioners, focusing on **analysis + communication** rather than just creating charts. The series emphasizes real-world applications, best practices, and storytelling through data.

### **Target Audience**
- **Primary**: Intermediate Python users (comfortable with pandas, basic statistics)
- **Skills**: Basic programming, some data analysis experience
- **Goal**: Master data visualization for professional analysis and communication

### **Core Philosophy**
- **Analysis-Driven**: Every visualization serves an analytical purpose
- **Communication-First**: Charts must tell clear, compelling stories
- **Best Practices**: Industry-standard approaches to color, accessibility, design
- **Real Data**: Authentic datasets with real-world complexity
- **Reproducible**: Full environment setup and data pipelines

---

## 📚 **Syllabus Overview (14 Modules)**

This syllabus balances depth and progression from fundamentals to advanced applications. Each module is designed as a standalone Jupyter notebook, building on prerequisites. Total estimated time: 35-45 hours for focused learning path.

| Module | Title | Learning Objectives | Inputs/Outputs | Estimated Time |
|--------|-------|--------------------|--------------------|-----------------|
| **1** | **Introduction to Data Visualization Principles** | Understand core viz concepts; choose charts based on data types/tasks; avoid common pitfalls | Input: Gapminder dataset; Output: Basic plots, chart rationale doc | 2 hours |
| **2** | **Visual Best Practices and Accessibility** | Apply encodings, colors, labels; ensure accessibility; redesign poor charts | Input: NYC TLC trips sample; Output: Accessible figures, checklist application | 2.5 hours |
| **3** | **Visualizing Distributions and Uncertainty** | Handle histograms, KDEs, violins; visualize CIs, error bars; interpret uncertainty | Input: NOAA GSOD climate; Output: Distribution plots with uncertainty overlays | 2.5 hours |
| **4** | **Time Series and Change Over Time** | Plot trends, seasonality; use small multiples, annotations; avoid misleading axes | Input: Johns Hopkins COVID archive; Output: Annotated time series figures | 2 hours |
| **5** | **Comparisons and Relationships** | Create scatter, pair plots, heatmaps; distinguish correlation/causation; use marginals | Input: Gapminder + OpenAQ air quality; Output: Relationship visualizations, mini-analysis | 2.5 hours |
| **6** | **Handling Large Datasets and Interactivity** | Downsample, bin, use Datashader; build basic interactive plots with Plotly/Altair | Input: NYC TLC large sample; Output: Interactive big data viz, performance report | 3 hours |
| **7** | **Geospatial Visualization: Vector Data** | Work with GeoJSON/Shapefiles; create choropleths, symbols; handle classifications | Input: Natural Earth + GADM boundaries, GBIF occurrences; Output: Vector maps, habitat analysis | 3 hours |
| **8** | **Geospatial Visualization: Raster and Interactive Maps** | Process rasters, compute indices; build interactive maps with Folium/Pydeck | Input: Copernicus DEM + Landsat/Sentinel samples; Output: Raster composites, interactive map dashboard | 3 hours |
| **9** | **Color Theory and Accessibility Design** | Master ColorBrewer, Okabe-Ito palettes; ensure WCAG compliance; design for colorblind users | Input: All previous datasets; Output: Accessible palette guide, redesigned figures | 2 hours |
| **10** | **Advanced Matplotlib and Publication Graphics** | Custom styling, complex layouts; export publication-quality figures; vector formats | Input: Scientific datasets; Output: Publication-ready figures, style guide | 2.5 hours |
| **11** | **Interactive Dashboards and Streamlit** | Build responsive dashboards; implement filtering, linked brushing; optimize performance | Input: Combined datasets; Output: Multi-panel dashboard, UX report | 3 hours |
| **12** | **Data Storytelling and Narrative Design** | Structure narratives; build focus+context; incorporate scrollytelling principles | Input: Conservation case study data; Output: Narrative dashboard, story arc document | 2.5 hours |
| **13** | **Ethics, Integrity, and Reproducibility** | Identify biases, misleading viz; ensure reproducible workflows; transparency practices | Input: All datasets; Output: Ethics checklist, reproducible repo structure | 2 hours |
| **14** | **Capstone: Conservation Analytics Dashboard** | End-to-end project; biodiversity/climate analysis; publication + interactive deliverables | Input: GBIF + climate datasets; Output: Research report, interactive dashboard, GitHub repo | 6-8 hours |

### **🧬 Specialized Omics Visualization Track (Optional Advanced Modules)**

| Module | Title | Learning Objectives | Inputs/Outputs | Estimated Time |
|--------|-------|--------------------|--------------------|-----------------|
| **15** | **Genomic Data Visualization Fundamentals** | ChIP-seq peaks, ATAC-seq accessibility, genome browsers; IGV-style track visualization | Input: ENCODE ChIP-seq/ATAC-seq; Output: Multi-track genome browser plots | 4 hours |
| **16** | **Epigenomic Deep Learning Model Visualization** | Attention maps, feature importance, embedding spaces; model interpretability for sequence models | Input: Trained CNN/Transformer models; Output: Model interpretation dashboards | 4-5 hours |
| **17** | **Multi-Omics Integration and Network Visualization** | Hi-C contact matrices, 3D genome structure, pathway networks; integrated omics analysis | Input: Multi-modal datasets (RNA+ATAC+Hi-C); Output: Interactive multi-omics dashboard | 5-6 hours |

**Total Estimated Time**: 35-45 hours (core) + 13-15 hours (omics track) = **48-60 hours comprehensive**

---

## 🛠 **Technical Stack**

### **Primary Libraries**
- **Core**: `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Interactive**: `plotly`, `altair`, `bokeh`
- **Geospatial**: `geopandas`, `folium`, `contextily`, `leafmap`
- **Raster**: `rasterio`, `rioxarray`, `xarray`
- **Big Data**: `datashader`, `hvplot`, `dask`
- **Maps**: `pydeck`, `keplergl`
- **Dashboards**: `streamlit`, `panel`

### **Specialized Omics Libraries** (Advanced Track)
- **Genomic Visualization**: `pyGenomeTracks`, `matplotlib`, `seaborn`
- **Sequence Analysis**: `biopython`, `pysam`, `pybedtools`
- **Hi-C Analysis**: `cooltools`, `cooler`, `hicstraw`
- **Deep Learning**: `torch`, `tensorflow`, `captum` (interpretability)
- **Network Analysis**: `networkx`, `igraph`, `pyvis`
- **3D Visualization**: `mayavi`, `plotly`, `pyvista`
- **Model Interpretation**: `shap`, `lime`, `integrated-gradients`

### **Environment Setup**
```yaml
# environment_dataviz.yml
name: dataviz_comprehensive
channels:
  - conda-forge
  - pyviz
dependencies:
  - python=3.9
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - plotly
  - altair
  - geopandas
  - folium
  - contextily
  - rasterio
  - rioxarray
  - datashader
  - streamlit
  - notebook
  - jupyterlab
```

---

## 📊 **Chart Selection Matrix**

| **Task** | **Recommended Charts** | **Encodings to Emphasize** | **Good Alternatives** | **Anti-Patterns to Avoid** |
|----------|------------------------|----------------------------|----------------------|---------------------------|
| **Compare categories** | Bar/column plot | Length/position for values; color for groups | Dot plot, lollipop chart | Pie charts (poor precision); 3D bars (distortion) |
| **Show distributions** | Histogram/KDE/violin | Position for bins; area for density | Box plot, beeswarm | Over-smoothed KDE; ignoring multimodality |
| **Trends over time** | Line plot | Position along x (time); y for value | Area chart, small multiples | Dual axes (false correlations); truncated y-axis |
| **Show relationships** | Scatter/hexbin | Position for variables; color/size for third dimension | Contour plot, pair plot | 3D scatter (hard to interpret); forcing lines on non-linear |
| **Part-to-whole** | Stacked bar | Length for proportions; color for parts | Treemap (if hierarchical) | Donut charts (like pie but worse); multiple pie charts |
| **Geospatial density** | Choropleth/hex bin | Color for intensity; position for location | Dot density, proportional symbols | Rainbow scales; no classification scheme |
| **Show uncertainty** | Error bars/CI bands | Lines for means; shading for intervals | Violin with quantiles | Hiding variability; overconfident point estimates |
| **Multiple comparisons** | Heatmap/small multiples | Color for values; grid position for groups | Parallel coordinates | Clustered bars >4 groups (visual clutter) |
| **Hierarchical data** | Treemap/sunburst | Area for values; nesting for hierarchy | Dendrogram, network diagram | Pie charts for hierarchies |
| **Change/flow** | Sankey/alluvial | Width for magnitude; flow for connections | Slope graph, stream graph | Arrow diagrams (cognitive overload) |

### **Quick Decision Tree**
1. **What type of data?** → Categorical (bars), Continuous (scatter/lines), Geographic (maps), Time (lines)
2. **What's the goal?** → Compare (bars), Trend (lines), Relationship (scatter), Distribution (histogram)
3. **How many variables?** → 1 (histogram), 2 (scatter), 3+ (color/size), Many (heatmap)
4. **Data size?** → Small (<1K), Medium (1K-100K), Large (>100K, use binning/sampling)

---

## 🎨 **Color & Accessibility Guide**

### **Recommended Palettes**
- **Qualitative (Categories)**: Okabe-Ito (8 colors, colorblind-safe), ColorBrewer Set2, Tableau 10
- **Sequential (Continuous)**: Viridis, Plasma, ColorBrewer Blues/Greens (perceptually uniform)
- **Diverging (±Center)**: ColorBrewer RdBu, RdYlBu, PiYG (emphasize deviation from midpoint)
- **Geographic**: Terrain-appropriate schemes, avoid jet/rainbow for scientific data

### **Accessibility Requirements**
- ✅ **Contrast Ratios**: 4.5:1 for normal text, 3:1 for large text/UI elements
- ✅ **Colorblind Testing**: Use Color Oracle, Coblis, or sim-daltonism tools
- ✅ **Alternative Encodings**: Patterns, shapes, labels alongside color
- ✅ **Typography**: Sans-serif fonts (Arial, Helvetica), 10-12pt minimum, bold for emphasis
- ✅ **Alt Text**: Describe chart type, data, key insights for screen readers

### **Publication Export Settings**
- **Print/Journal**: PDF/EPS, 300 DPI, CMYK, embedded fonts, vector when possible
- **Web/Presentation**: PNG, 150 DPI, RGB, optimized file size
- **Interactive**: SVG for scalability, consider mobile viewport
- **Figure Sizing**: 6"x4" single column, 8"x6" double column, consistent aspect ratios

### **Common Mistakes to Avoid**
- ❌ **Rainbow scales** for quantitative data (perceptual bias)
- ❌ **Red-green combinations** without alternatives (colorblind issues)
- ❌ **Too many colors** (>8 categories become indistinguishable)
- ❌ **Low contrast** combinations (fails accessibility standards)
- ❌ **Cultural assumptions** (red=bad varies by culture)

## 📊 **Uncertainty Visualization Cheat Sheet**

| **Method** | **When to Use** | **Appropriate For** | **Avoid When** |
|------------|-----------------|-------------------|----------------|
| **Confidence Intervals/Error Bars** | Showing sampling error in means; parametric estimates | Point estimates with known uncertainty | Multiple overlapping series (visual clutter) |
| **Confidence Bands** | Continuous functions (regression lines); forecast intervals | Time series predictions; trend uncertainty | Discrete data points |
| **Violin Plots** | Distribution shape matters; multimodal data | Comparing group distributions | Very small sample sizes (<10) |
| **Box Plots** | Quick summary statistics; outlier identification | Robust statistics needed | When distribution shape is important |
| **Ridge Plots** | Many groups to compare; evolution of distributions | Time series of distributions | Few groups (<3) |
| **Fan Charts** | Forecast uncertainty; widening confidence over time | Economic/climate projections | Historical data analysis |
| **Spaghetti Plots** | Multiple model runs; individual trajectories | Ensemble forecasts; bootstrap samples | Too many lines (>20, use alpha blending) |
| **Bootstrapped Distributions** | Non-parametric confidence; small samples | Robust uncertainty estimation | Large samples where CLT applies |
| **Quantile Plots** | Spatial uncertainty; risk visualization | Geographic risk maps; percentile displays | Simple point estimates sufficient |
| **Hypothetical Outcome Plots (HOPs)** | Animated uncertainty; engaging presentations | Public communication; education | Static reports; print publications |

### **Best Practices for Uncertainty**
- **Always explain what uncertainty represents** (sampling, measurement, model, forecast)
- **Choose appropriate confidence levels** (90%, 95%, 99% based on context)
- **Use visual hierarchy** (mean/median darker, uncertainty lighter)
- **Provide sample sizes** when showing confidence intervals
- **Consider your audience** (technical vs. general public)

## 🗺️ **Geospatial Visualization Deep Dive**

### **Vector Data Best Practices**
- **Classification Schemes**:
  - **Quantile**: Equal number of features per class (good for skewed data)
  - **Equal Interval**: Equal ranges (good for familiar units)
  - **Jenks Natural Breaks**: Minimize within-class variance (best for patterns)
  - **Manual**: Domain-specific breakpoints (policy thresholds)

- **When to Use Each Map Type**:
  - **Choropleth**: Rates, densities, percentages (normalize by area/population)
  - **Proportional Symbols**: Raw counts, totals (scale by circle area, not radius)
  - **Dot Density**: Population-like data (one dot = X people)
  - **Cartogram**: Emphasize variable over geography (area scaled by data)

### **Raster Data Strategies**
- **RGB Composites**:
  - **True Color**: Red=Red, Green=Green, Blue=Blue (natural appearance)
  - **False Color**: NIR=Red, Red=Green, Green=Blue (vegetation analysis)
  - **Color Infrared**: NIR=Red, Red=Green, Green=Blue (classic remote sensing)

- **Environmental Indices**:
  - **NDVI**: (NIR-Red)/(NIR+Red) → Vegetation health (-1 to +1)
  - **NDWI**: (Green-NIR)/(Green+NIR) → Water content
  - **NBR**: (NIR-SWIR)/(NIR+SWIR) → Burn severity

### **Interactive Map Guidelines**
- **Performance**: Tile-based rendering for large datasets
- **User Experience**: Zoom-dependent detail levels
- **Attribution**: Always credit data sources (OSM, satellite providers)
- **Coordinate Systems**: Web Mercator for web maps, equal-area for analysis

## 🔍 **Big Data Visualization Strategies**

### **Data Size Guidelines**
| **Data Size** | **Strategy** | **Tools** | **Considerations** |
|---------------|--------------|-----------|-------------------|
| **< 1,000 points** | Show all data | matplotlib, seaborn | Direct plotting, full interactivity |
| **1K - 10K points** | Transparency, jittering | plotly, altair | Alpha blending, avoid overplotting |
| **10K - 100K points** | Sampling, binning | pandas.sample(), hexbin | Representative subsets, 2D histograms |
| **100K - 1M points** | Aggregation, datashader | datashader, vaex | Rasterization, statistical summaries |
| **> 1M points** | Server-side rendering | hvplot, pydeck | Database integration, tile servers |

### **Sampling Strategies**
- **Random**: Representative of whole dataset
- **Stratified**: Preserve group proportions
- **Systematic**: Every nth observation
- **Cluster**: Sample geographic/temporal clusters

### **Performance Optimization**
- **Pre-compute aggregations** for common views
- **Use categorical data types** for memory efficiency
- **Implement progressive loading** for web dashboards
- **Cache intermediate results** to avoid recomputation

### **Module 5: Vector Geospatial Data**
**Focus**: Choropleth maps, classification schemes, coordinate systems

**Datasets**:
- Natural Earth Countries: https://www.naturalearthdata.com/downloads/
- US Census TIGER: https://www.census.gov/geographies/mapping-files/
- Global Administrative Database (GADM): https://gadm.org/

**Key Techniques**:
- **Classification Schemes**: Quantile, Equal Interval, Jenks Natural Breaks
- **Symbol Maps**: Proportional circles, graduated symbols
- **Dot Density**: Population visualization
- **Coordinate Systems**: Web Mercator vs. Equal Area projections

**When to Use / Avoid**:
- ✅ **Use Choropleth**: For rates, densities, percentages
- ❌ **Avoid Choropleth**: For raw counts (use proportional symbols)
- ✅ **Use Equal Area**: For area-based comparisons
- ❌ **Avoid Web Mercator**: For area comparisons at global scale

### **Module 6: Raster & Satellite Data**
**Focus**: Satellite imagery, elevation models, environmental indices

**Datasets**:
- Copernicus DEM: https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model
- Landsat Collection: https://earthexplorer.usgs.gov/
- MODIS Products: https://modis.gsfc.nasa.gov/data/
- Sentinel Hub: https://www.sentinel-hub.com/

**Key Techniques**:
- **RGB Composites**: True color, false color, infrared
- **Environmental Indices**: NDVI, NDWI, Burn severity
- **Hillshade**: Terrain visualization
- **Temporal Analysis**: Change detection, time series

### **Module 7: Interactive Maps**
**Focus**: Web-based mapping, user interaction, dynamic data

**Libraries Deep Dive**:
- **Folium**: Leaflet integration, choropleth plugins
- **Leafmap**: Jupyter-optimized mapping
- **Pydeck**: GPU-accelerated visualization
- **KeplerGL**: Geospatial data exploration

---

## 📈 **Module-by-Module Blueprint**

### **Module 1: Introduction to Data Visualization Principles**

**Concept Focus & Why It Matters**: Covers foundational theory (data-ink ratio, Gestalt principles) to build analytical viz skills, emphasizing communication over aesthetics. Poor visualization leads to misinterpretation in reports and decisions.

**Datasets**:
- **Gapminder** (global development indicators): https://www.gapminder.org/data/ (CC BY license; pre-process: filter 2000-2020, ~500 rows)
- **Palmer Penguins** (species measurements): https://github.com/allisonhorst/palmerpenguins (CC0 license; complete dataset, 344 rows)

**Visual Techniques Taught**: 
- Bar/line/scatter plots fundamentals
- *When to use*: Bars for categorical comparisons; lines for trends; scatters for relationships
- *When to avoid*: Bars for continuous data (use histogram); lines without temporal/ordinal structure

**Best Practices + Common Pitfalls + Smell Tests**:
- Use minimal ink; label axes clearly with units
- Pitfalls: 3D effects distort perception; truncated axes mislead; chart junk distracts
- Smell test: Can a stranger understand the main message in 10 seconds?

**Hands-On Tasks**:
- Load Gapminder data with pandas, explore structure
- Create matplotlib bar plot of life expectancy by continent
- Switch to seaborn for improved aesthetic defaults
- Defend chart choice in markdown cells with data type reasoning
- Apply "chart doctor" diagnostic to provided misleading examples

**Stretch Tasks**: 
- Add Plotly for hover interactivity; compare static vs interactive trade-offs
- Create small multiples showing trends by continent
- Design custom color palette following accessibility guidelines

**Expected Artifacts**: 3 publication-ready figures (PNG exports), 1-page chart selection rationale

**Assessment Rubric**:
- **Excellent (90-100%)**: Clear labels/units; justified choices; defends against alternatives; no visual distortions; accessibility considered
- **Good (80-89%)**: Appropriate chart types; basic best practices; some justification
- **Needs Work (<80%)**: Poor chart choices; missing labels; visual distortions present

**Prerequisites**: Basic pandas/numpy. **Success Criteria**: Produce defensible plots with clear reasoning. **Extension Ideas**: Integrate statistical annotations (confidence intervals, trend lines).

---

### **Module 2: Visual Best Practices and Accessibility**

**Concept Focus & Why It Matters**: Visual encodings (position, length, color); accessibility ensures inclusive communication, critical for diverse audiences in science and policy contexts.

**Datasets**:
- **NYC TLC Yellow Taxi Trips** (rides, fares, locations): https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page (public domain; pre-process: sample 10K rows, convert to CSV)

**Visual Techniques Taught**: 
- Customizing colors, scales, annotations
- *When to use*: Sequential colors for ordered data; categorical for groups
- *When to avoid*: Rainbow scales for quantitative data (perceptual bias); red-green without alternatives

**Best Practices + Common Pitfalls + Smell Tests**:
- Use ColorBrewer/Okabe-Ito palettes; check WCAG AA contrast ratios (4.5:1)
- Pitfalls: Overplotting obscures patterns; ignoring colorblind accessibility
- Smell test: Print in black & white—still readable? Test with colorblind simulator

**Hands-On Tasks**:
- Explore TLC trip data distributions and patterns
- Create seaborn bar plot with accessible color scheme
- Add comprehensive labels, titles, captions, and source attribution
- Redesign deliberately "bad" example charts provided
- Test visualizations with online accessibility tools

**Stretch Tasks**: 
- Implement Altair for declarative grammar of graphics
- Create interactive accessibility audit checklist
- Design visualization templates for organizational consistency

**Expected Artifacts**: Before/after figure comparisons, completed accessibility checklist, color palette guide

**Assessment Rubric**:
- **Excellent**: High contrast ratios; annotations enhance story; passes accessibility audit; no anti-patterns
- **Good**: Basic accessibility; clear improvements over original; some best practices
- **Needs Work**: Low contrast; missing accessibility features; unclear improvements

**Prerequisites**: Module 1. **Success Criteria**: Pass WCAG accessibility checks; demonstrate clear improvement. **Extension Ideas**: Typography optimization for web vs print; responsive design principles.

---

### **Module 3: Visualizing Distributions and Uncertainty**

**Concept Focus & Why It Matters**: Shows data variability and uncertainty; builds trust in analyses and is vital for environmental/climate data interpretation.

**Datasets**:
- **NOAA Global Summary of the Day (GSOD)** (weather station data): https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-day (public domain; pre-process: monthly temperature aggregates for major cities)

**Visual Techniques Taught**: 
- Histograms, KDE, violin, box plots; error bars, confidence intervals
- *When to use*: Violins for multimodal distributions; box plots for outlier identification
- *When to avoid*: Box plots for small samples (<10); KDE without sufficient data

**Best Practices + Common Pitfalls + Smell Tests**:
- Bootstrap confidence intervals for robustness; show raw data when possible
- Pitfalls: Over-smoothed KDE; ignoring outliers; hiding uncertainty
- Smell test: Does visualization show both central tendency AND variability?

**Hands-On Tasks**:
- Compute descriptive statistics on temperature data
- Create seaborn violin plots with confidence intervals
- Overlay bootstrapped error bars on group means
- Visualize prediction intervals for forecasting
- Compare uncertainty representation methods

**Stretch Tasks**: 
- Use scipy.stats for advanced statistical distributions
- Create ridge plots for temporal distribution evolution
- Implement Bayesian uncertainty visualization

**Expected Artifacts**: Distribution figures with multiple uncertainty representations, statistical interpretation report

**Assessment Rubric**:
- **Excellent**: Accurate uncertainty quantification; clear encoding interpretations; appropriate method selection
- **Good**: Basic uncertainty shown; adequate statistical understanding
- **Needs Work**: Missing uncertainty; incorrect statistical interpretation

**Prerequisites**: Modules 1-2, basic statistics. **Success Criteria**: Defend uncertainty visualization choices. **Extension Ideas**: Fan charts for forecast uncertainty; ensemble visualization.

---

### **Module 4: Time Series and Change Over Time**

**Concept Focus & Why It Matters**: Captures temporal dynamics; proper handling prevents misleading trend interpretation in monitoring applications (climate change, epidemiology).

**Datasets**:
- **Johns Hopkins COVID-19 Data Repository** (daily cases/deaths): https://github.com/CSSEGISandData/COVID-19 (CC BY 4.0; pre-process: US states, weekly resampling)

**Visual Techniques Taught**: 
- Line plots, area charts, small multiples, event annotations
- *When to use*: Small multiples for group comparisons; annotations for context
- *When to avoid*: Dual y-axes (misleading correlations); animation when static comparison suffices

**Best Practices + Common Pitfalls + Smell Tests**:
- Annotate major events; use uncertainty bands for projections; maintain consistent scales
- Pitfalls: Truncated y-axis exaggerates changes; dual axes create false correlations
- Smell test: Does y-axis start at appropriate baseline? Are trends genuinely comparable?

**Hands-On Tasks**:
- Resample COVID data to appropriate temporal resolution
- Create annotated matplotlib time series with event markers
- Use faceting for state-by-state comparisons
- Add reference lines for policy interventions
- Implement trend decomposition (seasonal, trend, residual)

**Stretch Tasks**: 
- Create cumulative vs. rate plots comparison
- Build Plotly animation showing geographic spread
- Implement change point detection algorithms

**Expected Artifacts**: Annotated time series portfolio, change detection analysis report

**Assessment Rubric**:
- **Excellent**: No misleading axes; clear temporal narrative; appropriate seasonal adjustments
- **Good**: Basic time series best practices; some context provided
- **Needs Work**: Misleading scales; missing temporal context; poor trend interpretation

**Prerequisites**: Module 3, basic time series concepts. **Success Criteria**: Identify and correct common temporal visualization pitfalls. **Extension Ideas**: Forecast uncertainty; regime change detection.

---

### **Module 7: Geospatial Visualization: Vector Data**

**Concept Focus & Why It Matters**: Maps biodiversity patterns and conservation habitats; vector data provides precise boundary representation for protected areas and species ranges.

**Datasets**:
- **Natural Earth** (world boundaries): https://www.naturalearthdata.com/downloads/ (public domain; 1:50m resolution)
- **GADM** (administrative boundaries): https://gadm.org/download_country.html (license varies by country; pre-process: clip to study regions)
- **GBIF Species Occurrences** (biodiversity): https://www.gbif.org/occurrence/search (CC BY 4.0; pre-process: filter by taxonomic group, convert to GeoDataFrame)

**Visual Techniques Taught**: 
- Choropleth maps, proportional symbols, dot density, hex binning
- *When to use*: Quantile classification for skewed data; Jenks for natural patterns
- *When to avoid*: Equal interval for highly skewed data; raw counts without normalization

**Best Practices + Common Pitfalls + Smell Tests**:
- Use appropriate projections (equal-area for analysis); classify data thoughtfully
- Pitfalls: Modifiable Areal Unit Problem (MAUP); web Mercator for area comparisons
- Smell test: Are map patterns real or artifacts of boundaries? Is projection appropriate?

**Hands-On Tasks**:
- Load and explore vector data with geopandas
- Create choropleth map of species richness by administrative unit
- Add proportional symbols for point data (protected areas)
- Implement hex binning for dense occurrence data
- Compare classification schemes (quantile vs. Jenks vs. equal interval)

**Stretch Tasks**: 
- Create dot density maps for population-like data
- Use shapely for spatial operations (buffers, intersections)
- Implement advanced cartographic techniques (relief shading)

**Expected Artifacts**: Vector map portfolio, habitat suitability analysis, classification comparison report

**Assessment Rubric**:
- **Excellent**: Proper coordinate systems; justified classifications; spatial analysis insights
- **Good**: Basic mapping competency; appropriate symbolization
- **Needs Work**: Projection errors; poor classification choices; missing spatial context

**Prerequisites**: Module 6, basic GIS concepts. **Success Criteria**: Perform accurate spatial joins and area calculations. **Extension Ideas**: Network analysis; accessibility modeling; least-cost path analysis.

---

## 🧬 **Advanced Omics Visualization Track**

### **Module 15: Genomic Data Visualization Fundamentals**

**Concept Focus & Why It Matters**: Genomic data requires specialized visualization approaches due to linear coordinate systems, multi-scale resolution (base pair to chromosome), and track-based organization. Essential for understanding regulatory landscapes and genomic features.

**Learning Objectives**:
- Visualize genomic intervals and peaks (ChIP-seq, ATAC-seq)
- Create genome browser-style track plots
- Handle genomic coordinates and annotations
- Design publication-quality genomic figures

**Datasets**:
- **ENCODE ChIP-seq**: https://www.encodeproject.org/ (H3K4me3, H3K27ac histone marks; public domain)
- **ENCODE ATAC-seq**: Chromatin accessibility data (various cell types; pre-process: peak calling with MACS2)
- **GENCODE Annotations**: https://www.gencodegenes.org/ (gene annotations GTF; public domain)
- **RefSeq Genes**: UCSC Table Browser (gene models; public domain)

**Visual Techniques Taught**:
- **Track-based visualization**: Stacked genomic tracks with proper scaling
- **Peak calling visualization**: ChIP-seq/ATAC-seq signal tracks with peak annotations
- **Genome browser plots**: IGV-style multi-track visualization
- **Genomic heatmaps**: Signal matrices around transcription start sites

**When to Use Each**:
- **Signal tracks**: Continuous data (ChIP-seq coverage, ATAC-seq signal)
- **Peak tracks**: Discrete intervals (called peaks, gene annotations)
- **Heatmaps**: Meta-analysis across multiple loci
- **Arc plots**: Long-range interactions (Hi-C, ChIA-PET)

**Best Practices + Common Pitfalls**:
- Use log scale for ChIP-seq signal (wide dynamic range)
- Maintain consistent genomic coordinates across tracks
- Pitfalls: Mixing different genome assemblies; ignoring strand information
- Color consistency: Same marks same colors across experiments

**Hands-On Tasks**:
- Load genomic data with pyGenomeTracks or matplotlib
- Create ChIP-seq signal track with peak overlays
- Build multi-track genome browser visualization
- Generate TSS-centered heatmaps for chromatin marks
- Compare accessibility patterns across cell types

**Stretch Tasks**:
- Implement interactive genome browser with bokeh
- Add sequence motif visualization
- Create chromatin state segmentation plots

**Expected Artifacts**: Genome browser-style figures, peak analysis plots, chromatin landscape visualization

**Assessment Rubric**:
- **Excellent**: Proper genomic coordinates; clear track organization; publication-ready formatting
- **Good**: Basic genomic visualization; appropriate scaling
- **Needs Work**: Coordinate errors; poor track alignment; unclear genomic context

**Prerequisites**: Module 6 (big data), basic genomics knowledge. **Success Criteria**: Create publication-quality genomic track plots. **Extension Ideas**: 3D genome visualization; comparative genomics.

---

### **Module 16: Epigenomic Deep Learning Model Visualization**

**Concept Focus & Why It Matters**: Deep learning models for genomic data are "black boxes" requiring specialized interpretability techniques. Essential for understanding what sequence features drive predictions and building trust in models for regulatory genomics.

**Learning Objectives**:
- Visualize CNN/Transformer attention patterns on genomic sequences
- Create feature importance maps for sequence motifs
- Design model training diagnostic plots
- Build model interpretation dashboards

**Datasets**:
- **Trained Models**: Pre-trained CNN models for chromatin accessibility prediction
- **DeepSEA**: http://deepsea.princeton.edu/ (sequence-based regulatory prediction)
- **Basenji**: https://github.com/calico/basenji (sequence-to-expression models)
- **Enformer**: https://github.com/deepmind/deepmind-research/tree/master/enformer (Transformer for gene expression)

**Visual Techniques Taught**:
- **Attention visualization**: Transformer attention heads on genomic sequences
- **Saliency maps**: Input gradient visualization for CNNs
- **Feature importance**: SHAP values for genomic positions
- **Embedding spaces**: t-SNE/UMAP of learned sequence representations
- **Model diagnostics**: Training curves, validation metrics, confusion matrices

**When to Use Each**:
- **Attention maps**: Understanding Transformer model focus
- **Saliency/gradient maps**: CNN feature importance
- **SHAP plots**: Model-agnostic interpretability
- **Embeddings**: Sequence similarity analysis
- **ROC/PR curves**: Model performance evaluation

**Best Practices + Common Pitfalls**:
- Use sequence logos for motif visualization
- Aggregate attention across multiple heads/layers
- Pitfalls: Over-interpreting individual attention patterns; ignoring model uncertainty
- Always validate interpretations with known biology

**Hands-On Tasks**:
- Extract and visualize CNN filter activations
- Create attention heatmaps for genomic sequences
- Generate SHAP importance plots for regulatory predictions
- Build t-SNE visualization of learned sequence embeddings
- Design model performance dashboard with plotly

**Stretch Tasks**:
- Implement integrated gradients for better attributions
- Create interactive sequence viewer with model predictions
- Compare attention patterns across different architectures

**Expected Artifacts**: Model interpretation plots, attention visualization dashboard, feature importance analysis

**Assessment Rubric**:
- **Excellent**: Biologically meaningful interpretations; proper statistical validation; clear model insights
- **Good**: Basic interpretability methods; reasonable biological context
- **Needs Work**: Misinterpretation of model outputs; insufficient biological validation

**Prerequisites**: Module 6 (interactivity), deep learning basics, genomics knowledge. **Success Criteria**: Generate interpretable model explanations. **Extension Ideas**: Adversarial example analysis; model uncertainty quantification.

---

### **Module 17: Multi-Omics Integration and Network Visualization**

**Concept Focus & Why It Matters**: Multi-omics integration requires sophisticated visualization to understand relationships between genomic layers (chromatin accessibility, gene expression, 3D structure). Critical for systems biology and precision medicine approaches.

**Learning Objectives**:
- Visualize Hi-C contact matrices and 3D genome structure
- Create integrated multi-omics heatmaps
- Design network visualizations for regulatory relationships
- Build comparative omics dashboards

**Datasets**:
- **4DN Hi-C**: https://data.4dnucleome.org/ (chromosome conformation; public domain)
- **TCGA Multi-omics**: https://portal.gdc.cancer.gov/ (RNA+methylation+CNV; controlled access)
- **ROADMAP Epigenomics**: http://www.roadmapepigenomics.org/ (multi-tissue chromatin states)
- **GTEx eQTL**: https://gtexportal.org/ (expression quantitative trait loci)

**Visual Techniques Taught**:
- **Hi-C heatmaps**: Contact matrices with proper normalization
- **Circos plots**: Genomic interactions and structural variants
- **Network diagrams**: Gene regulatory networks with networkx
- **Integrated heatmaps**: Multi-layer omics data matrices
- **3D genome visualization**: Chromatin structure with mayavi/plotly

**When to Use Each**:
- **Contact heatmaps**: Hi-C, ChIA-PET interaction data
- **Circos plots**: Genome-wide structural variations
- **Network graphs**: Regulatory relationships, protein interactions
- **Clustered heatmaps**: Multi-omics data integration
- **3D plots**: Spatial genome organization

**Best Practices + Common Pitfalls**:
- Proper Hi-C matrix normalization (ICE, KR methods)
- Consistent color scales across omics layers
- Pitfalls: Over-cluttered network layouts; ignoring batch effects
- Statistical significance testing for interactions

**Hands-On Tasks**:
- Process and visualize Hi-C contact matrices with cooltools
- Create Circos-style genome plots with matplotlib
- Build gene regulatory networks with networkx
- Design integrated multi-omics heatmaps
- Implement 3D genome structure visualization

**Stretch Tasks**:
- Create interactive 3D genome browser
- Implement topologically associating domain (TAD) detection
- Build comparative Hi-C analysis dashboard

**Expected Artifacts**: Hi-C contact maps, regulatory network diagrams, integrated omics dashboard

**Assessment Rubric**:
- **Excellent**: Proper normalization; biologically meaningful integrations; clear multi-scale visualization
- **Good**: Basic multi-omics visualization; appropriate statistical methods
- **Needs Work**: Poor data integration; missing statistical validation; unclear biological interpretation

**Prerequisites**: Module 16, advanced genomics, network analysis basics. **Success Criteria**: Create integrated multi-omics analysis with clear biological insights. **Extension Ideas**: Single-cell multi-omics; dynamic network analysis; machine learning integration.

---

## 🔍 **Big Data Strategies (Module 8)**

### **Challenge**: Visualizing millions of points effectively

**Datasets**:
- **NYC Taxi Trips**: TLC sample (10M+ records)
- **Satellite Imagery**: Landsat pixel data
- **Social Media**: Twitter geotagged sample

**Techniques**:
1. **Sampling**: Random, stratified, systematic
2. **Binning**: Hexagonal, square grids
3. **Datashader**: Rasterization for large datasets
4. **Level-of-Detail**: Zoom-dependent visualization
5. **Server-side**: Tile-based rendering

**Performance Guidelines**:
- **< 1K points**: Show all points
- **1K - 100K**: Consider transparency, jittering
- **100K - 1M**: Use binning, sampling
- **> 1M**: Datashader, server-side rendering

---

## 📱 **Dashboard Design Principles (Module 11)**

### **Layout Guidelines**:
- **F-Pattern**: Most important info top-left
- **Grid System**: Consistent spacing and alignment
- **Information Hierarchy**: Size, color, position
- **Progressive Disclosure**: Start simple, allow drilling down

### **Interactivity Patterns**:
- **Filtering**: Dropdowns, sliders, checkboxes
- **Linked Brushing**: Selection across multiple charts
- **Drill-down**: Summary to detail views
- **Tooltips**: Additional context on demand

### **Performance Considerations**:
- **Caching**: Pre-compute aggregations
- **Lazy Loading**: Load data on demand
- **Debouncing**: Limit rapid updates
- **Memory Management**: Limit data in browser

---

## 🎯 **Capstone Project: Conservation Analytics Dashboard**

### **Project Options** (Choose One):

#### **Option A: Madagascar Biodiversity Hotspots**
**Question**: Where are conservation priorities for endemic species?

**Datasets**:
- **GBIF Species Occurrences**: https://www.gbif.org/
- **Protected Areas**: WDPA database
- **Land Cover**: ESA WorldCover
- **Climate Data**: WorldClim bioclimatic variables

**Analysis Plan**:
1. Species richness mapping
2. Threat assessment (deforestation, climate change)
3. Conservation gap analysis
4. Priority area identification

**Visualization Plan**:
- Interactive species occurrence maps
- Threat assessment dashboards
- Conservation priority matrices
- Time series of land cover change

#### **Option B: Urban Air Quality & Health**
**Question**: How does air pollution affect urban health outcomes?

**Datasets**:
- **Air Quality**: OpenAQ, EPA AirNow
- **Health Data**: CDC, local health departments
- **Demographics**: Census ACS
- **Land Use**: OSM, local GIS

**Analysis Plan**:
1. Spatial interpolation of air quality
2. Health outcome correlation analysis
3. Environmental justice assessment
4. Policy intervention scenarios

#### **Option C: Climate Change Impacts**
**Question**: How is climate change affecting regional ecosystems?

**Datasets**:
- **Climate**: NOAA, ERA5 reanalysis
- **Vegetation**: MODIS NDVI time series
- **Phenology**: USA-NPN, eMODIS
- **Species**: eBird, iNaturalist

**Deliverables**:
1. **Static Report**: 15-page analysis with publication-quality figures
2. **Interactive Dashboard**: Streamlit app with multiple views
3. **Technical Documentation**: Methodology, data sources, limitations
4. **Presentation**: 10-minute stakeholder presentation

**Grading Rubric**:
- **Data Processing** (20%): Clean, well-documented pipeline
- **Visual Design** (25%): Follows best practices, accessible
- **Analysis Quality** (25%): Appropriate methods, valid conclusions
- **Communication** (20%): Clear narrative, actionable insights
- **Technical Excellence** (10%): Code quality, reproducibility

---

## ⚡ **Getting Started Quickly**

### **Environment Setup** (15 minutes):
```bash
# Clone repository
git clone https://github.com/SanjeevaRDodlapati/GeoSpatialAI.git
cd GeoSpatialAI/projects/project_dataviz_comprehensive_series

# Create conda environment from spec
conda env create -f environment_dataviz.yml
conda activate dataviz_comprehensive

# Verify installation
python scripts/test_environment.py

# Download sample datasets
python scripts/download_sample_data.py

# Launch Jupyter Lab
jupyter lab
```

### **Quick Start Learning Path** (2-3 hours total):
If you only have limited time, focus on these **3 essential modules** first:

1. **Module 1: Fundamentals** (1 hour)
   - Core visualization principles
   - Chart selection framework
   - Basic matplotlib/seaborn skills

2. **Module 9: Color & Accessibility** (30 minutes)
   - Accessible color palettes
   - WCAG compliance basics
   - Quick wins for better design

3. **Module 5: Basic Geospatial** (1 hour)
   - Simple choropleth maps
   - Coordinate systems basics
   - Real-world conservation examples

**Why This Order?** These modules provide maximum practical value and can be immediately applied to any visualization project.

### **Environment Specification**:
```yaml
# environment_dataviz.yml
name: dataviz_comprehensive
channels:
  - conda-forge
  - bioconda  # For genomics tools
  - pyviz
dependencies:
  - python=3.10
  - pandas=1.5
  - numpy=1.24
  - matplotlib=3.6
  - seaborn=0.12
  - plotly=5.11
  - altair=4.2
  - geopandas=0.12
  - contextily=1.2
  - folium=0.14
  - leafmap=0.9
  - pydeck=0.8
  - shapely=2.0
  - rasterio=1.3
  - rioxarray=0.13
  - datashader=0.14
  - holoviews=1.15
  - streamlit=1.15
  - panel=0.14
  - jupyterlab=3.5
  # Omics-specific libraries
  - biopython=1.81
  - pysam=0.21
  - pybedtools=0.9
  - networkx=3.1
  - scikit-learn=1.3
  - pytorch=2.0
  - pip
  - pip:
    - papermill
    - keplergl
    - plotly-dash
    - pyGenomeTracks
    - cooltools
    - cooler
    - shap
    - captum  # PyTorch model interpretability
    - pyvis  # Interactive networks
    - pyvista  # 3D visualization
```

---

## 📊 **Datasets Repository**

All datasets include **direct download links**, **preprocessing notes**, and **license information**:

### **Core Learning Datasets**
| Dataset | Description | Size | License | Preprocessing |
|---------|-------------|------|---------|---------------|
| **Gapminder** | Global development indicators (GDP, life expectancy) | ~1,700 rows | CC BY 4.0 | Filter 2000-2020; handle missing values |
| **Palmer Penguins** | Antarctic penguin species measurements | 344 rows | CC0 | Complete dataset; categorical encoding |
| **NYC TLC Yellow Taxi** | Taxi trip records (pickup, dropoff, fare) | Sample 10K | Public Domain | Sample large files; convert datetime |
| **NOAA GSOD Climate** | Daily weather station summaries | Variable | Public Domain | Aggregate to monthly; quality control flags |
| **Johns Hopkins COVID-19** | Daily case/death counts by location | ~100K rows | CC BY 4.0 | Resample to weekly; geographic joins |

### **Geospatial Datasets**
| Dataset | Description | Format | Source | Usage Notes |
|---------|-------------|---------|--------|-------------|
| **Natural Earth Countries** | World political boundaries | Shapefile | https://www.naturalearthdata.com/downloads/ | 1:50m resolution; includes attributes |
| **GADM Administrative** | Country administrative boundaries | Shapefile | https://gadm.org/download_country.html | License varies; clip to regions |
| **GBIF Species Occurrences** | Biodiversity observation records | CSV/JSON | https://www.gbif.org/occurrence/search | Filter by taxon; coordinate validation |
| **Copernicus DEM** | Global elevation model | GeoTIFF | https://spacedata.copernicus.eu/ | 30m resolution; clip to study areas |
| **OpenStreetMap** | Geographic features | Various | https://www.openstreetmap.org/ | Use overpass API; attribution required |

### **Specialized Analysis Datasets**
| Dataset | Description | Application | Download Command | Processing Notes |
|---------|-------------|-------------|------------------|------------------|
| **OpenAQ Air Quality** | Global air pollution monitoring | Environmental health | `wget https://openaq-data.s3.amazonaws.com/` | Temporal aggregation needed |
| **Global Forest Watch** | Deforestation alerts | Conservation | API access via `gfwpy` | Requires registration |
| **World Bank Indicators** | Economic/social development | Comparative analysis | `pip install wbdata` | Multiple indicators available |
| **NASA MODIS** | Satellite vegetation indices | Remote sensing | Earth Explorer | Large files; cloud masking |

### **Sample Data Download Script**:
```bash
#!/bin/bash
# download_sample_data.sh

# Create data directories
mkdir -p data/{raw,processed,external}

# Core datasets
wget https://raw.githubusercontent.com/plotly/datasets/master/gapminder.csv -O data/raw/gapminder.csv
wget https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv -O data/raw/penguins.csv

# NYC TLC sample (10K rows)
wget "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet" -O data/raw/nyc_taxi_sample.parquet

# Natural Earth boundaries
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip -O data/raw/countries.zip
unzip data/raw/countries.zip -d data/raw/

# Climate data sample
wget "https://www1.ncdc.noaa.gov/pub/data/gsod/2023/gsod_2023.tar" -O data/raw/climate_2023.tar

echo "✅ Sample datasets downloaded successfully!"
echo "📁 Check data/raw/ directory for files"
echo "🔄 Run preprocessing: python scripts/preprocess_data.py"
```

---

## 🎯 **Capstone Project: Biodiversity Conservation Analytics**

### **Project Overview**
Design and implement a comprehensive conservation analytics dashboard that combines multiple data sources to inform protected area management and species conservation priorities.

### **Three Project Options** (Choose One):

#### **Option A: Madagascar Endemic Species Conservation**
**Research Question**: Where should new protected areas be established to maximize endemic species conservation?

**Datasets**:
- **GBIF Madagascar Occurrences**: Endemic lemur, reptile, and plant species
- **Madagascar Protected Areas**: WDPA database + local government data
- **Land Cover Change**: ESA WorldCover time series (2016-2021)
- **Threat Indicators**: Deforestation alerts, road network, population density
- **Climate Variables**: WorldClim current + future projections

**Analysis Workflow**:
1. Species richness and endemism mapping
2. Habitat suitability modeling (MaxEnt-style analysis)
3. Threat assessment and vulnerability scoring
4. Conservation gap analysis (protected vs. unprotected habitats)
5. Climate change impact modeling
6. Priority area identification using systematic conservation planning

**Visualization Deliverables**:
- Interactive species occurrence maps (Folium/Leafmap)
- Threat assessment dashboard (Streamlit)
- Conservation priority matrix (static + interactive)
- Climate impact scenarios (animated time series)
- Policy briefing report (publication-quality figures)

#### **Option B: Urban Air Quality & Environmental Justice**
**Research Question**: How does air pollution exposure vary across demographic groups, and where are interventions most needed?

**Datasets**:
- **Air Quality Monitoring**: OpenAQ, EPA AirNow (PM2.5, NO2, O3)
- **Demographics**: US Census American Community Survey
- **Health Outcomes**: CDC PLACES (asthma, cardiovascular disease)
- **Land Use**: USGS NLCD, OpenStreetMap (roads, industry)
- **Social Vulnerability**: CDC SVI index

**Analysis Workflow**:
1. Spatial interpolation of air quality measurements
2. Demographic disparity analysis
3. Health outcome correlation assessment
4. Environmental justice screening
5. Source attribution (traffic, industrial, natural)
6. Intervention scenario modeling

#### **Option C: Climate Change Ecosystem Monitoring**
**Research Question**: How are regional ecosystems responding to changing climate conditions?

**Datasets**:
- **Climate Data**: NOAA/NCEI temperature, precipitation records
- **Vegetation**: MODIS NDVI time series (2000-2023)
- **Phenology**: USA National Phenology Network
- **Species Observations**: eBird, iNaturalist citizen science
- **Extreme Events**: NOAA Storm Events database

**Analysis Workflow**:
1. Climate trend analysis and change detection
2. Vegetation response correlation (NDVI vs. climate)
3. Phenological shift quantification
4. Species distribution modeling under climate scenarios
5. Ecosystem vulnerability assessment
6. Adaptation planning recommendations

#### **Option D: Epigenomic Deep Learning Model Interpretability** (Advanced Omics Track)
**Research Question**: How do deep learning models identify regulatory sequences, and what biological insights can we extract?

**Datasets**:
- **ENCODE ChIP-seq/ATAC-seq**: Multi-cell type regulatory data
- **Pre-trained Models**: Basenji, Enformer, or custom CNN models
- **Sequence Annotations**: GENCODE genes, repeat elements, transcription factor motifs
- **Validation Data**: Independent experimental datasets for model validation

**Analysis Workflow**:
1. Model performance evaluation across cell types and marks
2. Attention pattern analysis for regulatory sequence identification
3. Feature importance mapping using SHAP/integrated gradients
4. Sequence motif discovery and validation
5. Model uncertainty quantification
6. Biological insight extraction and hypothesis generation

**Visualization Plan**:
- Interactive genome browser with model predictions
- Attention heatmaps overlaid on genomic tracks
- Feature importance dashboards for different cell types
- Model performance comparison across architectures
- Regulatory network visualization from model insights

### **Technical Requirements**:
- **Static Report**: 15-page analysis with publication-quality figures (300 DPI)
- **Interactive Dashboard**: Multi-panel Streamlit application
- **Code Repository**: Well-documented GitHub repo with reproducible analysis
- **Data Pipeline**: Automated download and preprocessing scripts
- **Presentation**: 10-minute stakeholder briefing with key findings

### **Assessment Rubric**:
| **Criteria** | **Excellent (A)** | **Good (B)** | **Needs Improvement (C)** |
|--------------|-------------------|--------------|---------------------------|
| **Data Processing (20%)** | Clean, automated pipeline; handles edge cases | Some automation; basic quality control | Manual processing; limited validation |
| **Visual Design (25%)** | Publication-ready; accessible; tells clear story | Good aesthetics; mostly accessible | Basic plots; some design issues |
| **Analysis Quality (25%)** | Sophisticated methods; valid statistical inference | Appropriate methods; reasonable conclusions | Basic analysis; questionable methods |
| **Communication (20%)** | Compelling narrative; actionable insights | Clear presentation; logical flow | Unclear message; limited insights |
| **Technical Excellence (10%)** | Reproducible; well-documented; efficient code | Mostly reproducible; decent documentation | Hard to reproduce; poor documentation |

### **Timeline Suggestions**:
- **Week 1**: Data acquisition and exploration
- **Week 2**: Preprocessing and quality control  
- **Week 3**: Core analysis and modeling
- **Week 4**: Visualization development
- **Week 5**: Dashboard building and integration
- **Week 6**: Report writing and presentation preparation

---

## 📚 **Pedagogy & Supporting Materials**

### **Per-Module Structure**:
Each module follows consistent pedagogical design:
- **🎯 Learning Objectives**: Specific, measurable outcomes
- **📚 Theoretical Foundation**: Key concepts with visual examples
- **🛠️ Hands-On Practice**: Guided exercises with real data
- **💪 Challenge Tasks**: Advanced applications and extensions
- **📊 Portfolio Artifacts**: Concrete deliverables for assessment
- **🔍 Self-Assessment**: Rubrics and reflection prompts

### **Assessment Philosophy**:
- **Formative**: Continuous feedback through exercises and peer review
- **Summative**: Portfolio-based evaluation emphasizing real-world application
- **Authentic**: Tasks mirror professional data visualization contexts
- **Inclusive**: Multiple pathways to demonstrate mastery

### **Repository Structure**:
```
project_dataviz_comprehensive_series/
├── README.md                          # Project overview and setup
├── DATAVIZ_TUTORIAL_MASTER_PLAN.md   # This comprehensive plan
├── environment_dataviz.yml           # Conda environment specification
├── notebooks/                        # 14 tutorial modules
│   ├── 01_fundamentals.ipynb
│   ├── 02_accessibility.ipynb
│   └── ...
├── data/                             # Datasets and examples
│   ├── raw/                          # Original downloaded data
│   ├── processed/                    # Clean, analysis-ready data
│   └── external/                     # Large files (referenced, not stored)
├── scripts/                          # Utility and setup scripts
│   ├── download_sample_data.py
│   ├── test_environment.py
│   └── preprocess_data.py
├── assets/                           # Reference materials
│   ├── chart_selection_guide.md
│   ├── color_palette_reference.md
│   └── accessibility_checklist.md
└── outputs/                          # Generated visualizations
    ├── figures/                      # Static plots
    └── dashboards/                   # Interactive applications
```

### **Quality Assurance**:
- **Peer Review**: Students evaluate each other's work using provided rubrics
- **Expert Validation**: Industry professionals review capstone projects
- **Continuous Improvement**: Regular updates based on learner feedback
- **Accessibility Audit**: All materials tested for universal design compliance

---

## � **Appendix: Quick Reference Assets**

### **"Chart Doctor" Decision Flowchart**
```
START: What type of data do you have?
│
├─ CATEGORICAL ──────────────────────────────────────┐
│   │                                                │
│   ├─ Few categories (<5) ── Bar chart               │
│   ├─ Many categories (>5) ── Horizontal bar         │
│   ├─ Part-to-whole ── Stacked bar, treemap         │
│   └─ Hierarchical ── Treemap, sunburst             │
│                                                     │
├─ CONTINUOUS ──────────────────────────────────────┤
│   │                                                │
│   ├─ Single variable ── Histogram, box plot        │
│   ├─ Two variables ── Scatter plot                 │
│   ├─ Multiple variables ── Correlation matrix      │
│   └─ Distribution comparison ── Violin, ridge      │
│                                                     │
├─ TIME SERIES ─────────────────────────────────────┤
│   │                                                │
│   ├─ Single series ── Line chart                   │
│   ├─ Multiple series ── Small multiples            │
│   ├─ Seasonal patterns ── Heatmap calendar         │
│   └─ Uncertainty ── Confidence bands               │
│                                                     │
└─ GEOSPATIAL ─────────────────────────────────────┘
    │
    ├─ Point data ── Dot map, proportional symbols
    ├─ Area data ── Choropleth, cartogram
    ├─ Raster data ── Heat map, contour
    └─ Networks ── Node-link, arc diagram

DECISION FACTORS:
✓ Data size: <1K (show all), 1K-100K (sample), >100K (aggregate)
✓ Audience: Expert (complex OK), General (simple)
✓ Purpose: Explore (interactive), Present (static), Publish (high-quality)
```

### **Figure Quality Checklist**
Before publishing any visualization, verify:

**📊 Content & Accuracy**
- [ ] Title clearly states the main message
- [ ] Subtitle provides context or key insight  
- [ ] Caption explains methodology and data source
- [ ] All axes labeled with units
- [ ] Legend is necessary and well-positioned
- [ ] Data source and date are cited
- [ ] Sample sizes shown when relevant

**🎨 Design & Aesthetics**
- [ ] Color palette is accessible (colorblind-safe)
- [ ] Contrast ratios meet WCAG AA standards (4.5:1)
- [ ] Font sizes are readable (≥10pt for print, ≥12pt for web)
- [ ] Visual hierarchy guides attention appropriately
- [ ] Chart junk eliminated (unnecessary 3D, grid lines, etc.)
- [ ] Consistent styling across related figures

**📐 Technical Quality**
- [ ] Appropriate chart type for data and message
- [ ] Scales start at meaningful baselines (zero for bars)
- [ ] No misleading visual elements (truncated axes, dual y-axes)
- [ ] Resolution appropriate for medium (300 DPI print, 150 DPI web)
- [ ] File format suitable (PNG for web, PDF/SVG for print)
- [ ] Color space appropriate (RGB for web, CMYK for print)

### **Publication Export Settings Reference**

| **Output Type** | **Format** | **DPI** | **Color** | **Size** | **Fonts** |
|-----------------|------------|---------|-----------|----------|-----------|
| **Web/Blog** | PNG | 150 | RGB | 800x600px | Web-safe fonts |
| **Presentation** | PNG/SVG | 150 | RGB | 1920x1080px | Sans-serif, large |
| **Journal Paper** | PDF/EPS | 300-600 | CMYK | 6"x4" (single column) | Embedded fonts |
| **Poster** | PDF/SVG | 300 | CMYK | Full size | Vector when possible |
| **Social Media** | PNG | 72-150 | RGB | Platform-specific | Bold, readable |
| **Dashboard** | SVG | Vector | RGB | Responsive | System fonts |

**Matplotlib Export Code**:
```python
# High-quality figure export
plt.savefig('figure.pdf', 
           dpi=300, 
           bbox_inches='tight',
           format='pdf',
           facecolor='white',
           edgecolor='none',
           transparent=False)

# For journals requiring specific formats
plt.rcParams['pdf.fonttype'] = 42  # Embed fonts as outlines
plt.rcParams['ps.fonttype'] = 42   # For EPS files
```

### **Visualization Design Brief Template**

Use this template to plan visualizations systematically:

**Project**: _________________________
**Date**: _________________________

**1. Audience Analysis**
- Primary audience: _________________________
- Technical expertise level: _________________________  
- Decision-making context: _________________________
- Time available for interpretation: _________________________

**2. Communication Objectives**
- Main message: _________________________
- Key insights to highlight: _________________________
- Call to action: _________________________
- Success criteria: _________________________

**3. Data Characteristics**
- Data source: _________________________
- Sample size: _________________________
- Variables of interest: _________________________
- Data quality issues: _________________________
- Update frequency: _________________________

**4. Design Constraints**
- Medium (print/web/presentation): _________________________
- Size limitations: _________________________
- Color restrictions: _________________________
- Accessibility requirements: _________________________
- Branding guidelines: _________________________

**5. Visualization Plan**
- Chart type rationale: _________________________
- Visual encodings: _________________________
- Color strategy: _________________________
- Interaction requirements: _________________________
- Alternative formats needed: _________________________

### **Common Anti-Patterns to Avoid**

| **Anti-Pattern** | **Why It's Bad** | **Better Alternative** |
|------------------|------------------|------------------------|
| **Pie charts >5 slices** | Hard to compare angles | Horizontal bar chart |
| **3D effects** | Distorts perception | Clean 2D design |
| **Dual y-axes** | Implies false correlation | Small multiples |
| **Rainbow color scales** | Not perceptually uniform | Viridis, ColorBrewer |
| **Truncated bar charts** | Exaggerates differences | Start bars at zero |
| **Too many colors** | Overwhelming, inaccessible | Limit to 5-8 colors max |
| **Misleading baselines** | Distorts magnitude | Use appropriate zero point |
| **Cluttered legends** | Reduces comprehension | Direct labeling |
| **Inconsistent scales** | Prevents comparison | Standardize across panels |
| **Missing error bars** | Overstates certainty | Show uncertainty |

### **Accessibility Quick Reference**

**Color Guidelines**:
- Use ColorBrewer or Okabe-Ito palettes
- Ensure 4.5:1 contrast ratio for text
- Provide pattern alternatives to color
- Test with colorblind simulation tools

**Typography**:
- Minimum 10pt for print, 12pt for web
- Sans-serif fonts (Arial, Helvetica, Calibri)
- Bold for emphasis, not color alone
- High contrast between text and background

**Alt Text Templates**:
- **Chart type**: "Bar chart showing..."
- **Variables**: "X-axis: time, Y-axis: temperature"  
- **Key findings**: "Trend shows 2°C increase over 20 years"
- **Data context**: "Based on 50 weather stations, 2000-2020"

### **Glossary of Data Visualization Terms**

**Aesthetic**: Visual property used to represent data (position, color, size, shape)

**Binning**: Grouping continuous data into discrete intervals for visualization

**Chart Junk**: Unnecessary visual elements that don't represent data

**Color Gamut**: Range of colors that can be displayed or printed

**Data-Ink Ratio**: Proportion of visualization that represents data vs. decoration

**Encoding**: Mapping data values to visual properties

**Faceting**: Creating multiple plots for subsets of data (small multiples)

**Gestalt Principles**: Psychology of visual perception (proximity, similarity, closure)

**Grammar of Graphics**: Theoretical framework for building visualizations systematically

**Information Density**: Amount of data represented per unit of visual space

**Modifiable Areal Unit Problem (MAUP)**: Geographic analysis results vary with boundary choices

**Overplotting**: Points obscuring each other in dense scatter plots

**Perceptual Uniformity**: Equal visual differences represent equal data differences

**Small Multiples**: Series of similar charts showing different subsets

**Visual Hierarchy**: Design elements that guide attention to most important information

---

*This comprehensive master plan provides the foundation for a world-class data visualization curriculum that bridges technical skills with communication excellence, ethical practice, and real-world application.*
