from __future__ import annotations

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pymatgen.core import Structure
import crystal_toolkit.components as ctc
import base64

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("CIF File Upload Visualization"),
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload File'),
        multiple=False
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output-message'),
    html.Div(id='output-structure')
])

@app.callback(
    Output('output-message', 'children'),
    Output('output-structure', 'children'),
    Input('submit-button', 'n_clicks'),
    State('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def display_message(n_clicks, contents, filename):
    if n_clicks > 0 and contents is not None:
        # Decode and process CIF file
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        structure = Structure.from_str(decoded.decode('utf-8'), fmt='cif')
        structure_component = ctc.StructureMoleculeComponent(structure, id="structure")
        
        # Create visualization layout
        layout = html.Div([structure_component.layout()])
        
        # Display the message and visualization
        return "Congratulations!", layout
    
    return "", ""

# Register Crystal Toolkit layout
ctc.register_crystal_toolkit(app, layout=app.layout)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
