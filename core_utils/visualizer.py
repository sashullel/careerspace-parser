"""
Visualizer module for visualizing frequency of each quailification level
based on Excel worksheet 'Уровень' column
"""
from pathlib import Path

try:
    import plotly
    import plotly.express as px

except ImportError:
    print('No libraries installed. Failed to import.')

from openpyxl.worksheet.worksheet import Worksheet


def visualize(ws: Worksheet, path_to_save: Path) -> None:
    """
    param: ws is an instance of the Worksheet class
    """
    column_name = 'Уровень'
    frequencies = {
        'Junior': 0,
        'Middle': 0,
        'Senior': 0,
        'Не указано': 0
    }

    for col in ws.iter_cols():
        if col[0].value == column_name:
            for cell in col[1:]:
                if not cell.value:
                    frequencies['Не указано'] = frequencies.get('Не указано') + 1
                    continue
                if 'Junior' in cell.value:
                    frequencies['Junior'] = frequencies.get('Junior') + 1
                if 'Middle' in cell.value:
                    frequencies['Middle'] = frequencies.get('Middle') + 1
                if 'Senior' in cell.value:
                    frequencies['Senior'] = frequencies.get('Senior') + 1
            break

    fig = px.pie(values=frequencies.values(),
                 names=frequencies.keys(),
                 opacity=0.75)

    fig.update_layout(showlegend=True, legend=dict(
        title_font_family='Courier New',
        font=dict(size=25)
    ))

    fig.write_html(path_to_save)
