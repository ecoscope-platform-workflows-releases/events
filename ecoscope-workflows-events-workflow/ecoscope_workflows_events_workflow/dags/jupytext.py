# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "096a6fa43734c88c56ead5ca4b242709db7cb7efe284dd34ee2ea141952fc0f4"


# ruff: noqa: E402

# %% [markdown]
# # Events
# TODO: top level description

# %% [markdown]
# ## Imports

import os
from ecoscope_workflows_core.tasks.config import set_workflow_details
from ecoscope_workflows_core.tasks.io import set_connection
from ecoscope_workflows_core.tasks.groupby import set_groupers
from ecoscope_workflows_core.tasks.filter import set_time_range
from ecoscope_workflows_ext_ecoscope.tasks.io import get_events
from ecoscope_workflows_ext_ecoscope.tasks.transformation import (
    apply_reloc_coord_filter,
)
from ecoscope_workflows_core.tasks.transformation import add_temporal_index
from ecoscope_workflows_ext_ecoscope.tasks.transformation import apply_color_map
from ecoscope_workflows_ext_ecoscope.tasks.results import create_point_layer
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_ecomap
from ecoscope_workflows_core.tasks.io import persist_text
from ecoscope_workflows_core.tasks.results import create_map_widget_single_view
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_time_series_bar_chart
from ecoscope_workflows_core.tasks.results import create_plot_widget_single_view
from ecoscope_workflows_ext_ecoscope.tasks.analysis import create_meshgrid
from ecoscope_workflows_ext_ecoscope.tasks.analysis import calculate_feature_density
from ecoscope_workflows_ext_ecoscope.tasks.results import create_polygon_layer
from ecoscope_workflows_core.tasks.groupby import split_groups
from ecoscope_workflows_core.tasks.results import merge_widget_views
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_pie_chart
from ecoscope_workflows_core.tasks.results import gather_dashboard

# %% [markdown]
# ## Set Workflow Details

# %%
# parameters

workflow_details_params = dict(
    name=...,
    description=...,
    image_url=...,
)

# %%
# call the task


workflow_details = set_workflow_details.partial(**workflow_details_params).call()


# %% [markdown]
# ## Select EarthRanger Connection

# %%
# parameters

er_client_name_params = dict(
    name=...,
)

# %%
# call the task


er_client_name = set_connection.partial(**er_client_name_params).call()


# %% [markdown]
# ## Set Groupers

# %%
# parameters

groupers_params = dict(
    groupers=...,
)

# %%
# call the task


groupers = set_groupers.partial(**groupers_params).call()


# %% [markdown]
# ## Set Time Range Filters

# %%
# parameters

time_range_params = dict(
    since=...,
    until=...,
    time_format=...,
)

# %%
# call the task


time_range = set_time_range.partial(**time_range_params).call()


# %% [markdown]
# ## Get Events from EarthRanger

# %%
# parameters

get_events_data_params = dict(
    event_types=...,
)

# %%
# call the task


get_events_data = get_events.partial(
    client=er_client_name,
    time_range=time_range,
    event_columns=["id", "time", "event_type", "geometry"],
    **get_events_data_params,
).call()


# %% [markdown]
# ## Apply Relocation Coordinate Filter

# %%
# parameters

filter_events_params = dict(
    min_x=...,
    max_x=...,
    min_y=...,
    max_y=...,
    filter_point_coords=...,
)

# %%
# call the task


filter_events = apply_reloc_coord_filter.partial(
    df=get_events_data, **filter_events_params
).call()


# %% [markdown]
# ## Add temporal index to Events

# %%
# parameters

events_add_temporal_index_params = dict(
    cast_to_datetime=...,
    format=...,
)

# %%
# call the task


events_add_temporal_index = add_temporal_index.partial(
    df=filter_events,
    time_col="time",
    groupers=groupers,
    **events_add_temporal_index_params,
).call()


# %% [markdown]
# ## Events Colormap

# %%
# parameters

events_colormap_params = dict()

# %%
# call the task


events_colormap = apply_color_map.partial(
    df=events_add_temporal_index,
    input_column_name="event_type",
    colormap="tab20b",
    output_column_name="event_type_colormap",
    **events_colormap_params,
).call()


