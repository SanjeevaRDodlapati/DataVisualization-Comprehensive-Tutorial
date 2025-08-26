# Chart Selection Flowchart

## Quick Decision Tree for Chart Selection

### Step 1: What type of data do you have?

#### 📊 **Categorical Data**
- **Single Category**: Bar chart, dot plot
- **Multiple Categories**: Grouped bar chart, stacked bar chart
- **Hierarchical**: Treemap, sunburst chart
- **Part-to-Whole**: Pie chart (≤5 categories), waffle chart

#### 📈 **Numerical Data**
- **Single Variable**: Histogram, box plot, violin plot
- **Two Variables**: Scatter plot, line chart (if time-ordered)
- **Multiple Variables**: Correlation matrix, parallel coordinates

#### 🗓️ **Time Series Data**
- **Single Series**: Line chart, area chart
- **Multiple Series**: Small multiples, grouped line chart
- **With Uncertainty**: Confidence bands, fan charts

#### 🗺️ **Geospatial Data**
- **Point Data**: Dot maps, proportional symbols
- **Area Data**: Choropleth maps, cartograms
- **Raster Data**: Heat maps, satellite imagery

### Step 2: What is your primary goal?

#### 🔍 **Compare Values**
- **Few Categories**: Bar chart, dot plot
- **Many Categories**: Horizontal bar chart, cleveland dot plot
- **Over Time**: Line chart, slope graph

#### 📊 **Show Distribution**
- **Single Distribution**: Histogram, density plot
- **Multiple Distributions**: Box plots, violin plots
- **Compare Distributions**: Ridge plots, small multiples

#### 🔄 **Show Relationship**
- **Correlation**: Scatter plot, correlation matrix
- **Causation**: Before/after plots, slope graphs
- **Part-to-Whole**: Stacked charts, pie charts

#### 📍 **Show Location/Spatial**
- **Geographic**: Choropleth, dot density
- **Network**: Node-link diagrams, arc diagrams
- **Hierarchical**: Tree diagrams, dendrograms

### Step 3: What encodings should you use?

#### 🎯 **Most Effective Encodings** (in order of effectiveness)
1. **Position** (x, y coordinates)
2. **Length** (bar length)
3. **Angle** (pie slices - use sparingly)
4. **Area** (bubble size)
5. **Color** (hue, saturation, lightness)
6. **Texture/Pattern** (accessibility backup)

### Step 4: Accessibility and Design Checklist

#### ♿ **Accessibility**
- [ ] Color-blind safe palette (ColorBrewer, Okabe-Ito)
- [ ] Sufficient contrast ratios (4.5:1 for text)
- [ ] Alternative encodings beyond color
- [ ] Descriptive titles and labels
- [ ] Alt text for screen readers

#### 🎨 **Design Excellence**
- [ ] Clear, descriptive title
- [ ] Axis labels with units
- [ ] Legend when needed (but prefer direct labeling)
- [ ] Appropriate aspect ratio
- [ ] Remove chart junk
- [ ] Consistent color usage

## Quick Reference: Common Chart Types

| **Data Type** | **Primary Use** | **Best Chart** | **Avoid** |
|---------------|-----------------|----------------|-----------|
| Categorical comparison | Compare categories | Bar chart | Pie chart (>5 categories) |
| Time series | Show trend over time | Line chart | Bar chart |
| Distribution | Show data spread | Histogram | Pie chart |
| Correlation | Show relationship | Scatter plot | Bar chart |
| Geographic | Show spatial patterns | Choropleth | 3D maps |
| Part-to-whole | Show proportions | Stacked bar | Multiple pie charts |
| Ranking | Show order | Horizontal bar | Vertical bar (many items) |

## Advanced Considerations

### **When to Use Small Multiples**
- Comparing multiple groups
- Time series by category
- Geographic regions
- Different scenarios/models

### **When to Use Animation**
- Showing change over time
- Storytelling presentations
- User exploration tools
- **Avoid for**: Static reports, printed materials

### **When to Use Interaction**
- Large datasets needing filtering
- Multiple dimensions to explore
- User-driven exploration
- Dashboard applications

### **Color Strategy**
- **Qualitative**: Distinct hues for categories
- **Sequential**: Single hue, varying lightness
- **Diverging**: Two hues meeting at neutral
- **Highlight**: Gray + one accent color

## Common Mistakes to Avoid

❌ **Don't**:
- Use pie charts for >5 categories
- Truncate y-axis without clear justification
- Use dual y-axes (use small multiples instead)
- Rely only on color to encode information
- Use 3D effects unnecessarily
- Create misleading scales

✅ **Do**:
- Start y-axis at zero for bar charts
- Use consistent color meanings
- Provide clear titles and labels
- Consider your audience's expertise
- Test with colorblind viewers
- Iterate based on feedback
