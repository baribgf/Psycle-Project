"""
PyShS v1.0
-----------

A python module to style strings with multiple features.

Example:

>>> from pyshs import styled
>>> text = 'Hello world'
>>> styled_text = styled(text=text, fg='white', bg='blue', style='bold')
>>> print(styled_text)
>>> # Output: the bold text 'Hello world' with white in a blue background 
"""

from colorama.ansi import Fore, Back, Style, code_to_chars

Style.__setattr__('BOLD', Style.BRIGHT)
Style.__setattr__('ITALIC', code_to_chars(3))
Style.__setattr__('UNDERLINED', code_to_chars(4))

def start_feature(feature: str, value: str) -> str:
    """
    Starts styling with one of the features: `fg`, `bg`, `style`

    Args:
        - `feature`: the style feature name to be started
        - `value`: the value of the feature
    """

    understyle = None

    if feature == "fg":
        understyle = Fore.__getattribute__(value.upper())

    elif feature == "bg":
        understyle = Back.__getattribute__(value.upper())

    elif feature == "style":
        understyle = Style.__getattribute__(value.upper())
    
    else:
        raise ValueError('feature must be either: "fg", "bg", "style"')

    return understyle

def end_feature(feature: str) -> str:
    """
    Ends styling with one of the features: `fg`, `bg`, `style`
    
    Args:
        - `feature`: the style feature name to be ended

    -> `Note`: the end feature style will end all other features
    """

    understyle = None

    if feature == "fg":
        understyle = Fore.RESET

    elif feature == "bg":
        understyle = Back.RESET

    elif feature == "style":
        understyle = Style.RESET_ALL
    
    else:
        raise ValueError('feature must be either: "fg", "bg", "style"')

    return understyle

def styled(text: str, fg: str = None, bg: str = None, style: str = None) -> str:
    """
    Returns a stylized text with:
        * `Foreground`
        * `Background`
        * `Text style`

    Provided:
        * `fg`:
            - `Standard`: BLACK - RED - GREEN - YELLOW - BLUE - MAGENTA - CYAN - WHITE
            - `Fairely supported`: LIGHTBLACK_EX - LIGHTRED_EX - LIGHTGREEN_EX - LIGHTYELLOW_EX - LIGHTBLUE_EX - LIGHTMAGENTA_EX - LIGHTCYAN_EX - LIGHTWHITE_EX

        * `bg`:
            - `Standard`: BLACK - RED - GREEN - YELLOW - BLUE - MAGENTA - CYAN - WHITE
            - `Fairely supported`: LIGHTBLACK_EX - LIGHTRED_EX - LIGHTGREEN_EX - LIGHTYELLOW_EX - LIGHTBLUE_EX - LIGHTMAGENTA_EX - LIGHTCYAN_EX - LIGHTWHITE_EX

        * `style`:
            - BRIGHT or BOLD - ITALIC - UNDERLINED - DIM - NORMAL
    """

    try:
        styled_text = str(text)

        if fg is not None:
            styled_text = start_feature('fg', fg) + styled_text + end_feature('fg')

        if bg is not None:
            styled_text = start_feature('bg', bg) + styled_text + end_feature('bg')

        if style is not None:
            styled_text = start_feature('style', style) + styled_text + end_feature('style')

        return styled_text

    except AttributeError:
        args_sum = {"fg": fg, "bg": bg, "style": style}
        print(styled(f"[{__file__.split('/')[-2]}] WARNING: Invalid features value passed {args_sum}, original text will be returned", 'red'))
        return text