# %% [markdown]
# ## Create map layer from Events

# %%
# parameters

events_map_layer_params = dict()

# %%
# call the task


events_map_layer = create_point_layer.partial(
    geodataframe=events_colormap,
    layer_style={"fill_color_column": "event_type_colormap", "get_radius": 5},
    legend={"label_column": "event_type", "color_column": "event_type_colormap"},
    **events_map_layer_params,
).call()


# %% [markdown]
# ## Draw Ecomap from Time Density

# %%
# parameters

events_ecomap_params = dict(
    title=...,
)

# %%
# call the task


events_ecomap = draw_ecomap.partial(
    geo_layers=events_map_layer,
    tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
    north_arrow_style={"placement": "top-left"},
    legend_style={"placement": "bottom-right"},
    static=False,
    **events_ecomap_params,
).call()


# %% [markdown]
# ## Persist Ecomap as Text

# %%
# parameters

events_ecomap_html_url_params = dict(
    filename=...,
)

# %%
# call the task


events_ecomap_html_url = persist_text.partial(
    text=events_ecomap,
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **events_ecomap_html_url_params,
).call()


# %% [markdown]
# ## Create Time Density Map Widget

# %%
# parameters

events_map_widget_params = dict(
    view=...,
)

# %%
# call the task


events_map_widget = create_map_widget_single_view.partial(
    data=events_ecomap_html_url, title="Events Map", **events_map_widget_params
).call()


# %% [markdown]
# ## Draw Time Series Bar Chart for Events

# %%
# parameters

events_bar_chart_params = dict(
    time_interval=...,
    grouped_styles=...,
    layout_style=...,
)

# %%
# call the task


events_bar_chart = draw_time_series_bar_chart.partial(
    dataframe=events_colormap,
    x_axis="time",
    y_axis="event_type",
    category="event_type",
    agg_function="count",
    color_column="event_type_colormap",
    plot_style={"xperiodalignment": "middle"},
    **events_bar_chart_params,
).call()


# %% [markdown]
# ## Persist Bar Chart as Text

# %%
# parameters

events_bar_chart_html_url_params = dict(
    filename=...,
)

# %%
# call the task


events_bar_chart_html_url = persist_text.partial(
    text=events_bar_chart,
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **events_bar_chart_html_url_params,
).call()


# %% [markdown]
# ## Create Plot Widget for Events

# %%
# parameters

events_bar_chart_widget_params = dict(
    view=...,
)

# %%
# call the task


events_bar_chart_widget = create_plot_widget_single_view.partial(
    data=events_bar_chart_html_url,
    title="Events Bar Chart",
    **events_bar_chart_widget_params,
).call()


# %% [markdown]
# ## Create Events Meshgrid

# %%
# parameters

events_meshgrid_params = dict(
    cell_width=...,
    cell_height=...,
    intersecting_only=...,
)

# %%
# call the task


events_meshgrid = create_meshgrid.partial(
    aoi=events_add_temporal_index, **events_meshgrid_params
).call()


# %% [markdown]
# ## Events Feature Density

# %%
# parameters

events_feature_density_params = dict()

# %%
# call the task


events_feature_density = calculate_feature_density.partial(
    geodataframe=events_add_temporal_index,
    meshgrid=events_meshgrid,
    geometry_type="point",
    **events_feature_density_params,
).call()


# %% [markdown]
# ## Feature Density Colormap

# %%
# parameters

fd_colormap_params = dict()

# %%
# call the task


fd_colormap = apply_color_map.partial(
    df=events_feature_density,
    input_column_name="density",
    colormap="RdYlGn_r",
    output_column_name="density_colormap",
    **fd_colormap_params,
).call()


# %% [markdown]
# ## Create map layer from Feature Density

# %%
# parameters

fd_map_layer_params = dict(
    legend=...,
)

# %%
# call the task


fd_map_layer = create_polygon_layer.partial(
    geodataframe=fd_colormap,
    layer_style={
        "fill_color_column": "density_colormap",
        "get_line_width": 0,
        "opacity": 0.4,
    },
    **fd_map_layer_params,
).call()


# %% [markdown]
# ## Draw Ecomap from Feature Density

