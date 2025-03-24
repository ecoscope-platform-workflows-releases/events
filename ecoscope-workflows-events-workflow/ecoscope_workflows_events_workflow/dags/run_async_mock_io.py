# AUTOGENERATED BY ECOSCOPE-WORKFLOWS; see fingerprint in README.md for details

# ruff: noqa: E402

"""WARNING: This file is generated in a testing context and should not be used in production.
Lines specific to the testing context are marked with a test tube emoji (🧪) to indicate
that they would not be included (or would be different) in the production version of this file.
"""

import json
import os
import warnings  # 🧪
from ecoscope_workflows_core.testing import create_task_magicmock  # 🧪


from ecoscope_workflows_core.graph import DependsOn, DependsOnSequence, Graph, Node

from ecoscope_workflows_core.tasks.config import set_workflow_details
from ecoscope_workflows_core.tasks.io import set_er_connection
from ecoscope_workflows_core.tasks.filter import set_time_range

get_events = create_task_magicmock(  # 🧪
    anchor="ecoscope_workflows_ext_ecoscope.tasks.io",  # 🧪
    func_name="get_events",  # 🧪
)  # 🧪
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
from ecoscope_workflows_core.tasks.results import merge_widget_views
from ecoscope_workflows_ext_ecoscope.tasks.results import create_point_layer
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_ecomap
from ecoscope_workflows_core.tasks.results import create_map_widget_single_view
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_pie_chart
from ecoscope_workflows_ext_ecoscope.tasks.analysis import create_meshgrid
from ecoscope_workflows_ext_ecoscope.tasks.analysis import calculate_feature_density
from ecoscope_workflows_core.tasks.transformation import sort_values
from ecoscope_workflows_core.tasks.transformation import map_values_with_unit
from ecoscope_workflows_ext_ecoscope.tasks.results import create_polygon_layer
from ecoscope_workflows_core.tasks.results import gather_dashboard

from ..params import Params


