# AUTOGENERATED BY ECOSCOPE-WORKFLOWS; see fingerprint in README.md for details


# ruff: noqa: E402

# %% [markdown]
# # Events
# TODO: top level description

# %% [markdown]
# ## Imports

import os
from ecoscope_workflows_core.tasks.config import set_workflow_details
from ecoscope_workflows_core.tasks.skip import any_is_empty_df
from ecoscope_workflows_core.tasks.skip import any_dependency_skipped
from ecoscope_workflows_core.tasks.io import set_er_connection
from ecoscope_workflows_core.tasks.filter import set_time_range
from ecoscope_workflows_ext_ecoscope.tasks.io import get_events
from ecoscope_workflows_core.tasks.transformation import extract_value_from_json_column
from ecoscope_workflows_core.tasks.groupby import set_groupers
from ecoscope_workflows_ext_ecoscope.tasks.transformation import (
    apply_reloc_coord_filter,
)
from ecoscope_workflows_core.tasks.transformation import add_temporal_index
from ecoscope_workflows_ext_ecoscope.tasks.transformation import apply_color_map
from ecoscope_workflows_core.tasks.groupby import split_groups
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_time_series_bar_chart
from ecoscope_workflows_core.tasks.io import persist_text
from ecoscope_workflows_core.tasks.results import create_plot_widget_single_view
from ecoscope_workflows_core.tasks.skip import never
from ecoscope_workflows_core.tasks.results import merge_widget_views
from ecoscope_workflows_core.tasks.transformation import map_columns
from ecoscope_workflows_ext_ecoscope.tasks.results import set_base_maps
from ecoscope_workflows_ext_ecoscope.tasks.results import create_point_layer
from ecoscope_workflows_ext_ecoscope.tasks.skip import all_geometry_are_none
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_ecomap
from ecoscope_workflows_core.tasks.results import create_map_widget_single_view
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_pie_chart
from ecoscope_workflows_ext_ecoscope.tasks.analysis import create_meshgrid
from ecoscope_workflows_ext_ecoscope.tasks.analysis import calculate_feature_density
from ecoscope_workflows_core.tasks.transformation import sort_values
from ecoscope_workflows_core.tasks.transformation import map_values_with_unit
from ecoscope_workflows_ext_ecoscope.tasks.results import create_polygon_layer
from ecoscope_workflows_core.tasks.results import gather_dashboard

# %% [markdown]
# ## Workflow Details

# %%
# parameters

workflow_details_params = dict(
    name=...,
    description=...,
    image_url=...,
)

# %%
# call the task


workflow_details = (
    set_workflow_details.handle_errors(task_instance_id="workflow_details")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(**workflow_details_params)
    .call()
)


# %% [markdown]
# ## Data Source

# %%
# parameters

er_client_name_params = dict(
    data_source=...,
)

# %%
# call the task


er_client_name = (
    set_er_connection.handle_errors(task_instance_id="er_client_name")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(**er_client_name_params)
    .call()
)


# %% [markdown]
# ## Time Range

# %%
# parameters

time_range_params = dict(
    since=...,
    until=...,
)

# %%
# call the task


time_range = (
    set_time_range.handle_errors(task_instance_id="time_range")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(time_format="%d %b %Y %H:%M:%S %Z", **time_range_params)
    .call()
)


# %% [markdown]
# ## Event Types

# %%
# parameters

get_events_data_params = dict(
    event_types=...,
    drop_null_geometry=...,
)

# %%
# call the task


get_events_data = (
    get_events.handle_errors(task_instance_id="get_events_data")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        client=er_client_name,
        time_range=time_range,
        event_columns=[
            "id",
            "time",
            "event_type",
            "event_category",
            "reported_by",
            "serial_number",
            "geometry",
        ],
        raise_on_empty=False,
        **get_events_data_params,
    )
    .call()
)


# %% [markdown]
# ## Extract reported_by_name from Events

# %%
# parameters

extract_reported_by_params = dict()

# %%
# call the task


