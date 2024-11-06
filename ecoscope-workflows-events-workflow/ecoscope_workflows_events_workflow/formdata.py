# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "6581c63822e13f69ae1b49518ecca8fd71c6ab4f149fa76fd14fcc3fd3ca48e7"


from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, confloat


class WorkflowDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str = Field(..., description="The name of your workflow", title="Name")
    description: str = Field(..., description="A description", title="Description")
    image_url: Optional[str] = Field("", description="An image url", title="Image Url")


class TimeRange(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    since: AwareDatetime = Field(..., description="The start time", title="Since")
    until: AwareDatetime = Field(..., description="The end time", title="Until")


class GetEventsData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    client: str = Field(
        ..., description="A named EarthRanger connection.", title="Client"
    )
    event_types: List[str] = Field(
        ..., description="list of event types", title="Event Types"
    )
    event_columns: List[str] = Field(
        ..., description="The interested event columns", title="Event Columns"
    )


class EventsColormap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ...,
        description="The name of the column with categorical values.",
        title="Input Column Name",
    )
    colormap: Optional[str] = Field(
        "viridis", description="A named matplotlib colormap.", title="Colormap"
    )
    output_column_name: Optional[str] = Field(
        None,
        description="The dataframe column that will contain the color values.",
        title="Output Column Name",
    )


class EventsMapWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class TimeInterval(str, Enum):
    year = "year"
    month = "month"
    week = "week"
    day = "day"
    hour = "hour"


class EventsBarChartWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class EventsMeshgrid(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    cell_width: Optional[int] = Field(
        5000, description="The width of a grid cell in meters.", title="Cell Width"
    )
    cell_height: Optional[int] = Field(
        5000, description="The height of a grid cell in meters.", title="Cell Height"
    )
    intersecting_only: Optional[bool] = Field(
        False,
        description="Whether to return only grid cells intersecting with the aoi.",
        title="Intersecting Only",
    )


class GeometryType(str, Enum):
    point = "point"
    line = "line"


class EventsFeatureDensity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    geometry_type: GeometryType = Field(
        ...,
        description="The geometry type of the provided geodataframe",
        title="Geometry Type",
    )


class FdColormap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ...,
        description="The name of the column with categorical values.",
        title="Input Column Name",
    )
    colormap: Optional[str] = Field(
        "viridis", description="A named matplotlib colormap.", title="Colormap"
    )
    output_column_name: Optional[str] = Field(
        None,
        description="The dataframe column that will contain the color values.",
        title="Output Column Name",
    )


class FdMapWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class GroupedEventsMapWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class GroupedEventsPieChartWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class GroupedEventsFeatureDensity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    geometry_type: GeometryType = Field(
        ...,
        description="The geometry type of the provided geodataframe",
        title="Geometry Type",
    )


class GroupedFdColormap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ...,
        description="The name of the column with categorical values.",
        title="Input Column Name",
    )
    colormap: Optional[str] = Field(
        "viridis", description="A named matplotlib colormap.", title="Colormap"
    )
    output_column_name: Optional[str] = Field(
        None,
        description="The dataframe column that will contain the color values.",
        title="Output Column Name",
    )


class GroupedFdMapWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class Grouper(BaseModel):
    index_name: str = Field(..., title="Index Name")


class Directive(str, Enum):
    field_a = "%a"
    field_A = "%A"
    field_b = "%b"
    field_B = "%B"
    field_c = "%c"
    field_d = "%d"
    field_f = "%f"
    field_H = "%H"
    field_I = "%I"
    field_j = "%j"
    field_m = "%m"
    field_M = "%M"
    field_p = "%p"
    field_S = "%S"
    field_U = "%U"
    field_w = "%w"
    field_W = "%W"
    field_x = "%x"
    field_X = "%X"
    field_y = "%y"
    field_Y = "%Y"
    field_z = "%z"
    field__ = "%%"


class TemporalGrouper(BaseModel):
    index_name: str = Field(..., title="Index Name")
    directive: Directive = Field(..., title="Directive")


class TimeRange1(BaseModel):
    since: AwareDatetime = Field(..., title="Since")
    until: AwareDatetime = Field(..., title="Until")
    time_format: Optional[str] = Field("%d %b %Y %H:%M:%S %Z", title="Time Format")


class LegendDefinition(BaseModel):
    label_column: Optional[str] = Field(None, title="Label Column")
    color_column: Optional[str] = Field(None, title="Color Column")
    labels: Optional[List[str]] = Field(None, title="Labels")
    colors: Optional[List[str]] = Field(None, title="Colors")


class Placement(str, Enum):
    top_left = "top-left"
    top_right = "top-right"
    bottom_left = "bottom-left"
    bottom_right = "bottom-right"
    fill = "fill"


class LegendStyle(BaseModel):
    placement: Optional[Placement] = Field("bottom-right", title="Placement")


class NorthArrowStyle(BaseModel):
    placement: Optional[Placement] = Field("top-left", title="Placement")
    style: Optional[Dict[str, Any]] = Field({"transform": "scale(0.8)"}, title="Style")


class LineWidthUnits(str, Enum):
    meters = "meters"
    pixels = "pixels"


class RadiusUnits(str, Enum):
    meters = "meters"
    pixels = "pixels"


class PointLayerStyle(BaseModel):
    filled: Optional[bool] = Field(True, title="Filled")
    get_fill_color: Optional[str] = Field(None, title="Get Fill Color")
    get_line_color: Optional[str] = Field(None, title="Get Line Color")
    get_line_width: Optional[float] = Field(1, title="Get Line Width")
    fill_color_column: Optional[str] = Field(None, title="Fill Color Column")
    line_width_units: Optional[LineWidthUnits] = Field(
        "pixels", title="Line Width Units"
    )
    get_radius: Optional[float] = Field(5, title="Get Radius")
    radius_units: Optional[RadiusUnits] = Field("pixels", title="Radius Units")


