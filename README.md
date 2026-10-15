# MLHub Notebooks

A curated collection of Jupyter notebooks and Python scripts demonstrating how to use TrendMiner’s MLHub for time-series analytics, contextual data enrichment, and visualization. Each folder groups examples by theme and lists individual notebooks/scripts with concrete, task-oriented use cases.

GitHub itself does not support interactive outputs. For many of the examples here, you can go to `nbviewer.org`, and paste the GitHub url to get access to the interactive result (i.e., the output graphs) of a Notebook.

---

## 📂 Calculations examples

Notebooks illustrating common time-series calculations and KPI reporting on TrendHub data:

- **time_based_report_calculations.ipynb**  
  Compute time-based KPIs (e.g. uptime, cycle time, batch yields) over fixed intervals. Shows how to:  
  - Slice a continuous signal into hourly/daily chunks  
  - Calculate aggregates (mean, min/max, counts) per period  
  - Combine the data in a Pandas DataFrame for further processing

- **value_based_search_and_calculation_example.ipynb**  
  Locate segments of interest by value thresholds (e.g. all periods where temperature > setpoint) and calculate statistics only on those segments. Covers:  
  - Value-based search for runs or events  
  - Rolling and conditional calculations  
  - Combining search results with downstream analytics  

---

## 📂 Contexthub examples

Notebooks for loading and enriching process data with ContextHub metadata and attachments:

- **get_context_item_attachment.ipynb**  
  Download and display attachments (PDFs, images, CSV logs) linked to ContextHub items. Demonstrates:   
  - Retrieving item attachments by ID  
  - Saving and previewing file content in MLHub  

- **loading_additional_context_item_fields.ipynb**  
  Fetch custom fields and tags associated with ContextHub items for richer filtering and analysis. Includes:  
  - Querying standard vs. custom metadata fields  
  - Merging context-item attributes into your DataFrame  
  - Filtering by business-specific context labels  

---

## 📂 Fetching data examples

Programmatic retrieval of TrendHub view data and metadata with interpolation:

- **get_interpolated_data.ipynb**  
  Load uniformly-spaced time-series data (e.g. 1-minute intervals) from an existing TrendHub view. Covers:  
  - Specifying start/end timestamps  
  - Choosing interpolation frequency and method  
  - Handling large date ranges via paging/batching  

---

## 📂 Plotting examples

Examples of static and interactive visualizations for TrendMiner time-series data:

- **cached_plot_example.ipynb**  
  Leverage MLHub’s plot-caching mechanism to speed up repeated rendering of large datasets. Illustrates:  
  - Caching settings and invalidation  
  - Overlaying multiple tags with different time spans  

- **plotting_example.ipynb**  
  General purpose plotting demo with:  
  - Matplotlib: static trend overlays, rolling-stats ribbons  
  - Plotly: interactive zoom, hover annotations, and export  

- **tag_histogram_examples.ipynb**
  Demo for plotting histograms of tag time series data, including:
  - Interactive selection of a specific tag (from predetermined list)
  - Interactive selection of a given time interval (from predetermined list)
  
- **plotting_aggregated_values_from_context_items.ipynb**
  Demo of plotting aggregated values from context items in a Plotly plot.

- **binned_correlations.ipynb**
  Demo of binning time series datapoints based on the values of one tag, and then creating a bar chart showing the aggregated (e.g. median) value of a second tag within that bin, as well as a box plot which gives a full overview of the statistical distribution within each bin.

---