extract_reported_by = (
    extract_value_from_json_column.handle_errors(task_instance_id="extract_reported_by")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        df=get_events_data,
        column_name="reported_by",
        field_name_options=["name"],
        output_type="str",
        output_column_name="reported_by_name",
        **extract_reported_by_params,
    )
    .call()
)


# %% [markdown]
# ## Group Data

# %%
# parameters

groupers_params = dict(
    groupers=...,
)

# %%
# call the task


groupers = (
    set_groupers.handle_errors(task_instance_id="groupers")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(**groupers_params)
    .call()
)


# %% [markdown]
# ## Event Location Filter

# %%
# parameters

filter_events_params = dict(
    bounding_box=...,
    filter_point_coords=...,
)

# %%
# call the task


filter_events = (
    apply_reloc_coord_filter.handle_errors(task_instance_id="filter_events")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        df=extract_reported_by, roi_gdf=None, roi_name=None, **filter_events_params
    )
    .call()
)


# %% [markdown]
# ## Add temporal index to Events

# %%
# parameters

events_add_temporal_index_params = dict()

# %%
# call the task


events_add_temporal_index = (
    add_temporal_index.handle_errors(task_instance_id="events_add_temporal_index")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        df=filter_events,
        time_col="time",
        groupers=groupers,
        cast_to_datetime=True,
        format="mixed",
        **events_add_temporal_index_params,
    )
    .call()
)


# %% [markdown]
# ## Events Colormap

# %%
# parameters

events_colormap_params = dict()

# %%
# call the task


events_colormap = (
    apply_color_map.handle_errors(task_instance_id="events_colormap")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        df=events_add_temporal_index,
        input_column_name="event_type",
        colormap="tab20b",
        output_column_name="event_type_colormap",
        **events_colormap_params,
    )
    .call()
)


# %% [markdown]
# ## Split Events by Group

# %%
# parameters

split_event_groups_params = dict()

# %%
# call the task


split_event_groups = (
    split_groups.handle_errors(task_instance_id="split_event_groups")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(df=events_colormap, groupers=groupers, **split_event_groups_params)
    .call()
)


# %% [markdown]
# ## Draw Time Series Bar Chart for Events

# %%
# parameters

events_bar_chart_params = dict(
    time_interval=...,
)

# %%
# call the task


events_bar_chart = (
    draw_time_series_bar_chart.handle_errors(task_instance_id="events_bar_chart")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        x_axis="time",
        y_axis="event_type",
        category="event_type",
        agg_function="count",
        color_column="event_type_colormap",
        plot_style={"xperiodalignment": "middle"},
        layout_style=None,
        **events_bar_chart_params,
    )
    .mapvalues(argnames=["dataframe"], argvalues=split_event_groups)
)


# %% [markdown]
# ## Persist Bar Chart as Text

# %%
# parameters

events_bar_chart_html_url_params = dict(
    filename=...,
)

# %%
# call the task


events_bar_chart_html_url = (
    persist_text.handle_errors(task_instance_id="events_bar_chart_html_url")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
        **events_bar_chart_html_url_params,
    )
    .mapvalues(argnames=["text"], argvalues=events_bar_chart)
)


# %% [markdown]
# ## Create Bar Plot Widget for Events

# %%
# parameters

events_bar_chart_widget_params = dict()

# %%
# call the task


events_bar_chart_widget = (
    create_plot_widget_single_view.handle_errors(
        task_instance_id="events_bar_chart_widget"
    )
    .skipif(
        conditions=[
            never,
        ],
        unpack_depth=1,
    )
    .partial(title="Events Bar Chart", **events_bar_chart_widget_params)
    .map(argnames=["view", "data"], argvalues=events_bar_chart_html_url)
)


# %% [markdown]
# ## Merge Bar Plot Widget Views

# %%
# parameters

grouped_bar_plot_widget_merge_params = dict()

# %%
# call the task


