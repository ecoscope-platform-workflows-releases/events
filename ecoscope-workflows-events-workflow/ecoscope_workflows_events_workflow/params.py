# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "ab0fe8d27af828622e9e2ee7237e1c87056198e47aca9d007cbf1753deb17bc2"


from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, confloat


class WorkflowDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str = Field(..., description="The name of your workflow", title="Name")
    description: str = Field(..., description="A description", title="Description")
    image_url: Optional[str] = Field("", description="An image url", title="Image Url")


class ErClientName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    EcoscopeWorkflowsNamedConnection: str = Field(
        ..., description="A named connection.", title="Name"
    )


class TimeRange(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    since: datetime = Field(..., description="The start time", title="Since")
    until: datetime = Field(..., description="The end time", title="Until")


class GetEventsData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    event_types: List[str] = Field(
        ..., description="list of event types", title="Event Types"
    )


class TimeInterval(str, Enum):
    year = "year"
    month = "month"
    week = "week"
    day = "day"
    hour = "hour"


class EventsBarChart(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_interval: TimeInterval = Field(
        ..., description="Sets the time interval of the x axis.", title="Time Interval"
    )


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
    since: datetime = Field(..., title="Since")
    until: datetime = Field(..., title="Until")
    time_format: Optional[str] = Field("%d %b %Y %H:%M:%S %Z", title="Time Format")


class BarLayoutStyle(BaseModel):
    font_color: Optional[str] = Field(None, title="Font Color")
    font_style: Optional[str] = Field(None, title="Font Style")
    plot_bgcolor: Optional[str] = Field(None, title="Plot Bgcolor")
    showlegend: Optional[bool] = Field(None, title="Showlegend")
    title: Optional[str] = Field(None, title="Title")
    title_x: Optional[confloat(ge=0.0, le=1.0)] = Field(None, title="Title X")
    title_y: Optional[confloat(ge=0.0, le=1.0)] = Field(None, title="Title Y")
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


class Params(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_details: Optional[WorkflowDetails] = Field(
        None, title="Set Workflow Details"
    )
    er_client_name: Optional[ErClientName] = Field(
        None, title="Select EarthRanger Connection"
    )
    groupers: Optional[Groupers] = Field(None, title="Set Groupers")
    time_range: Optional[TimeRange] = Field(None, title="Set Time Range Filters")
    get_events_data: Optional[GetEventsData] = Field(
        None, title="Get Events from EarthRanger"
    )
    events_bar_chart: Optional[EventsBarChart] = Field(
        None, title="Draw Time Series Bar Chart for Events"
    )


class GroupedPlotStyle(BaseModel):
    category: str = Field(..., title="Category")
    plot_style: PlotCategoryStyle
