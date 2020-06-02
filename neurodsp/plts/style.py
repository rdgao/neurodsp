"""Style helpers and utilities for plots."""

from functools import wraps

import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

PLOT_STYLE_ARGS = ['title', 'xlabel', 'ylabel', 'xlim', 'ylim']
LINE_STYLE_ARGS = ['alpha', 'lw']

def plot_style(ax, **kwargs):
    """Define plot style."""

    # Set any provided plot arguments
    ax.set(**kwargs)

    # Aesthetics and axis labels
    ax.xaxis.label.set_size(16)
    ax.yaxis.label.set_size(16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    # If labels were provided, add a legend
    if ax.get_legend_handles_labels()[0]:
        ax.legend(prop={'size': 12}, loc='best')

    # If a title was provided, update the size
    if ax.get_title():
        ax.title.set_size(20)

    plt.tight_layout()


def style_plot(func, *args, **kwargs):
    """Decorator function to apply a plot style function, after plot generation."""

    @wraps(func)
    def decorated(*args, **kwargs):

        # Grab a custom style function, if provided, and grab any provided style arguments
        style_func = kwargs.pop('plot_style', plot_style)
        style_kwargs = {key : kwargs.pop(key) for key in PLOT_STYLE_ARGS if key in kwargs}
        line_kwargs = {key : kwargs.pop(key) for key in LINE_STYLE_ARGS if key in kwargs}

        # Create the plot
        func(*args, **kwargs)

        # Get plot axis, if a specific one was provided, or just grab current and apply style
        cur_ax = kwargs['ax'] if 'ax' in kwargs and kwargs['ax'] is not None else plt.gca()
        style_func(cur_ax, **style_kwargs)

        # Apply line styles
        for line_style in LINE_STYLE_ARGS:

            # Ensure argument is valid
            if line_style in line_kwargs.keys() and line_kwargs[line_style] is not None:

                # Change style line-by-line
                for idx, line in enumerate(cur_ax.lines):

                    if line_style == 'lw':
                        try:
                            line.set_linewidth(line_kwargs[line_style][idx])
                        except TypeError:
                            # If an arg is not iterable, all lines will have the same style.
                            line.set_linewidth(line_kwargs[line_style])

                    if line_style == 'alpha':
                        try:
                            line.set_alpha(line_kwargs[line_style][idx])
                        except TypeError:
                            # If an arg is not iterable, all lines will have the same style.
                            line.set_alpha(line_kwargs[line_style])

    return decorated
