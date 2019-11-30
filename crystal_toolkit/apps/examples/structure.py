# standard Dash imports
import dash
import dash_html_components as html
import dash_core_components as dcc

# standard Crystal Toolkit import
import crystal_toolkit.components as ctc

# import for this example
from pymatgen import Structure, Lattice

# create Dash app as normal
app = dash.Dash()

# If callbacks created dynamically they cannot be statically checked at app startup.
# For this simple example this is not a problem, but if creating a complicated,
# nested layout this will need to be enabled -- consult Dash documentation
# for more information.
# app.config["suppress_callback_exceptions"] = True

# tell Crystal Toolkit about the app
ctc.register_app(app)

# create the Structure object
structure = Structure(Lattice.cubic(5), ["H"], [[0, 0, 0]])

# create the Crystal Toolkit component
structure_component = ctc.StructureMoleculeComponent(structure)

# example layout to demonstrate capabilities of component
my_layout = html.Div(
    [
        html.H1("StructureMoleculeComponent Example"),
        html.H2("Standard Layout"),
        structure_component.layout,
        html.H2("Optional Additional Layouts"),
        html.H3("Screenshot Layout"),
        structure_component.screenshot_layout,
        html.H3("Options Layout"),
        structure_component.options_layout,
        html.H3("Title Layout"),
        structure_component.title_layout,
        html.H3("Legend Layout"),
        structure_component.legend_layout,
        html.H2("Technical Details"),
        dcc.Markdown(str(structure_component)),
    ]
)

# wrap your app.layout with crystal_toolkit_layout()
# to ensure all necessary components are loaded into layout
app.layout = ctc.crystal_toolkit_layout(my_layout)


# allow app to be run using "python structure.py"
# in production, deploy behind gunicorn or similar
# see Dash documentation for more information
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
