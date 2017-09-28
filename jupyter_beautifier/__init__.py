from IPython.display import HTML, display


def show_code_option():
    """
    Puts a input on jupyter notebook to show/hide code

    Returns
    -------
    IPython.display.HTML
    """
    val = HTML("""
    <script>
        function code_toggle() {
            if (code_shown) {
                $('div.input').hide('500');
                $('#toggleButton').val('Show Code')
            } else {
                $('div.input').show('500');
                $('#toggleButton').val('Hide Code')
            }
            code_shown = !code_shown
        }
    
        $(document).ready(function () {
            code_shown = true;
            $('div.input').show()
        })
    </script>
    <form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>
    """)
    return display(val)


def hide_element(element):
    """ Hide specific element """

    html_string = """
        <style>
            {} {{display: None;}}
        </style>
    """.format(element)

    return display(HTML(html_string))


def show_element(element):
    """ Shows specific element"""

    html_string = """
       <style>
            {} {{display: 1;}}
        </style>
    """.format(element)

    return display(HTML(html_string))


def set_container_width(width):
    """Sets width of notebook """

    if not (25 <= width <= 100):
        raise ValueError('width is out-of-bound')

    html_string = """
    <style>
        .container {{ width: {}% !important; }}
    </style>
    """.format(width)

    return display(HTML(html_string))


def set_plot_align(text_align, vertical_align):
    """
    Sets align of output_png class

    Parameters
    -----------
    text_align: str
    vertical_align: str
    """

    html_string = """
    <style>
        .output_png {{
            display: table-cell;
            text-align: {text_align};
            vertical-align: {vertical_align};
        }}
    </style>
    """.format(text_align=text_align, vertical_align=vertical_align)

    return display(HTML(html_string))
