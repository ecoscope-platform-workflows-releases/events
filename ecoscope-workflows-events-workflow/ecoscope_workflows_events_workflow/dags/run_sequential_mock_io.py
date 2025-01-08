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


from ecoscope_workflows_core.tasks.config import set_workflow_details
from ecoscope_workflows_core.tasks.io import set_er_connection
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

    workflow_details = (
        set_workflow_details.validate()
        .partial(**(params_dict.get("workflow_details") or {}))
        .call()
    )

    er_client_name = (
        set_er_connection.validate()
        .partial(**(params_dict.get("er_client_name") or {}))
        .call()
    )

    groupers = (
        set_groupers.validate().partial(**(params_dict.get("groupers") or {})).call()
    )

    time_range = (
        set_time_range.validate()
        .partial(
            time_format="%d %b %Y %H:%M:%S %Z", **(params_dict.get("time_range") or {})
        )
        .call()
    )

    get_events_data = (
        get_events.validate()
        .partial(
            client=er_client_name,
            time_range=time_range,
            event_columns=["id", "time", "event_type", "geometry"],
            **(params_dict.get("get_events_data") or {}),
        )
        .call()
    )

    filter_events = (
        apply_reloc_coord_filter.validate()
        .partial(df=get_events_data, **(params_dict.get("filter_events") or {}))
        .call()
    )

    events_add_temporal_index = (
        add_temporal_index.validate()
        .partial(
            df=filter_events,
            time_col="time",
            groupers=groupers,
            cast_to_datetime=True,
            format="mixed",
            **(params_dict.get("events_add_temporal_index") or {}),
        )
        .call()
    )

    events_colormap = (
        apply_color_map.validate()
        .partial(
            df=events_add_temporal_index,
            input_column_name="event_type",
            colormap="tab20b",
            output_column_name="event_type_colormap",
            **(params_dict.get("events_colormap") or {}),
        )
        .call()
    )

    split_event_groups = (
        split_groups.validate()
        .partial(
            df=events_colormap,
            groupers=groupers,
            **(params_dict.get("split_event_groups") or {}),
        )
        .call()
    )

    events_bar_chart = (
        draw_time_series_bar_chart.validate()
        .partial(
            x_axis="time",
            y_axis="event_type",
            category="event_type",
            agg_function="count",
            color_column="event_type_colormap",
            plot_style={"xperiodalignment": "middle"},
            grouped_styles=None,
            layout_style=None,
            **(params_dict.get("events_bar_chart") or {}),
        )
        .mapvalues(argnames=["dataframe"], argvalues=split_event_groups)
    )

    events_bar_chart_html_url = (
        persist_text.validate()
        .partial(
            root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            **(params_dict.get("events_bar_chart_html_url") or {}),
        )
        .mapvalues(argnames=["text"], argvalues=events_bar_chart)
    )

    events_bar_chart_widget = (
        create_plot_widget_single_view.validate()
        .partial(
            title="Events Bar Chart",
            **(params_dict.get("events_bar_chart_widget") or {}),
        )
        .map(argnames=["view", "data"], argvalues=events_bar_chart_html_url)
    )

    grouped_bar_plot_widget_merge = (
        merge_widget_views.validate()
        .partial(
            widgets=events_bar_chart_widget,
            **(params_dict.get("grouped_bar_plot_widget_merge") or {}),
        )
        .call()
    )

    grouped_events_map_layer = (
        create_point_layer.validate()
        .partial(
            layer_style={"fill_color_column": "event_type_colormap", "get_radius": 5},
            legend={
                "label_column": "event_type",
                "color_column": "event_type_colormap",
            },
            **(params_dict.get("grouped_events_map_layer") or {}),
        )
        .mapvalues(argnames=["geodataframe"], argvalues=split_event_groups)
    )

    grouped_events_ecomap = (
        draw_ecomap.validate()
        .partial(
            title=None,
            tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
            north_arrow_style={"placement": "top-left"},
            legend_style={"placement": "bottom-right"},
            static=False,
            **(params_dict.get("grouped_events_ecomap") or {}),
        )
        .mapvalues(argnames=["geo_layers"], argvalues=grouped_events_map_layer)
    )

    grouped_events_ecomap_html_url = (
        persist_text.validate()
        .partial(
            root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            **(params_dict.get("grouped_events_ecomap_html_url") or {}),
        )
        .mapvalues(argnames=["text"], argvalues=grouped_events_ecomap)
    )

    grouped_events_map_widget = (
        create_map_widget_single_view.validate()
        .partial(
            title="Events Map", **(params_dict.get("grouped_events_map_widget") or {})
        )
        .map(argnames=["view", "data"], argvalues=grouped_events_ecomap_html_url)
    )

    grouped_events_map_widget_merge = (
        merge_widget_views.validate()
        .partial(
            widgets=grouped_events_map_widget,
            **(params_dict.get("grouped_events_map_widget_merge") or {}),
        )
        .call()
    )

    grouped_events_pie_chart = (
        draw_pie_chart.validate()
        .partial(
            value_column="event_type",
            color_column="event_type_colormap",
            plot_style={"textinfo": "value"},
            label_column=None,
            layout_style=None,
            **(params_dict.get("grouped_events_pie_chart") or {}),
        )
        .mapvalues(argnames=["dataframe"], argvalues=split_event_groups)
    )

    grouped_pie_chart_html_urls = (
        persist_text.validate()
        .partial(
            root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            **(params_dict.get("grouped_pie_chart_html_urls") or {}),
        )
        .mapvalues(argnames=["text"], argvalues=grouped_events_pie_chart)
    )

    grouped_events_pie_chart_widgets = (
        create_plot_widget_single_view.validate()
        .partial(
            title="Events Pie Chart",
            **(params_dict.get("grouped_events_pie_chart_widgets") or {}),
        )
        .map(argnames=["view", "data"], argvalues=grouped_pie_chart_html_urls)
    )

    grouped_events_pie_widget_merge = (
        merge_widget_views.validate()
        .partial(
            widgets=grouped_events_pie_chart_widgets,
            **(params_dict.get("grouped_events_pie_widget_merge") or {}),
        )
        .call()
    )

    events_meshgrid = (
        create_meshgrid.validate()
        .partial(
            aoi=events_add_temporal_index,
            intersecting_only=False,
            **(params_dict.get("events_meshgrid") or {}),
        )
        .call()
    )

    grouped_events_feature_density = (
        calculate_feature_density.validate()
        .partial(
            meshgrid=events_meshgrid,
            geometry_type="point",
            **(params_dict.get("grouped_events_feature_density") or {}),
        )
        .mapvalues(argnames=["geodataframe"], argvalues=split_event_groups)
    )

    grouped_fd_colormap = (
        apply_color_map.validate()
        .partial(
            input_column_name="density",
            colormap="RdYlGn_r",
            output_column_name="density_colormap",
            **(params_dict.get("grouped_fd_colormap") or {}),
        )
        .mapvalues(argnames=["df"], argvalues=grouped_events_feature_density)
    )

    sort_grouped_density_values = (
        sort_values.validate()
        .partial(
            column_name="density",
            ascending=True,
            na_position="last",
            **(params_dict.get("sort_grouped_density_values") or {}),
        )
        .mapvalues(argnames=["df"], argvalues=grouped_fd_colormap)
    )

    grouped_feature_density_format = (
        map_values_with_unit.validate()
        .partial(
            original_unit=None,
            new_unit=None,
            input_column_name="density",
            output_column_name="density",
            decimal_places=0,
            **(params_dict.get("grouped_feature_density_format") or {}),
        )
        .mapvalues(argnames=["df"], argvalues=sort_grouped_density_values)
    )

    grouped_fd_map_layer = (
        create_polygon_layer.validate()
        .partial(
            layer_style={
                "fill_color_column": "density_colormap",
                "get_line_width": 0,
                "opacity": 0.4,
            },
            legend={"label_column": "density", "color_column": "density_colormap"},
            **(params_dict.get("grouped_fd_map_layer") or {}),
        )
        .mapvalues(argnames=["geodataframe"], argvalues=grouped_feature_density_format)
    )

    grouped_fd_ecomap = (
        draw_ecomap.validate()
        .partial(
            title=None,
            tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
            north_arrow_style={"placement": "top-left"},
            legend_style={"title": "Number of events", "placement": "bottom-right"},
            static=False,
            **(params_dict.get("grouped_fd_ecomap") or {}),
        )
        .mapvalues(argnames=["geo_layers"], argvalues=grouped_fd_map_layer)
    )

    grouped_fd_ecomap_html_url = (
        persist_text.validate()
        .partial(
            root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            **(params_dict.get("grouped_fd_ecomap_html_url") or {}),
        )
        .mapvalues(argnames=["text"], argvalues=grouped_fd_ecomap)
    )

    grouped_fd_map_widget = (
        create_map_widget_single_view.validate()
        .partial(
            title="Density Map", **(params_dict.get("grouped_fd_map_widget") or {})
        )
        .map(argnames=["view", "data"], argvalues=grouped_fd_ecomap_html_url)
    )

    grouped_fd_map_widget_merge = (
        merge_widget_views.validate()
        .partial(
            widgets=grouped_fd_map_widget,
            **(params_dict.get("grouped_fd_map_widget_merge") or {}),
        )
        .call()
    )

    events_dashboard = (
        gather_dashboard.validate()
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
            **(params_dict.get("events_dashboard") or {}),
        )
        .call()
    )

    return events_dashboard