grouped_bar_plot_widget_merge = (
    merge_widget_views.handle_errors(task_instance_id="grouped_bar_plot_widget_merge")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(widgets=events_bar_chart_widget, **grouped_bar_plot_widget_merge_params)
    .call()
)


# %% [markdown]
# ## Rename columns for map tooltip display

# %%
# parameters

rename_display_columns_params = dict()

# %%
# call the task


rename_display_columns = (
    map_columns.handle_errors(task_instance_id="rename_display_columns")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        drop_columns=[],
        retain_columns=[],
        rename_columns={
            "serial_number": "Event Serial",
            "time": "Event Time",
            "event_type": "Event Type",
            "reported_by_name": "Reported By",
        },
        **rename_display_columns_params,
    )
    .mapvalues(argnames=["df"], argvalues=split_event_groups)
)


# %% [markdown]
# ## Base Maps

# %%
# parameters

base_map_defs_params = dict(
    base_maps=...,
)

# %%
# call the task


base_map_defs = (
    set_base_maps.handle_errors(task_instance_id="base_map_defs")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(**base_map_defs_params)
    .call()
)


# %% [markdown]
# ## Create map layer from grouped Events

# %%
# parameters

grouped_events_map_layer_params = dict(
    zoom=...,
)

# %%
# call the task


grouped_events_map_layer = (
    create_point_layer.handle_errors(task_instance_id="grouped_events_map_layer")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
            all_geometry_are_none,
        ],
        unpack_depth=1,
    )
    .partial(
        layer_style={"fill_color_column": "event_type_colormap", "get_radius": 5},
        legend={"label_column": "Event Type", "color_column": "event_type_colormap"},
        tooltip_columns=["Event Serial", "Event Time", "Event Type", "Reported By"],
        **grouped_events_map_layer_params,
    )
    .mapvalues(argnames=["geodataframe"], argvalues=rename_display_columns)
)


# %% [markdown]
# ## Draw Ecomap from grouped Events

# %%
# parameters

grouped_events_ecomap_params = dict(
    view_state=...,
)

# %%
# call the task


grouped_events_ecomap = (
    draw_ecomap.handle_errors(task_instance_id="grouped_events_ecomap")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        title=None,
        tile_layers=base_map_defs,
        north_arrow_style={"placement": "top-left"},
        legend_style={"placement": "bottom-right"},
        static=False,
        max_zoom=20,
        **grouped_events_ecomap_params,
    )
    .mapvalues(argnames=["geo_layers"], argvalues=grouped_events_map_layer)
)


# %% [markdown]
# ## Persist grouped Events Ecomap as Text

# %%
# parameters

grouped_events_ecomap_html_url_params = dict(
    filename=...,
)

# %%
# call the task


grouped_events_ecomap_html_url = (
    persist_text.handle_errors(task_instance_id="grouped_events_ecomap_html_url")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
        **grouped_events_ecomap_html_url_params,
    )
    .mapvalues(argnames=["text"], argvalues=grouped_events_ecomap)
)


# %% [markdown]
# ## Create grouped Events Map Widget

# %%
# parameters

grouped_events_map_widget_params = dict()

# %%
# call the task


grouped_events_map_widget = (
    create_map_widget_single_view.handle_errors(
        task_instance_id="grouped_events_map_widget"
    )
    .skipif(
        conditions=[
            never,
        ],
        unpack_depth=1,
    )
    .partial(title="Events Map", **grouped_events_map_widget_params)
    .map(argnames=["view", "data"], argvalues=grouped_events_ecomap_html_url)
)


# %% [markdown]
# ## Merge Events Map Widget Views

# %%
# parameters

grouped_events_map_widget_merge_params = dict()

# %%
# call the task


grouped_events_map_widget_merge = (
    merge_widget_views.handle_errors(task_instance_id="grouped_events_map_widget_merge")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        widgets=grouped_events_map_widget, **grouped_events_map_widget_merge_params
    )
    .call()
)


# %% [markdown]
# ## Draw Pie Chart for Events

# %%
# parameters

grouped_events_pie_chart_params = dict()

# %%
# call the task


