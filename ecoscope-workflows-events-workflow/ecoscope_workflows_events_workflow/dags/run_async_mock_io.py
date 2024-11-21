# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "ab0fe8d27af828622e9e2ee7237e1c87056198e47aca9d007cbf1753deb17bc2"

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
from ecoscope_workflows_core.tasks.io import set_connection
from ecoscope_workflows_core.tasks.groupby import set_groupers
from ecoscope_workflows_core.tasks.filter import set_time_range

get_events = create_task_magicmock(  # 🧪
    anchor="ecoscope_workflows_ext_ecoscope.tasks.io",  # 🧪
    func_name="get_events",  # 🧪
)  # 🧪
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

from ..params import Params


def main(params: Params):
    warnings.warn("This test script should not be used in production!")  # 🧪

    params_dict = json.loads(params.model_dump_json(exclude_unset=True))

    dependencies = {
        "workflow_details": [],
        "er_client_name": [],
        "groupers": [],
        "time_range": [],
        "get_events_data": ["er_client_name", "time_range"],
        "filter_events": ["get_events_data"],
        "events_add_temporal_index": ["filter_events", "groupers"],
        "events_colormap": ["events_add_temporal_index"],
        "events_map_layer": ["events_colormap"],
        "events_ecomap": ["events_map_layer"],
        "events_ecomap_html_url": ["events_ecomap"],
        "events_map_widget": ["events_ecomap_html_url"],
        "events_bar_chart": ["events_colormap"],
        "events_bar_chart_html_url": ["events_bar_chart"],
        "events_bar_chart_widget": ["events_bar_chart_html_url"],
        "events_meshgrid": ["events_add_temporal_index"],
        "events_feature_density": ["events_add_temporal_index", "events_meshgrid"],
        "fd_colormap": ["events_feature_density"],
        "fd_map_layer": ["fd_colormap"],
        "fd_ecomap": ["fd_map_layer"],
        "fd_ecomap_html_url": ["fd_ecomap"],
        "fd_map_widget": ["fd_ecomap_html_url"],
        "split_event_groups": ["events_colormap", "groupers"],
        "grouped_events_map_layer": ["split_event_groups"],
        "grouped_events_ecomap": ["grouped_events_map_layer"],
        "grouped_events_ecomap_html_url": ["grouped_events_ecomap"],
        "grouped_events_map_widget": ["grouped_events_ecomap_html_url"],
        "grouped_events_map_widget_merge": ["grouped_events_map_widget"],
        "grouped_events_pie_chart": ["split_event_groups"],
        "grouped_pie_chart_html_urls": ["grouped_events_pie_chart"],
        "grouped_events_pie_chart_widgets": ["grouped_pie_chart_html_urls"],
        "grouped_events_pie_widget_merge": ["grouped_events_pie_chart_widgets"],
        "grouped_events_feature_density": ["events_meshgrid", "split_event_groups"],
        "grouped_fd_colormap": ["grouped_events_feature_density"],
        "grouped_fd_map_layer": ["grouped_fd_colormap"],
        "grouped_fd_ecomap": ["grouped_fd_map_layer"],
        "grouped_fd_ecomap_html_url": ["grouped_fd_ecomap"],
        "grouped_fd_map_widget": ["grouped_fd_ecomap_html_url"],
        "grouped_fd_map_widget_merge": ["grouped_fd_map_widget"],
        "events_dashboard": [
            "workflow_details",
            "events_map_widget",
            "events_bar_chart_widget",
            "fd_map_widget",
            "grouped_events_map_widget_merge",
            "grouped_events_pie_widget_merge",
            "grouped_fd_map_widget_merge",
            "groupers",
            "time_range",
        ],
    }

    nodes = {
        "workflow_details": Node(
            async_task=set_workflow_details.validate().set_executor("lithops"),
            partial=(params_dict.get("workflow_details") or {}),
            method="call",
        ),
        "er_client_name": Node(
            async_task=set_connection.validate().set_executor("lithops"),
            partial=(params_dict.get("er_client_name") or {}),
            method="call",
        ),
        "groupers": Node(
            async_task=set_groupers.validate().set_executor("lithops"),
            partial=(params_dict.get("groupers") or {}),
            method="call",
        ),
        "time_range": Node(
            async_task=set_time_range.validate().set_executor("lithops"),
            partial=(params_dict.get("time_range") or {}),
            method="call",
        ),
        "get_events_data": Node(
            async_task=get_events.validate().set_executor("lithops"),
            partial={
                "client": DependsOn("er_client_name"),
                "time_range": DependsOn("time_range"),
                "event_columns": ["id", "time", "event_type", "geometry"],
            }
            | (params_dict.get("get_events_data") or {}),
            method="call",
        ),
        "filter_events": Node(
            async_task=apply_reloc_coord_filter.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("get_events_data"),
            }
            | (params_dict.get("filter_events") or {}),
            method="call",
        ),
        "events_add_temporal_index": Node(
            async_task=add_temporal_index.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("filter_events"),
                "time_col": "time",
                "groupers": DependsOn("groupers"),
            }
            | (params_dict.get("events_add_temporal_index") or {}),
            method="call",
        ),
        "events_colormap": Node(
            async_task=apply_color_map.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("events_add_temporal_index"),
                "input_column_name": "event_type",
                "colormap": "tab20b",
                "output_column_name": "event_type_colormap",
            }
            | (params_dict.get("events_colormap") or {}),
            method="call",
        ),
        "events_map_layer": Node(
            async_task=create_point_layer.validate().set_executor("lithops"),
            partial={
                "geodataframe": DependsOn("events_colormap"),
                "layer_style": {
                    "fill_color_column": "event_type_colormap",
                    "get_radius": 5,
                },
                "legend": {
                    "label_column": "event_type",
                    "color_column": "event_type_colormap",
                },
            }
            | (params_dict.get("events_map_layer") or {}),
            method="call",
        ),
        "events_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial={
                "geo_layers": DependsOn("events_map_layer"),
                "tile_layers": [
                    {"name": "TERRAIN"},
                    {"name": "SATELLITE", "opacity": 0.5},
                ],
                "north_arrow_style": {"placement": "top-left"},
                "legend_style": {"placement": "bottom-right"},
                "static": False,
            }
            | (params_dict.get("events_ecomap") or {}),
            method="call",
        ),
        "events_ecomap_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "text": DependsOn("events_ecomap"),
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("events_ecomap_html_url") or {}),
            method="call",
        ),
        "events_map_widget": Node(
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial={
                "data": DependsOn("events_ecomap_html_url"),
                "title": "Events Map",
            }
            | (params_dict.get("events_map_widget") or {}),
            method="call",
        ),
        "events_bar_chart": Node(
            async_task=draw_time_series_bar_chart.validate().set_executor("lithops"),
            partial={
                "dataframe": DependsOn("events_colormap"),
                "x_axis": "time",
                "y_axis": "event_type",
                "category": "event_type",
                "agg_function": "count",
                "color_column": "event_type_colormap",
                "plot_style": {"xperiodalignment": "middle"},
            }
            | (params_dict.get("events_bar_chart") or {}),
            method="call",
        ),
        "events_bar_chart_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "text": DependsOn("events_bar_chart"),
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("events_bar_chart_html_url") or {}),
            method="call",
        ),
        "events_bar_chart_widget": Node(
            async_task=create_plot_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial={
                "data": DependsOn("events_bar_chart_html_url"),
                "title": "Events Bar Chart",
            }
            | (params_dict.get("events_bar_chart_widget") or {}),
            method="call",
        ),
        "events_meshgrid": Node(
            async_task=create_meshgrid.validate().set_executor("lithops"),
            partial={
                "aoi": DependsOn("events_add_temporal_index"),
            }
            | (params_dict.get("events_meshgrid") or {}),
            method="call",
        ),
        "events_feature_density": Node(
            async_task=calculate_feature_density.validate().set_executor("lithops"),
            partial={
                "geodataframe": DependsOn("events_add_temporal_index"),
                "meshgrid": DependsOn("events_meshgrid"),
                "geometry_type": "point",
            }
            | (params_dict.get("events_feature_density") or {}),
            method="call",
        ),
        "fd_colormap": Node(
            async_task=apply_color_map.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("events_feature_density"),
                "input_column_name": "density",
                "colormap": "RdYlGn_r",
                "output_column_name": "density_colormap",
            }
            | (params_dict.get("fd_colormap") or {}),
            method="call",
        ),
        "fd_map_layer": Node(
            async_task=create_polygon_layer.validate().set_executor("lithops"),
            partial={
                "geodataframe": DependsOn("fd_colormap"),
                "layer_style": {
                    "fill_color_column": "density_colormap",
                    "get_line_width": 0,
                    "opacity": 0.4,
                },
            }
            | (params_dict.get("fd_map_layer") or {}),
            method="call",
        ),
        "fd_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial={
                "geo_layers": DependsOn("fd_map_layer"),
                "tile_layers": [
                    {"name": "TERRAIN"},
                    {"name": "SATELLITE", "opacity": 0.5},
                ],
                "north_arrow_style": {"placement": "top-left"},
                "legend_style": {"placement": "bottom-right"},
                "static": False,
            }
            | (params_dict.get("fd_ecomap") or {}),
            method="call",
        ),
        "fd_ecomap_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "text": DependsOn("fd_ecomap"),
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("fd_ecomap_html_url") or {}),
            method="call",
        ),
        "fd_map_widget": Node(
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial={
                "data": DependsOn("fd_ecomap_html_url"),
                "title": "Density Map",
            }
            | (params_dict.get("fd_map_widget") or {}),
            method="call",
        ),
        "split_event_groups": Node(
            async_task=split_groups.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("events_colormap"),
                "groupers": DependsOn("groupers"),
            }
            | (params_dict.get("split_event_groups") or {}),
            method="call",
        ),
        "grouped_events_map_layer": Node(
            async_task=create_point_layer.validate().set_executor("lithops"),
            partial={
                "layer_style": {
                    "fill_color_column": "event_type_colormap",
                    "get_radius": 5,
                },
                "legend": {
                    "label_column": "event_type",
                    "color_column": "event_type_colormap",
                },
            }
            | (params_dict.get("grouped_events_map_layer") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("split_event_groups"),
            },
        ),
        "grouped_events_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial={
                "tile_layers": [
                    {"name": "TERRAIN"},
                    {"name": "SATELLITE", "opacity": 0.5},
                ],
                "north_arrow_style": {"placement": "top-left"},
                "legend_style": {"placement": "bottom-right"},
                "static": False,
            }
            | (params_dict.get("grouped_events_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("grouped_events_map_layer"),
            },
        ),
        "grouped_events_ecomap_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
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
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial={
                "title": "Grouped Events Map",
            }
            | (params_dict.get("grouped_events_map_widget") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("grouped_events_ecomap_html_url"),
            },
        ),
        "grouped_events_map_widget_merge": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("grouped_events_map_widget"),
            }
            | (params_dict.get("grouped_events_map_widget_merge") or {}),
            method="call",
        ),
        "grouped_events_pie_chart": Node(
            async_task=draw_pie_chart.validate().set_executor("lithops"),
            partial={
                "value_column": "event_type",
                "color_column": "event_type_colormap",
                "plot_style": {"textinfo": "value"},
            }
            | (params_dict.get("grouped_events_pie_chart") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["dataframe"],
                "argvalues": DependsOn("split_event_groups"),
            },
        ),
        "grouped_pie_chart_html_urls": Node(
            async_task=persist_text.validate().set_executor("lithops"),
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
            async_task=create_plot_widget_single_view.validate().set_executor(
                "lithops"
            ),
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
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("grouped_events_pie_chart_widgets"),
            }
            | (params_dict.get("grouped_events_pie_widget_merge") or {}),
            method="call",
        ),
        "grouped_events_feature_density": Node(
            async_task=calculate_feature_density.validate().set_executor("lithops"),
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
            async_task=apply_color_map.validate().set_executor("lithops"),
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
        "grouped_fd_map_layer": Node(
            async_task=create_polygon_layer.validate().set_executor("lithops"),
            partial={
                "layer_style": {
                    "fill_color_column": "density_colormap",
                    "get_line_width": 0,
                    "opacity": 0.4,
                },
            }
            | (params_dict.get("grouped_fd_map_layer") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("grouped_fd_colormap"),
            },
        ),
        "grouped_fd_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial={
                "tile_layers": [
                    {"name": "TERRAIN"},
                    {"name": "SATELLITE", "opacity": 0.5},
                ],
                "north_arrow_style": {"placement": "top-left"},
                "legend_style": {"placement": "bottom-right"},
                "static": False,
            }
            | (params_dict.get("grouped_fd_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("grouped_fd_map_layer"),
            },
        ),
        "grouped_fd_ecomap_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
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
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial={
                "title": "Grouped Density Map",
            }
            | (params_dict.get("grouped_fd_map_widget") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("grouped_fd_ecomap_html_url"),
            },
        ),
        "grouped_fd_map_widget_merge": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("grouped_fd_map_widget"),
            }
            | (params_dict.get("grouped_fd_map_widget_merge") or {}),
            method="call",
        ),
        "events_dashboard": Node(
            async_task=gather_dashboard.validate().set_executor("lithops"),
            partial={
                "details": DependsOn("workflow_details"),
                "widgets": DependsOnSequence(
                    [
                        DependsOn("events_map_widget"),
                        DependsOn("events_bar_chart_widget"),
                        DependsOn("fd_map_widget"),
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