# %%
# parameters

fd_ecomap_params = dict(
    title=...,
)

# %%
# call the task


fd_ecomap = draw_ecomap.partial(
    geo_layers=fd_map_layer,
    tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
    north_arrow_style={"placement": "top-left"},
    legend_style={"placement": "bottom-right"},
    static=False,
    **fd_ecomap_params,
).call()


# %% [markdown]
# ## Persist Feature Density Ecomap as Text

# %%
# parameters

fd_ecomap_html_url_params = dict(
    filename=...,
)

# %%
# call the task


fd_ecomap_html_url = persist_text.partial(
    text=fd_ecomap,
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **fd_ecomap_html_url_params,
).call()


# %% [markdown]
# ## Create Feature Density Map Widget

# %%
# parameters

fd_map_widget_params = dict(
    view=...,
)

# %%
# call the task


fd_map_widget = create_map_widget_single_view.partial(
    data=fd_ecomap_html_url, title="Density Map", **fd_map_widget_params
).call()


# %% [markdown]
# ## Split Events by Group

# %%
# parameters

split_event_groups_params = dict()

# %%
# call the task


split_event_groups = split_groups.partial(
    df=events_colormap, groupers=groupers, **split_event_groups_params
).call()


# %% [markdown]
# ## Create map layer from grouped Events

# %%
# parameters

grouped_events_map_layer_params = dict(
    legend=...,
)

# %%
# call the task


grouped_events_map_layer = create_point_layer.partial(
    layer_style={"fill_color_column": "event_type_colormap", "get_radius": 5},
    **grouped_events_map_layer_params,
).mapvalues(argnames=["geodataframe"], argvalues=split_event_groups)


# %% [markdown]
# ## Draw Ecomap from grouped Events

# %%
# parameters

grouped_events_ecomap_params = dict(
    title=...,
)

# %%
# call the task


grouped_events_ecomap = draw_ecomap.partial(
    tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
    north_arrow_style={"placement": "top-left"},
    legend_style={"placement": "bottom-right"},
    static=False,
    **grouped_events_ecomap_params,
).mapvalues(argnames=["geo_layers"], argvalues=grouped_events_map_layer)


# %% [markdown]
# ## Persist grouped Events Ecomap as Text

# %%
# parameters

grouped_events_ecomap_html_url_params = dict(
    filename=...,
)

# %%
# call the task


grouped_events_ecomap_html_url = persist_text.partial(
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **grouped_events_ecomap_html_url_params,
).mapvalues(argnames=["text"], argvalues=grouped_events_ecomap)


# %% [markdown]
# ## Create grouped Events Map Widget

# %%
# parameters

grouped_events_map_widget_params = dict()

# %%
# call the task


grouped_events_map_widget = create_map_widget_single_view.partial(
    title="Grouped Events Map", **grouped_events_map_widget_params
).map(argnames=["view", "data"], argvalues=grouped_events_ecomap_html_url)


# %% [markdown]
# ## Merge Events Map Widget Views

# %%
# parameters

grouped_events_map_widget_merge_params = dict()

# %%
# call the task


grouped_events_map_widget_merge = merge_widget_views.partial(
    widgets=grouped_events_map_widget, **grouped_events_map_widget_merge_params
).call()


# %% [markdown]
# ## Draw Pie Chart for Events

# %%
# parameters

grouped_events_pie_chart_params = dict(
    label_column=...,
    layout_style=...,
)

# %%
# call the task


grouped_events_pie_chart = draw_pie_chart.partial(
    value_column="event_type",
    color_column="event_type_colormap",
    plot_style={"textinfo": "value"},
    **grouped_events_pie_chart_params,
).mapvalues(argnames=["dataframe"], argvalues=split_event_groups)


# %% [markdown]
# ## Persist Pie Chart as Text

# %%
# parameters

grouped_pie_chart_html_urls_params = dict(
    filename=...,
)

# %%
# call the task


grouped_pie_chart_html_urls = persist_text.partial(
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **grouped_pie_chart_html_urls_params,
).mapvalues(argnames=["text"], argvalues=grouped_events_pie_chart)


# %% [markdown]
# ## Create Plot Widget for Events