grouped_events_pie_chart = (
    draw_pie_chart.handle_errors(task_instance_id="grouped_events_pie_chart")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        value_column="event_type",
        color_column="event_type_colormap",
        plot_style={"textinfo": "value"},
        label_column=None,
        layout_style=None,
        **grouped_events_pie_chart_params,
    )
    .mapvalues(argnames=["dataframe"], argvalues=split_event_groups)
)


# %% [markdown]
# ## Persist Pie Chart as Text

# %%
# parameters

grouped_pie_chart_html_urls_params = dict(
    filename=...,
)

# %%
# call the task


grouped_pie_chart_html_urls = (
    persist_text.handle_errors(task_instance_id="grouped_pie_chart_html_urls")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
        **grouped_pie_chart_html_urls_params,
    )
    .mapvalues(argnames=["text"], argvalues=grouped_events_pie_chart)
)


# %% [markdown]
# ## Create Plot Widget for Events

# %%
# parameters

grouped_events_pie_chart_widgets_params = dict()

# %%
# call the task


grouped_events_pie_chart_widgets = (
    create_plot_widget_single_view.handle_errors(
        task_instance_id="grouped_events_pie_chart_widgets"
    )
    .skipif(
        conditions=[
            never,
        ],
        unpack_depth=1,
    )
    .partial(title="Events Pie Chart", **grouped_events_pie_chart_widgets_params)
    .map(argnames=["view", "data"], argvalues=grouped_pie_chart_html_urls)
)


# %% [markdown]
# ## Merge Pie Chart Widget Views

# %%
# parameters

grouped_events_pie_widget_merge_params = dict()

# %%
# call the task


grouped_events_pie_widget_merge = (
    merge_widget_views.handle_errors(task_instance_id="grouped_events_pie_widget_merge")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        widgets=grouped_events_pie_chart_widgets,
        **grouped_events_pie_widget_merge_params,
    )
    .call()
)


# %% [markdown]
# ##

# %%
# parameters

events_meshgrid_params = dict(
    auto_scale_or_custom_cell_size=...,
)

# %%
# call the task


events_meshgrid = (
    create_meshgrid.handle_errors(task_instance_id="events_meshgrid")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
            all_geometry_are_none,
        ],
        unpack_depth=1,
    )
    .partial(
        aoi=events_add_temporal_index, intersecting_only=False, **events_meshgrid_params
    )
    .call()
)


# %% [markdown]
# ## Grouped Events Feature Density

# %%
# parameters

grouped_events_feature_density_params = dict()

# %%
# call the task


grouped_events_feature_density = (
    calculate_feature_density.handle_errors(
        task_instance_id="grouped_events_feature_density"
    )
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        meshgrid=events_meshgrid,
        geometry_type="point",
        **grouped_events_feature_density_params,
    )
    .mapvalues(argnames=["geodataframe"], argvalues=split_event_groups)
)


# %% [markdown]
# ## Grouped Feature Density Colormap

# %%
# parameters

grouped_fd_colormap_params = dict()

# %%
# call the task


grouped_fd_colormap = (
    apply_color_map.handle_errors(task_instance_id="grouped_fd_colormap")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        input_column_name="density",
        colormap="RdYlGn_r",
        output_column_name="density_colormap",
        **grouped_fd_colormap_params,
    )
    .mapvalues(argnames=["df"], argvalues=grouped_events_feature_density)
)


# %% [markdown]
# ## Sort Density By Classification

# %%
# parameters

sort_grouped_density_values_params = dict()

# %%
# call the task


sort_grouped_density_values = (
    sort_values.handle_errors(task_instance_id="sort_grouped_density_values")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        column_name="density",
        ascending=True,
        na_position="last",
        **sort_grouped_density_values_params,
    )
    .mapvalues(argnames=["df"], argvalues=grouped_fd_colormap)
)


# %% [markdown]
# ## Format Grouped Feature Density Labels

# %%
# parameters

grouped_feature_density_format_params = dict()

# %%
# call the task