class PolygonLayerStyle(BaseModel):
    filled: Optional[bool] = Field(True, title="Filled")
    get_fill_color: Optional[str] = Field(None, title="Get Fill Color")
    get_line_color: Optional[str] = Field(None, title="Get Line Color")
    get_line_width: Optional[float] = Field(1, title="Get Line Width")
    fill_color_column: Optional[str] = Field(None, title="Fill Color Column")
    line_width_units: Optional[LineWidthUnits] = Field(
        "pixels", title="Line Width Units"
    )
    extruded: Optional[bool] = Field(False, title="Extruded")
    get_elevation: Optional[float] = Field(1000, title="Get Elevation")


class PolylineLayerStyle(BaseModel):
    pass


class TileLayer(BaseModel):
    name: str = Field(..., title="Name")
    opacity: Optional[float] = Field(1, title="Opacity")


class BarLayoutStyle(BaseModel):
    font_color: Optional[str] = Field(None, title="Font Color")
    font_style: Optional[str] = Field(None, title="Font Style")
    plot_bgcolor: Optional[str] = Field(None, title="Plot Bgcolor")
    showlegend: Optional[bool] = Field(None, title="Showlegend")
    bargap: Optional[confloat(ge=0.0, le=1.0)] = Field(None, title="Bargap")
    bargroupgap: Optional[confloat(ge=0.0, le=1.0)] = Field(None, title="Bargroupgap")


class LineStyle(BaseModel):
    color: Optional[str] = Field(None, title="Color")


class PlotCategoryStyle(BaseModel):
    marker_color: Optional[str] = Field(None, title="Marker Color")


class PlotStyle(BaseModel):
    xperiodalignment: Optional[str] = Field(None, title="Xperiodalignment")
    marker_colors: Optional[List[str]] = Field(None, title="Marker Colors")
    textinfo: Optional[str] = Field(None, title="Textinfo")
    line: Optional[LineStyle] = Field(None, title="Line")


class Groupers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groupers: List[Union[Grouper, TemporalGrouper]] = Field(
        ...,
        description="            Index(es) and/or column(s) to group by, along with\n            optional display names and help text.\n            ",
        title="Groupers",
    )


class EventsEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class FdEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class GroupedEventsEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class GroupedFdEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class LayerDefinition(BaseModel):
    geodataframe: Any = Field(..., title="Geodataframe")
    layer_style: Union[PolylineLayerStyle, PointLayerStyle, PolygonLayerStyle] = Field(
        ..., title="Layer Style"
    )
    legend: LegendDefinition


class GroupedPlotStyle(BaseModel):
    category: str = Field(..., title="Category")
    plot_style: PlotCategoryStyle


class EventsBarChart(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_interval: TimeInterval = Field(
        ..., description="Sets the time interval of the x axis.", title="Time Interval"
    )
    grouped_styles: Optional[List[GroupedPlotStyle]] = Field(
        [],
        description="Style arguments passed to plotly.graph_objects.Bar and applied to individual groups.",
        title="Grouped Styles",
    )


class FormData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_details: Optional[WorkflowDetails] = Field(
        None, title="Set Workflow Details"
    )
    groupers: Optional[Groupers] = Field(None, title="Set Groupers")
    time_range: Optional[TimeRange] = Field(None, title="Set Time Range Filters")
    get_events_data: Optional[GetEventsData] = Field(
        None, title="Get Events from EarthRanger"
    )
    events_colormap: Optional[EventsColormap] = Field(None, title="Events Colormap")
    events_ecomap: Optional[EventsEcomap] = Field(
        None, title="Draw Ecomap from Time Density"
    )
    events_map_widget: Optional[EventsMapWidget] = Field(
        None, title="Create Time Density Map Widget"
    )
    events_bar_chart: Optional[EventsBarChart] = Field(
        None, title="Draw Time Series Bar Chart for Events"
    )
    events_bar_chart_widget: Optional[EventsBarChartWidget] = Field(
        None, title="Create Plot Widget for Events"
    )
    events_meshgrid: Optional[EventsMeshgrid] = Field(
        None, title="Create Events Meshgrid"
    )
    events_feature_density: Optional[EventsFeatureDensity] = Field(
        None, title="Events Feature Density"
    )
    fd_colormap: Optional[FdColormap] = Field(None, title="Feature Density Colormap")
    fd_ecomap: Optional[FdEcomap] = Field(
        None, title="Draw Ecomap from Feature Density"
    )
    fd_map_widget: Optional[FdMapWidget] = Field(
        None, title="Create Feature Density Map Widget"
    )
    grouped_events_ecomap: Optional[GroupedEventsEcomap] = Field(
        None, title="Draw Ecomap from grouped Events"
    )
    grouped_events_map_widget: Optional[GroupedEventsMapWidget] = Field(
        None, title="Create grouped Events Map Widget"
    )
    grouped_events_pie_chart_widgets: Optional[GroupedEventsPieChartWidgets] = Field(
        None, title="Create Plot Widget for Events"
    )
    grouped_events_feature_density: Optional[GroupedEventsFeatureDensity] = Field(
        None, title="Grouped Events Feature Density"
    )
    grouped_fd_colormap: Optional[GroupedFdColormap] = Field(
        None, title="Grouped Feature Density Colormap"
    )
    grouped_fd_ecomap: Optional[GroupedFdEcomap] = Field(
        None, title="Draw Ecomap from Feature Density"
    )
    grouped_fd_map_widget: Optional[GroupedFdMapWidget] = Field(
        None, title="Create Feature Density Map Widget"
    )