# %%
# parameters

grouped_events_pie_chart_widgets_params = dict()

# %%
# call the task


grouped_events_pie_chart_widgets = create_plot_widget_single_view.partial(
    title="Events Pie Chart", **grouped_events_pie_chart_widgets_params
).map(argnames=["view", "data"], argvalues=grouped_pie_chart_html_urls)


# %% [markdown]
# ## Merge Pie Chart Widget Views

# %%
# parameters

grouped_events_pie_widget_merge_params = dict()

# %%
# call the task


grouped_events_pie_widget_merge = merge_widget_views.partial(
    widgets=grouped_events_pie_chart_widgets, **grouped_events_pie_widget_merge_params
).call()


# %% [markdown]
# ## Grouped Events Feature Density

# %%
# parameters

grouped_events_feature_density_params = dict()

# %%
# call the task


grouped_events_feature_density = calculate_feature_density.partial(
    meshgrid=events_meshgrid,
    geometry_type="point",
    **grouped_events_feature_density_params,
).mapvalues(argnames=["geodataframe"], argvalues=split_event_groups)


# %% [markdown]
# ## Grouped Feature Density Colormap

# %%
# parameters

grouped_fd_colormap_params = dict()

# %%
# call the task


grouped_fd_colormap = apply_color_map.partial(
    input_column_name="density",
    colormap="RdYlGn_r",
    output_column_name="density_colormap",
    **grouped_fd_colormap_params,
).mapvalues(argnames=["df"], argvalues=grouped_events_feature_density)


# %% [markdown]
# ## Create map layer from Feature Density

# %%
# parameters

grouped_fd_map_layer_params = dict(
    legend=...,
)

# %%
# call the task


grouped_fd_map_layer = create_polygon_layer.partial(
    layer_style={
        "fill_color_column": "density_colormap",
        "get_line_width": 0,
        "opacity": 0.4,
    },
    **grouped_fd_map_layer_params,
).mapvalues(argnames=["geodataframe"], argvalues=grouped_fd_colormap)


# %% [markdown]
# ## Draw Ecomap from Feature Density

# %%
# parameters

grouped_fd_ecomap_params = dict(
    title=...,
)

# %%
# call the task


grouped_fd_ecomap = draw_ecomap.partial(
    tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
    north_arrow_style={"placement": "top-left"},
    legend_style={"placement": "bottom-right"},
    static=False,
    **grouped_fd_ecomap_params,
).mapvalues(argnames=["geo_layers"], argvalues=grouped_fd_map_layer)


# %% [markdown]
# ## Persist Feature Density Ecomap as Text

# %%
# parameters

grouped_fd_ecomap_html_url_params = dict(
    filename=...,
)

# %%
# call the task


grouped_fd_ecomap_html_url = persist_text.partial(
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **grouped_fd_ecomap_html_url_params,
).mapvalues(argnames=["text"], argvalues=grouped_fd_ecomap)


# %% [markdown]
# ## Create Feature Density Map Widget

# %%
# parameters

grouped_fd_map_widget_params = dict()

# %%
# call the task


grouped_fd_map_widget = create_map_widget_single_view.partial(
    title="Grouped Density Map", **grouped_fd_map_widget_params
).map(argnames=["view", "data"], argvalues=grouped_fd_ecomap_html_url)


# %% [markdown]
# ## Merge Feature Density Widget Views

# %%
# parameters

grouped_fd_map_widget_merge_params = dict()

# %%
# call the task


grouped_fd_map_widget_merge = merge_widget_views.partial(
    widgets=grouped_fd_map_widget, **grouped_fd_map_widget_merge_params
).call()


# %% [markdown]
# ## Create Dashboard with Map Widgets

# %%
# parameters

events_dashboard_params = dict()

# %%
# call the task


events_dashboard = gather_dashboard.partial(
    details=workflow_details,
    widgets=[
        events_map_widget,
        events_bar_chart_widget,
        fd_map_widget,
        grouped_events_map_widget_merge,
        grouped_events_pie_widget_merge,
        grouped_fd_map_widget_merge,
    ],
    groupers=groupers,
    time_range=time_range,
    **events_dashboard_params,
).call()