grouped_feature_density_format = (
    map_values_with_unit.handle_errors(
        task_instance_id="grouped_feature_density_format"
    )
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        original_unit=None,
        new_unit=None,
        input_column_name="density",
        output_column_name="density",
        decimal_places=0,
        **grouped_feature_density_format_params,
    )
    .mapvalues(argnames=["df"], argvalues=sort_grouped_density_values)
)


# %% [markdown]
# ## Create map layer from Feature Density

# %%
# parameters

grouped_fd_map_layer_params = dict(
    zoom=...,
)

# %%
# call the task


grouped_fd_map_layer = (
    create_polygon_layer.handle_errors(task_instance_id="grouped_fd_map_layer")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
            all_geometry_are_none,
        ],
        unpack_depth=1,
    )
    .partial(
        layer_style={
            "fill_color_column": "density_colormap",
            "get_line_width": 0,
            "opacity": 0.4,
        },
        legend={"label_column": "density", "color_column": "density_colormap"},
        tooltip_columns=["density"],
        **grouped_fd_map_layer_params,
    )
    .mapvalues(argnames=["geodataframe"], argvalues=grouped_feature_density_format)
)


# %% [markdown]
# ## Draw Ecomap from Feature Density

# %%
# parameters

grouped_fd_ecomap_params = dict(
    view_state=...,
)

# %%
# call the task


grouped_fd_ecomap = (
    draw_ecomap.handle_errors(task_instance_id="grouped_fd_ecomap")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        title=None,
        tile_layers=base_map_defs,
        north_arrow_style={"placement": "top-left"},
        legend_style={"title": "Number of events", "placement": "bottom-right"},
        static=False,
        max_zoom=20,
        **grouped_fd_ecomap_params,
    )
    .mapvalues(argnames=["geo_layers"], argvalues=grouped_fd_map_layer)
)


# %% [markdown]
# ## Persist Feature Density Ecomap as Text

# %%
# parameters

grouped_fd_ecomap_html_url_params = dict(
    filename=...,
)

# %%
# call the task


grouped_fd_ecomap_html_url = (
    persist_text.handle_errors(task_instance_id="grouped_fd_ecomap_html_url")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
        **grouped_fd_ecomap_html_url_params,
    )
    .mapvalues(argnames=["text"], argvalues=grouped_fd_ecomap)
)


# %% [markdown]
# ## Create Feature Density Map Widget

# %%
# parameters

grouped_fd_map_widget_params = dict()

# %%
# call the task


grouped_fd_map_widget = (
    create_map_widget_single_view.handle_errors(
        task_instance_id="grouped_fd_map_widget"
    )
    .skipif(
        conditions=[
            never,
        ],
        unpack_depth=1,
    )
    .partial(title="Density Map", **grouped_fd_map_widget_params)
    .map(argnames=["view", "data"], argvalues=grouped_fd_ecomap_html_url)
)


# %% [markdown]
# ## Merge Feature Density Widget Views

# %%
# parameters

grouped_fd_map_widget_merge_params = dict()

# %%
# call the task


grouped_fd_map_widget_merge = (
    merge_widget_views.handle_errors(task_instance_id="grouped_fd_map_widget_merge")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(widgets=grouped_fd_map_widget, **grouped_fd_map_widget_merge_params)
    .call()
)


# %% [markdown]
# ## Create Dashboard with Map Widgets

# %%
# parameters

events_dashboard_params = dict()

# %%
# call the task


events_dashboard = (
    gather_dashboard.handle_errors(task_instance_id="events_dashboard")
    .skipif(
        conditions=[
            any_is_empty_df,
            any_dependency_skipped,
        ],
        unpack_depth=1,
    )
    .partial(
        details=workflow_details,
        widgets=[
            grouped_bar_plot_widget_merge,
            grouped_events_map_widget_merge,
            grouped_events_pie_widget_merge,
            grouped_fd_map_widget_merge,
        ],
        groupers=groupers,
        time_range=time_range,
        **events_dashboard_params,
    )
    .call()
)