def main(params: Params):
    warnings.warn("This test script should not be used in production!")  # 🧪

    params_dict = json.loads(params.model_dump_json(exclude_unset=True))

    dependencies = {
        "workflow_details": [],
        "er_client_name": [],
        "time_range": [],
        "get_events_data": ["er_client_name", "time_range"],
        "extract_reported_by": ["get_events_data"],
        "groupers": [],
        "filter_events": ["extract_reported_by"],
        "events_add_temporal_index": ["filter_events", "groupers"],
        "events_colormap": ["events_add_temporal_index"],
        "split_event_groups": ["events_colormap", "groupers"],
        "events_bar_chart": ["split_event_groups"],
        "events_bar_chart_html_url": ["events_bar_chart"],
        "events_bar_chart_widget": ["events_bar_chart_html_url"],
        "grouped_bar_plot_widget_merge": ["events_bar_chart_widget"],
        "grouped_events_map_layer": ["split_event_groups"],
        "grouped_events_ecomap": ["grouped_events_map_layer"],
        "grouped_events_ecomap_html_url": ["grouped_events_ecomap"],
        "grouped_events_map_widget": ["grouped_events_ecomap_html_url"],
        "grouped_events_map_widget_merge": ["grouped_events_map_widget"],
        "grouped_events_pie_chart": ["split_event_groups"],
        "grouped_pie_chart_html_urls": ["grouped_events_pie_chart"],
        "grouped_events_pie_chart_widgets": ["grouped_pie_chart_html_urls"],
        "grouped_events_pie_widget_merge": ["grouped_events_pie_chart_widgets"],
        "events_meshgrid": ["events_add_temporal_index"],
        "grouped_events_feature_density": ["events_meshgrid", "split_event_groups"],
        "grouped_fd_colormap": ["grouped_events_feature_density"],
        "sort_grouped_density_values": ["grouped_fd_colormap"],
        "grouped_feature_density_format": ["sort_grouped_density_values"],
        "grouped_fd_map_layer": ["grouped_feature_density_format"],
        "grouped_fd_ecomap": ["grouped_fd_map_layer"],
        "grouped_fd_ecomap_html_url": ["grouped_fd_ecomap"],
        "grouped_fd_map_widget": ["grouped_fd_ecomap_html_url"],
        "grouped_fd_map_widget_merge": ["grouped_fd_map_widget"],
        "events_dashboard": [
            "workflow_details",
            "grouped_bar_plot_widget_merge",
            "grouped_events_map_widget_merge",
            "grouped_events_pie_widget_merge",
            "grouped_fd_map_widget_merge",
            "groupers",
            "time_range",
        ],
    }

    nodes = {
        "workflow_details": Node(
            async_task=set_workflow_details.validate()
            .handle_errors(task_instance_id="workflow_details")
            .set_executor("lithops"),
            partial=(params_dict.get("workflow_details") or {}),
            method="call",
        ),
        "er_client_name": Node(
            async_task=set_er_connection.validate()
            .handle_errors(task_instance_id="er_client_name")
            .set_executor("lithops"),
            partial=(params_dict.get("er_client_name") or {}),
            method="call",
        ),
        "time_range": Node(
            async_task=set_time_range.validate()
            .handle_errors(task_instance_id="time_range")
            .set_executor("lithops"),
            partial={
                "time_format": "%d %b %Y %H:%M:%S %Z",
            }
            | (params_dict.get("time_range") or {}),
            method="call",
        ),
        "get_events_data": Node(
            async_task=get_events.validate()
            .handle_errors(task_instance_id="get_events_data")
            .set_executor("lithops"),
            partial={
                "client": DependsOn("er_client_name"),
                "time_range": DependsOn("time_range"),
                "event_columns": [
                    "id",
                    "time",
                    "event_type",
                    "event_category",
                    "reported_by",
                    "geometry",
                ],
                "raise_on_empty": True,
            }
            | (params_dict.get("get_events_data") or {}),
            method="call",
        ),
        "extract_reported_by": Node(
            async_task=extract_value_from_json_column.validate()
            .handle_errors(task_instance_id="extract_reported_by")
            .set_executor("lithops"),
            partial={
                "df": DependsOn("get_events_data"),
                "column_name": "reported_by",
                "field_name_options": ["name"],
                "output_type": "str",
                "output_column_name": "reported_by_name",
            }
            | (params_dict.get("extract_reported_by") or {}),
            method="call",
        ),
        "groupers": Node(
            async_task=set_groupers.validate()
            .handle_errors(task_instance_id="groupers")
            .set_executor("lithops"),
            partial=(params_dict.get("groupers") or {}),
            method="call",
        ),
        "filter_events": Node(
            async_task=apply_reloc_coord_filter.validate()
            .handle_errors(task_instance_id="filter_events")
            .set_executor("lithops"),
            partial={
                "df": DependsOn("extract_reported_by"),
                "roi_gdf": None,
                "roi_name": None,
            }
            | (params_dict.get("filter_events") or {}),
            method="call",
        ),
        "events_add_temporal_index": Node(
            async_task=add_temporal_index.validate()
            .handle_errors(task_instance_id="events_add_temporal_index")
            .set_executor("lithops"),
            partial={
                "df": DependsOn("filter_events"),
                "time_col": "time",
                "groupers": DependsOn("groupers"),
                "cast_to_datetime": True,
                "format": "mixed",
            }
            | (params_dict.get("events_add_temporal_index") or {}),
            method="call",
        ),
        "events_colormap": Node(
            async_task=apply_color_map.validate()
            .handle_errors(task_instance_id="events_colormap")
            .set_executor("lithops"),
            partial={
                "df": DependsOn("events_add_temporal_index"),
                "input_column_name": "event_type",
                "colormap": "tab20b",
                "output_column_name": "event_type_colormap",
            }
            | (params_dict.get("events_colormap") or {}),
            method="call",
        ),
        "split_event_groups": Node(
            async_task=split_groups.validate()
            .handle_errors(task_instance_id="split_event_groups")
            .set_executor("lithops"),
            partial={
                "df": DependsOn("events_colormap"),
                "groupers": DependsOn("groupers"),
            }
            | (params_dict.get("split_event_groups") or {}),
            method="call",
        ),
        "events_bar_chart": Node(
            async_task=draw_time_series_bar_chart.validate()
            .handle_errors(task_instance_id="events_bar_chart")
            .set_executor("lithops"),
            partial={
                "x_axis": "time",
                "y_axis": "event_type",
                "category": "event_type",
                "agg_function": "count",
                "color_column": "event_type_colormap",
                "plot_style": {"xperiodalignment": "middle"},
                "grouped_styles": None,
                "layout_style": None,
            }
            | (params_dict.get("events_bar_chart") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["dataframe"],
                "argvalues": DependsOn("split_event_groups"),
            },
        ),
        "events_bar_chart_html_url": Node(
            async_task=persist_text.validate()
            .handle_errors(task_instance_id="events_bar_chart_html_url")
            .set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("events_bar_chart_html_url") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("events_bar_chart"),
            },
        ),
        "events_bar_chart_widget": Node(
            async_task=create_plot_widget_single_view.validate()
            .handle_errors(task_instance_id="events_bar_chart_widget")
            .set_executor("lithops"),
            partial={
                "title": "Events Bar Chart",
            }
            | (params_dict.get("events_bar_chart_widget") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("events_bar_chart_html_url"),
            },
        ),
        "grouped_bar_plot_widget_merge": Node(
            async_task=merge_widget_views.validate()
            .handle_errors(task_instance_id="grouped_bar_plot_widget_merge")
            .set_executor("lithops"),
            partial={
                "widgets": DependsOn("events_bar_chart_widget"),
            }
            | (params_dict.get("grouped_bar_plot_widget_merge") or {}),
            method="call",
        ),
        "grouped_events_map_layer": Node(
            async_task=create_point_layer.validate()
            .handle_errors(task_instance_id="grouped_events_map_layer")
            .set_executor("lithops"),
            partial={
                "layer_style": {
                    "fill_color_column": "event_type_colormap",
                    "get_radius": 5,
                },
                "legend": {
                    "label_column": "event_type",
                    "color_column": "event_type_colormap",
                },
                "tooltip_columns": ["id", "time", "event_type"],
            }
            | (params_dict.get("grouped_events_map_layer") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("split_event_groups"),
            },
        ),
        "grouped_events_ecomap": Node(
            async_task=draw_ecomap.validate()
            .handle_errors(task_instance_id="grouped_events_ecomap")
            .set_executor("lithops"),
            partial={
                "title": None,
                "tile_layers": [
                    {"name": "TERRAIN"},
                    {"name": "SATELLITE", "opacity": 0.5},
                ],
                "north_arrow_style": {"placement": "top-left"},
                "legend_style": {"placement": "bottom-right"},
                "static": False,
                "max_zoom": 20,
            }
            | (params_dict.get("grouped_events_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("grouped_events_map_layer"),
            },
        ),
        "grouped_events_ecomap_html_url": Node(
            async_task=persist_text.validate()
            .handle_errors(task_instance_id="grouped_events_ecomap_html_url")
            .set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("grouped_events_ecomap_html_url") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("grouped_events_ecomap"),
            },
        ),
        "grouped_events_map_widget": Node(
            async_task=create_map_widget_single_view.validate()
            .handle_errors(task_instance_id="grouped_events_map_widget")
            .set_executor("lithops"),
            partial={
                "title": "Events Map",
            }
            | (params_dict.get("grouped_events_map_widget") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("grouped_events_ecomap_html_url"),
            },
        ),
        "grouped_events_map_widget_merge": Node(
            async_task=merge_widget_views.validate()
            .handle_errors(task_instance_id="grouped_events_map_widget_merge")
            .set_executor("lithops"),
            partial={
                "widgets": DependsOn("grouped_events_map_widget"),
            }
            | (params_dict.get("grouped_events_map_widget_merge") or {}),
            method="call",
        ),
        "grouped_events_pie_chart": Node(
            async_task=draw_pie_chart.validate()
            .handle_errors(task_instance_id="grouped_events_pie_chart")
            .set_executor("lithops"),
            partial={
                "value_column": "event_type",
                "color_column": "event_type_colormap",
                "plot_style": {"textinfo": "value"},
                "label_column": None,
                "layout_style": None,
            }
            | (params_dict.get("grouped_events_pie_chart") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["dataframe"],
                "argvalues": DependsOn("split_event_groups"),
            },
        ),
        "grouped_pie_chart_html_urls": Node(
            async_task=persist_text.validate()
            .handle_errors(task_instance_id="grouped_pie_chart_html_urls")
            .set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("grouped_pie_chart_html_urls") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("grouped_events_pie_chart"),
            },
        ),
        "grouped_events_pie_chart_widgets": Node(
            async_task=create_plot_widget_single_view.validate()
            .handle_errors(task_instance_id="grouped_events_pie_chart_widgets")
            .set_executor("lithops"),
            partial={
                "title": "Events Pie Chart",
            }
            | (params_dict.get("grouped_events_pie_chart_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("grouped_pie_chart_html_urls"),
            },
        ),
        "grouped_events_pie_widget_merge": Node(
            async_task=merge_widget_views.validate()
            .handle_errors(task_instance_id="grouped_events_pie_widget_merge")
            .set_executor("lithops"),
            partial={
                "widgets": DependsOn("grouped_events_pie_chart_widgets"),
            }
            | (params_dict.get("grouped_events_pie_widget_merge") or {}),
            method="call",
        ),
        "events_meshgrid": Node(
            async_task=create_meshgrid.validate()
            .handle_errors(task_instance_id="events_meshgrid")
            .set_executor("lithops"),
            partial={
                "aoi": DependsOn("events_add_temporal_index"),
                "intersecting_only": False,
            }
            | (params_dict.get("events_meshgrid") or {}),
            method="call",
        ),
        "grouped_events_feature_density": Node(
            async_task=calculate_feature_density.validate()
            .handle_errors(task_instance_id="grouped_events_feature_density")
            .set_executor("lithops"),
            partial={
                "meshgrid": DependsOn("events_meshgrid"),
                "geometry_type": "point",
            }
            | (params_dict.get("grouped_events_feature_density") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("split_event_groups"),
            },
        ),
        "grouped_fd_colormap": Node(
            async_task=apply_color_map.validate()
            .handle_errors(task_instance_id="grouped_fd_colormap")
            .set_executor("lithops"),
            partial={
                "input_column_name": "density",
                "colormap": "RdYlGn_r",
                "output_column_name": "density_colormap",
            }
            | (params_dict.get("grouped_fd_colormap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("grouped_events_feature_density"),
            },
        ),
        "sort_grouped_density_values": Node(
            async_task=sort_values.validate()
            .handle_errors(task_instance_id="sort_grouped_density_values")
            .set_executor("lithops"),
            partial={
                "column_name": "density",
                "ascending": True,
                "na_position": "last",
            }
            | (params_dict.get("sort_grouped_density_values") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("grouped_fd_colormap"),
            },
        ),
        "grouped_feature_density_format": Node(
            async_task=map_values_with_unit.validate()
            .handle_errors(task_instance_id="grouped_feature_density_format")
            .set_executor("lithops"),
            partial={
                "original_unit": None,
                "new_unit": None,
                "input_column_name": "density",
                "output_column_name": "density",
                "decimal_places": 0,
            }
            | (params_dict.get("grouped_feature_density_format") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("sort_grouped_density_values"),
            },
        ),
        "grouped_fd_map_layer": Node(
            async_task=create_polygon_layer.validate()
            .handle_errors(task_instance_id="grouped_fd_map_layer")
            .set_executor("lithops"),
            partial={
                "layer_style": {
                    "fill_color_column": "density_colormap",
                    "get_line_width": 0,
                    "opacity": 0.4,
                },
                "legend": {
                    "label_column": "density",
                    "color_column": "density_colormap",
                },
                "tooltip_columns": ["density"],
            }
            | (params_dict.get("grouped_fd_map_layer") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("grouped_feature_density_format"),
            },
        ),
        "grouped_fd_ecomap": Node(
            async_task=draw_ecomap.validate()
            .handle_errors(task_instance_id="grouped_fd_ecomap")
            .set_executor("lithops"),
            partial={
                "title": None,
                "tile_layers": [
                    {"name": "TERRAIN"},
                    {"name": "SATELLITE", "opacity": 0.5},
                ],
                "north_arrow_style": {"placement": "top-left"},
                "legend_style": {
                    "title": "Number of events",
                    "placement": "bottom-right",
                },
                "static": False,
                "max_zoom": 20,
            }
            | (params_dict.get("grouped_fd_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("grouped_fd_map_layer"),
            },
        ),
        "grouped_fd_ecomap_html_url": Node(
            async_task=persist_text.validate()
            .handle_errors(task_instance_id="grouped_fd_ecomap_html_url")
            .set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("grouped_fd_ecomap_html_url") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("grouped_fd_ecomap"),
            },
        ),
        "grouped_fd_map_widget": Node(
            async_task=create_map_widget_single_view.validate()
            .handle_errors(task_instance_id="grouped_fd_map_widget")
            .set_executor("lithops"),
            partial={
                "title": "Density Map",
            }
            | (params_dict.get("grouped_fd_map_widget") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("grouped_fd_ecomap_html_url"),
            },
        ),
        "grouped_fd_map_widget_merge": Node(
            async_task=merge_widget_views.validate()
            .handle_errors(task_instance_id="grouped_fd_map_widget_merge")
            .set_executor("lithops"),
            partial={
                "widgets": DependsOn("grouped_fd_map_widget"),
            }
            | (params_dict.get("grouped_fd_map_widget_merge") or {}),
            method="call",
        ),
        "events_dashboard": Node(
            async_task=gather_dashboard.validate()
            .handle_errors(task_instance_id="events_dashboard")
            .set_executor("lithops"),
            partial={
                "details": DependsOn("workflow_details"),
                "widgets": DependsOnSequence(
                    [
                        DependsOn("grouped_bar_plot_widget_merge"),
                        DependsOn("grouped_events_map_widget_merge"),
                        DependsOn("grouped_events_pie_widget_merge"),
                        DependsOn("grouped_fd_map_widget_merge"),
                    ],
                ),
                "groupers": DependsOn("groupers"),
                "time_range": DependsOn("time_range"),
            }
            | (params_dict.get("events_dashboard") or {}),
            method="call",
        ),
    }
    graph = Graph(dependencies=dependencies, nodes=nodes)
    results = graph.execute()
    return results
