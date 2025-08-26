# Color Palette Reference

## Quick Access Color Palettes for Data Visualization

### 🌈 Qualitative Palettes (Categorical Data)

#### **Okabe-Ito (Colorblind-Safe)**
```python
okabe_ito = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', 
             '#0072B2', '#D55E00', '#CC79A7', '#000000']
```
- **Use for**: Categorical data (up to 8 categories)
- **Advantage**: Universally accessible, distinct colors
- **Example**: Different species, product categories, regions

#### **Set1 (Vibrant)**
```python
set1 = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', 
        '#FF7F00', '#FFFF33', '#A65628', '#F781BF']
```
- **Use for**: Presentations, highlights (up to 8 categories)
- **Advantage**: High contrast, attention-grabbing
- **Example**: Political parties, survey responses

#### **Dark2 (Professional)**
```python
dark2 = ['#1B9E77', '#D95F02', '#7570B3', '#E7298A',
         '#66A61E', '#E6AB02', '#A6761D', '#666666']
```
- **Use for**: Professional reports, academic papers
- **Advantage**: Sophisticated, muted tones
- **Example**: Research categories, business segments

### 📊 Sequential Palettes (Continuous Data)

#### **Blues (Classic)**
```python
blues = ['#F7FBFF', '#DEEBF7', '#C6DBEF', '#9ECAE1',
         '#6BAED6', '#4292C6', '#2171B5', '#084594']
```
- **Use for**: Intensity, concentration, probability
- **Example**: Population density, temperature, confidence

#### **Viridis (Perceptually Uniform)**
```python
viridis = ['#440154', '#482878', '#3E4A89', '#31688E',
           '#26828E', '#1F9E89', '#35B779', '#6DCD59',
           '#B4DE2C', '#FDE725']
```
- **Use for**: Scientific data, heat maps
- **Advantage**: Colorblind-safe, perceptually uniform
- **Example**: Elevation, correlation strength

#### **Plasma (High Contrast)**
```python
plasma = ['#0D0887', '#46039F', '#7201A8', '#9C179E',
          '#BD3786', '#D8576B', '#ED7953', '#FB9F3A',
          '#FDCA26', '#F0F921']
```
- **Use for**: Highlighting extremes, energy data
- **Example**: Earthquake magnitude, stock volatility

### 🔴🔵 Diverging Palettes (Data with Meaningful Center)

#### **RdBu (Red-Blue)**
```python
rdbu = ['#67001F', '#B2182B', '#D6604D', '#F4A582',
        '#FDDBC7', '#F7F7F7', '#D1E5F0', '#92C5DE',
        '#4393C3', '#2166AC', '#053061']
```
- **Use for**: Correlation, change from baseline, political data
- **Example**: Election swing, profit/loss, temperature anomaly

#### **PiYG (Pink-Green)**
```python
piyg = ['#8E0152', '#C51B7D', '#DE77AE', '#F1B6DA',
        '#FDE0EF', '#F7F7F7', '#E6F5D0', '#B8E186',
        '#7FBC41', '#4D9221', '#276419']
```
- **Use for**: Survey responses, agreement scales
- **Example**: Likert scales, before/after comparisons

### 🎯 Single-Color Highlights

#### **Accent Colors**
```python
accent_colors = {
    'red': '#E74C3C',      # Alerts, errors, important
    'blue': '#3498DB',     # Information, trust, corporate
    'green': '#2ECC71',    # Success, growth, positive
    'orange': '#F39C12',   # Warning, energy, creative
    'purple': '#9B59B6',   # Premium, creative, mystery
    'teal': '#1ABC9C',     # Modern, fresh, balance
}
```

#### **Grayscale Foundation**
```python
grays = {
    'lightest': '#F8F9FA',  # Backgrounds
    'light': '#E9ECEF',     # Borders, subtle elements
    'medium': '#6C757D',    # Secondary text
    'dark': '#343A40',      # Primary text
    'darkest': '#212529',   # Headers, emphasis
}
```

## 🎨 Color Combination Strategies

### **Monochromatic**
- Single hue with varying saturation/lightness
- **Use for**: Professional, elegant, focused
- **Example**: Blues from light to dark

### **Analogous**
- Adjacent colors on color wheel
- **Use for**: Harmonious, natural, calming
- **Example**: Blue → Blue-green → Green

### **Complementary**
- Opposite colors on color wheel
- **Use for**: High contrast, attention-grabbing
- **Example**: Blue and Orange

### **Triadic**
- Three evenly spaced colors on wheel
- **Use for**: Vibrant, balanced, dynamic
- **Example**: Red, Yellow, Blue

## 🔧 Implementation Code Examples

### **Matplotlib**
```python
import matplotlib.pyplot as plt

# Set color palette
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=okabe_ito)

# Or for specific plot
plt.plot(x, y, color='#E69F00')  # Okabe-Ito orange
```

### **Seaborn**
```python
import seaborn as sns

# Set palette globally
sns.set_palette("colorblind")  # Okabe-Ito equivalent
sns.set_palette(okabe_ito)     # Custom palette

# Or for specific plot
sns.scatterplot(data=df, x='x', y='y', hue='category', 
                palette='viridis')
```

### **Plotly**
```python
import plotly.express as px

# Use built-in colorblind-safe palette
fig = px.scatter(df, x='x', y='y', color='category',
                 color_discrete_sequence=px.colors.qualitative.Safe)

# Custom colors
fig = px.scatter(df, x='x', y='y', color='value',
                 color_continuous_scale='viridis')
```

## ♿ Accessibility Guidelines

### **Contrast Requirements**
- **Normal text**: 4.5:1 minimum contrast ratio
- **Large text**: 3:1 minimum contrast ratio
- **UI elements**: 3:1 minimum contrast ratio

### **Colorblind Considerations**
- **Test your palettes**: Use tools like Coblis or Color Oracle
- **Never rely solely on color**: Use patterns, labels, or shapes
- **Recommended safe palettes**: Okabe-Ito, Viridis, ColorBrewer

### **Cultural Considerations**
- **Red**: Danger (Western), luck (Chinese), purity (Indian)
- **Green**: Growth (Western), nature (universal), inexperience
- **Blue**: Trust (Western), mourning (Iran), masculinity
- **White**: Purity (Western), mourning (East Asian)

## 🔄 Palette Testing Tools

### **Online Tools**
- **Coolors.co**: Generate and test palettes
- **ColorBrewer**: Cartography-focused palettes
- **Contrast Checker**: WCAG compliance testing
- **Sim Daltonism**: Colorblind simulation

### **Python Libraries**
```python
# Test colorblind accessibility
import colorcet as cc
cc.palette_n['colorblind8']

# Generate palettes
import seaborn as sns
sns.color_palette("husl", 8)  # Perceptually uniform

# Test in different conditions
import colorspacious
# Convert to different color spaces for testing
```

## 📋 Quick Decision Matrix

| **Data Type** | **Recommended Palette** | **Avoid** |
|---------------|------------------------|-----------|
| Categories (≤8) | Okabe-Ito, Set1 | Rainbow |
| Categories (>8) | Grayscale + 1 accent | Distinct hues |
| Continuous positive | Blues, Viridis | Red-Green |
| Continuous ±0 | RdBu, PiYG | Single hue |
| Geographic | ColorBrewer, Viridis | Jet/Rainbow |
| Time series | Single hue variations | Many colors |

Remember: **When in doubt, use fewer colors and test for accessibility!**
